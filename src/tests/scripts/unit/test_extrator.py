import os
import unittest
from unittest.mock import MagicMock, patch
from src.exceptions.exceptions import DataExtractException
from src.scripts.extractor import DataExtractor, UrlDataExtractStrategy

# Define o diretório de teste com base no diretório do arquivo de teste
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
# Define o caminho completo para o arquivo de teste dentro do diretório de teste
TEST_FILE = os.path.join(TEST_DIR, "test_file.txt")

class TestUrlDataExtractStrategy(unittest.TestCase):
    def setUp(self):
        # Inicializa a estratégia de extração e define a URL e o nome do arquivo para os testes
        self.strategy = UrlDataExtractStrategy()
        self.url = "http://example.com/data"
        self.filename = TEST_FILE

    @patch('urllib.request.urlretrieve')
    def test_extract_success(self, mock_urlretrieve):
        # Mock para simular um download de arquivo bem-sucedido
        mock_urlretrieve.return_value = None

        # Chama o método de extração
        self.strategy.extract(self.url, self.filename)

        # Simula a criação do arquivo no sistema de arquivos
        with open(self.filename, 'w') as f:
            f.write('Test data')

        # Verifica se urlretrieve foi chamado com os parâmetros corretos
        mock_urlretrieve.assert_called_once_with(self.url, self.filename)
        # Verifica se o arquivo foi criado (mesmo que esteja vazio, pois urlretrieve é mockado)
        self.assertTrue(os.path.exists(self.filename))

        # Limpa o arquivo criado
        if os.path.exists(self.filename):
            os.remove(self.filename)

    @patch('urllib.request.urlretrieve', side_effect=Exception("Erro de download"))
    def test_extract_failure(self, mock_urlretrieve):
        # Verifica se uma exceção DataExtractException é levantada corretamente ao ocorrer um erro
        with self.assertRaises(DataExtractException) as context:
            self.strategy.extract(self.url, self.filename)

        self.assertEqual(str(context.exception), "Erro ao extrair dados: Erro de download")

        # Verifica se o arquivo não foi criado
        self.assertFalse(os.path.exists(self.filename))


class TestDataExtractor(unittest.TestCase):
    def setUp(self):
        # Inicializa um mock para a estratégia de extração e o DataExtractor
        self.strategy = MagicMock()
        self.extractor = DataExtractor(self.strategy)
        self.url = "http://example.com/data"
        self.filename = TEST_FILE

    def test_extract_calls_strategy(self):
        # Chama o método de extração e verifica se a estratégia foi chamada corretamente
        self.extractor.extract(self.url, self.filename)
        self.strategy.extract.assert_called_once_with(self.url, self.filename)
