from src.mlProject.logger import logging
from src.mlProject.exception import CustomException
from src.mlProject.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.mlProject.components.data_transformation import DataTransformation, DataTransformationConfig
from src.mlProject.components.model_trainer import ModelTrainer, ModelTrainerConfig
import sys



if __name__ == "__main__":
    logging.info("Application started")
    try:
        
        data_ingestion = DataIngestion() 
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        #data_transformation_config = DataTransformationConfig()
        data_transformation = DataTransformation()
        train_array,test_array,_ =data_transformation.initiate_data_transformation(train_path=train_data_path,test_path=test_data_path)
    
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_array,test_array))
        
    except Exception as e:
        logging.info("Custom exception raised")
        raise CustomException(e,sys)
