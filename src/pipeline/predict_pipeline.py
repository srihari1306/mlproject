import os
import sys

import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path = 'artifacts\model.pkl'
            preprocessor_path = 'artifacts\preprocessor.pkl'
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
    
class CustomData:
    def __init__(self,
                 Make: str,
                 Kilometer:int, 
                 Fuel_Type:str, 
                 Transmission:str,
                 Location:str,
                 Color:str,
                 Owner:str,
                 Seller_Type:str,
                 Engine:float,
                 Drivetrain:str,
                 Length:float,
                 Width:float,
                 Height:float,
                 Seating_Capacity:int,
                 Fuel_Tank_Capacity:float,
                 power_per_rpm:float,
                 torque_per_rpm	:float,
                 Age:int) -> None:
        
        self.Make = Make
        self.Kilometer = Kilometer
        self.Fuel_type=Fuel_Type
        self.Transmission = Transmission
        self.Location = Location
        self.Color = Color
        self.Owner = Owner
        self.Seller_Type = Seller_Type
        self.Engine = Engine
        self.Drivetrain = Drivetrain
        self.Length = Length
        self.Width = Width
        self.Height = Height
        self.Seating_Capacity = Seating_Capacity
        self.Fuel_Tank_Capacity =Fuel_Tank_Capacity
        self.power_per_rpm = power_per_rpm
        self.torque_per_rpm = torque_per_rpm
        self.Age = Age
    
    def get_data_as_frame(self):
        try:
            custom_data_input_dict = {
                "Make": [self.Make],
                "Kilometer": [self.Kilometer],
                "Fuel Type": [self.Fuel_type],
                "Transmission": [self.Transmission],
                "Location": [self.Location],
                "Color": [self.Color],
                "Owner": [self.Owner],
                "Seller Type": [self.Seller_Type],
                "Engine": [self.Engine],
                "Drivetrain": [self.Drivetrain],
                "Length": [self.Length],
                "Width": [self.Width],
                "Height": [self.Height],
                "Seating Capacity": [self.Seating_Capacity],
                "Fuel Tank Capacity": [self.Fuel_Tank_Capacity],
                "power_per_rpm": [self.power_per_rpm],
                "torque_per_rpm": [self.torque_per_rpm],
                "Age": [self.Age]
            }
            
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e,sys)