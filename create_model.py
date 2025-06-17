from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__=="__main__":
    data_ingestion=DataIngestion()
    train_data_path,test_data_path = data_ingestion.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    train_arr,test_arr,obj = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    
    modeltrainer = ModelTrainer()
    best_model_name,r2_score = modeltrainer.initiate_model_trainer(train_arr,test_arr)
    print(f"The best model that is selected is: {best_model_name}")
    print(f"The accuracy score of the best model is {r2_score}")