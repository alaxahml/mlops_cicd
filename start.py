import mlops_cicd

RAW_DATA_PATH = "data/raw/all_v2.csv"
REGIONAL_DATA_PATH = "data/interim/data_regional.csv"
CLEANED_DATA_PATH = "data/interim/data_cleaned.csv"
FEATURED_DATA_PATH = "data/processed/data_featured.csv"
REGION_ID = 2661


if __name__ == "__main__":
    mlops_cicd.select_region(RAW_DATA_PATH, REGIONAL_DATA_PATH, REGION_ID)
    mlops_cicd.clean_data(REGIONAL_DATA_PATH, CLEANED_DATA_PATH)
    mlops_cicd.add_features(CLEANED_DATA_PATH, FEATURED_DATA_PATH)
