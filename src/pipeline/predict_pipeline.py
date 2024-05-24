import os,sys
import pandas as pd
from src.logger import logging

from src.exception import CustomException
import sys
from flask import request
from src.constant import *
from src.utils import download_model , load_object

from dataclasses import dataclass

@dataclass
class PredicationFileDetails:
    predication_output_dirname : str= "predications"
    predication_file_name:str = "predication_file.csv"
    predication_file_path:str = os.path.join(predication_output_dirname,predication_file_name)

class PredicationPipeline:
    def __init__(self,request):
        self.request = request
        self.predication_file_detail = PredicationFileDetails()
        
    def save_input_files(self) ->str:
        try:
            pred_file_input_dir = 'predication_artifacts'
            os.makedirs(pred_file_input_dir,exist_ok=True)
            
            input_csv_file = self.request.files['file']
            pred_file_path = os.path.join(pred_file_input_dir,input_csv_file.filename)
            input_csv_file.save(pred_file_path)
            return pred_file_path
        except Exception as e:
            raise CustomException(e,sys)
    
    def predict(self,features):
        try:
            # model_path = download_model(
            #     bucket_name="something",
            #     bucket_file_name="model.pkl",
            #     dest_file_name = 'model.pkl'
            #                             )
            
            model_path = '../../artifacts/model.pkl'
            model = load_object(file_path=model_path)
            
            preds = model.predic(features)
            return preds
        except Exception as e:
            raise CustomException (e,sys)
    
    def get_predicated_dataframe(self,input_dataframe_path:pd.DataFrame):
        try:
            predication_column_name : str = "Good/Bad"
            input_dataframe:pd.DataFrame = pd.read_csv(input_dataframe_path)
            predications = self.predict(input_dataframe)
            input_dataframe[predication_column_name] = [pred for pred in predications]
            target_column_mapping = {0:'negative',1:'positive'}
            
            input_dataframe[predication_column_name] = input_dataframe[predication_column_name].map(target_column_mapping)
            
            os.makedirs(self.predication_file_detail.predication_output_dirname,exist_ok=True)
            
            input_dataframe.to_csv(self.predication_file_detail.predication_file_path,index=False)
            
            logging.info("Predication complete . ")
        except Exception as e:
            raise CustomException (e,sys)
    
    def runpipeline(self):
        try:
            input_csv_path = self.save_input_files()
            self.get_predicated_dataframe(input_csv_path)
            return self.predication_file_detail
        except Exception as e:
            raise CustomException (e,sys)