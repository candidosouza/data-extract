import os
import boto3
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='./../../.env', 
        env_file_encoding='utf-8'
    )
    AWS_ACCESS_KEY_S3: str = os.environ['AWS_ACCESS_KEY_S3']
    AWS_ACCESS_SECRET_KEY_S3: str = os.environ['AWS_ACCESS_SECRET_KEY_S3']
    AWS_BUCKET_NAME: str = os.environ['AWS_BUCKET_NAME']
    AWS_REGION_S3: str = os.environ['AWS_REGION_S3']


class AWSS3Client:
    def __init__(self, access_key_id, secret_access_key, region_name, profile_name=None, session=None):
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        self.region_name = region_name
        self.profile_name = profile_name
        self.session = session or self.default_session()

    def client(self):
        return self.session.client('s3')

    def default_session(self):
        if self.profile_name:
            return boto3.Session(profile_name=self.profile_name)
        else:
            return boto3.Session(
                aws_access_key_id=self.access_key_id,
                aws_secret_access_key=self.secret_access_key,
                region_name=self.region_name
            )

class ConfigBoto3:
    def __init__(self):
        self.aws_access_key_id = Settings().AWS_ACCESS_KEY_S3
        self.aws_secret_access_key = Settings().AWS_ACCESS_SECRET_KEY_S3
        self.region_name = Settings().AWS_REGION_S3

    def create_client(self, profile_name=None):
        return AWSS3Client(
            self.aws_access_key_id,
            self.aws_secret_access_key,
            self.region_name,
            profile_name
        )
