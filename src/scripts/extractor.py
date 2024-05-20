import os
import urllib.request

from src.exceptions.exceptions import DataExtractException

class DataExtractor:
    def __init__(self, strategy):
        self.strategy = strategy

    def extract(self, url, filename):
        self.strategy.extract(url, filename)

class UrlDataExtractStrategy:
    def extract(self, url, filename):
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            raise DataExtractException(f"Erro ao extrair dados: {e}")
