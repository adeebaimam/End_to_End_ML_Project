from src.mlProject.logger import logging
from src.mlProject.exception import CustomException
from src.mlProject.components.data_ingestion import DataIngestion, DataIngestionConfig
import sys



if __name__ == "__main__":
    logging.info("Application started")
    try:
        
        data_ingestion = DataIngestion() 
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom exception raised")
        raise CustomException(e,sys)
