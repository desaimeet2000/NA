import os
import pandas as pd
import numpy as np


TARGET_COLUMN = "Result"
PIPELINE_NAME = "NetworkSecurity"
ARTIFACT_DIR = "Artifacts"
FILE_NAME: str = "NetworkData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

"""DATA INGESTION CONSTANTS
"""

DATA_INGESTION_COLLECTION_NAME: str = "phishingData"
DATA_INGESTION_DATABASE_NAME: str = "NetworkSecurity"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2