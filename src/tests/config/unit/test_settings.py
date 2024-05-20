import unittest
from unittest.mock import MagicMock, patch
from src.config.settings import AWSS3Client, ConfigBoto3

class TestAWSS3Client(unittest.TestCase):
    
    def test_default_session_with_access_keys(self):
        access_key_id = "test_access_key_id"
        secret_access_key = "test_secret_access_key"
        region_name = "test_region"
        client = AWSS3Client(access_key_id, secret_access_key, region_name)

        session = client.default_session()

        self.assertEqual(session.region_name, region_name)
        self.assertEqual(session.get_credentials().access_key, access_key_id)
        self.assertEqual(session.get_credentials().secret_key, secret_access_key)

    @patch('src.config.settings.boto3.Session')
    def test_default_session_with_profile(self, mock_session):
        profile_name = "test_profile"
        mock_session.return_value.profile_name = profile_name
        client = AWSS3Client(None, None, None, profile_name=profile_name)

        session = client.default_session()

        self.assertEqual(session.profile_name, profile_name)

    @patch('src.config.settings.boto3.Session')
    def test_client_creation(self, mock_session):
        # Mockando o cliente S3
        mock_s3_client = MagicMock()
        mock_session.return_value.client.return_value = mock_s3_client
        
        # Criando instância do AWSS3Client
        client = AWSS3Client(None, None, None)
        
        # Chamando o método client
        s3_client = client.client()
        
        # Verificando se o método client da sessão foi chamado
        mock_session.return_value.client.assert_called_once_with('s3')
        
        # Verificando se o cliente retornado é o mock do cliente S3
        self.assertEqual(s3_client, mock_s3_client)

class TestConfigBoto3(unittest.TestCase):
    @patch('src.config.settings.AWSS3Client.default_session')
    def test_create_client(self, mock_default_session):
        expected_access_key_id = "test_access_key_id"
        expected_secret_access_key = "test_secret_access_key"
        expected_region_name = "test_region"

        # Criando um MagicMock para Settings
        settings_mock = MagicMock()
        settings_mock.AWS_ACCESS_KEY_S3 = expected_access_key_id
        settings_mock.AWS_ACCESS_SECRET_KEY_S3 = expected_secret_access_key
        settings_mock.AWS_REGION_S3 = expected_region_name

        # Criando uma instância de ConfigBoto3
        config = ConfigBoto3()

        config.create_client()

        # Verificando se o método default_session foi chamado corretamente
        mock_default_session.assert_called_once_with()
