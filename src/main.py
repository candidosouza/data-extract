from src.scripts.extractor import DataExtractor, UrlDataExtractStrategy
from src.config.settings import Settings

settings = Settings()
print(settings.AWS_BUCKET_NAME)


if __name__ == "__main__":
    pass
    # extractor = DataExtractor(UrlDataExtractStrategy())
    # extractor.extract("https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/c9509ab4-6f6d-4b97-979a-0cf2a10c922b/download/311_service_requests_2015.csv", "src/data/data_2015.csv")
    # extractor.extract("https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/b7ea6b1b-3ca4-4c5b-9713-6dc1db52379a/download/311_service_requests_2016.csv", "src/data/data_2016.csv")
    # extractor.extract("https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/30022137-709d-465e-baae-ca155b51927d/download/311_service_requests_2017.csv", "src/data/data_2017.csv")
    # extractor.extract("https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/2be28d90-3a90-4af1-a3f6-f28c1e25880a/download/311_service_requests_2018.csv", "src/data/data_2018.csv")
    # extractor.extract("https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/ea2e4696-4a2d-429c-9807-d02eb92e0222/download/311_service_requests_2019.csv", "src/data/data_2019.csv")
    # extractor.extract("https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/6ff6a6fd-3141-4440-a880-6f60a37fe789/download/script_105774672_20210108153400_combine.csv", "src/data/data_2020.csv")
