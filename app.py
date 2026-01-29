from src.mlProject.logger import logging
from src.mlProject.exception import CustomException
from src.mlProject.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.mlProject.components.data_transformation import DataTransformation, DataTransformationConfig
import sys



if __name__ == "__main__":
    logging.info("Application started")
    try:
        
        data_ingestion = DataIngestion() 
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        #data_transformation_config = DataTransformationConfig()
        data_transformation.initiate_data_transformation(train_path=train_data_path,test_path=test_data_path)
    
    except Exception as e:
        logging.info("Custom exception raised")
        raise CustomException(e,sys)
