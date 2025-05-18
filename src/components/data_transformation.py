import sys
import os
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer ## it help to missing value by replacing mean,mode,median
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artificats',"preprocessor.pkl")
    
class DataTraformation:
    #constrocter
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
        
        ##methode
    def get_datatransformer_object(self):    
        try:
            numeric_column=["writing_score","reading_score"]
            categorical_column=[ "gender",
            "race_ethnicity",
            "parental_level_of_education",
            "lunch",
            "test_preparation_course",]
                
               ## create pipline
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                   ]
            ) 
                
            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler(with_mean=False))
                    ]
            )
            logging.info(f"Categorical column: {categorical_column}")
            logging.info(f"Numerical columns: {numeric_column}")
                
            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numeric_column),
                    ("cat_pipeline",cat_pipeline,categorical_column)
                    ]
            )
                
            return preprocessor
                
        except Exception as e:
            raise CustomException(e,sys)
                
                  
            
      ##method      
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
                
            logging.info("Reading test train data complete")
            logging.info("Obtaining preprocessing obj")
                
            preprocessing_obj=self.get_datatransformer_object()
            
            targeted_column_name="math_score"
            numerical_columns=["writing_score","reading_score"] 
            
            input_feature_train=train_df.drop(columns=[targeted_column_name],axis=1)
            targeted_feature_train=train_df[targeted_column_name]
            
            input_feature_test=test_df.drop(columns=[targeted_column_name],axis=1)   
            targeted_feature_test=test_df[targeted_column_name]
            
            logging.info(f"Applying preprocessing on training dataframe and testing datafrmae")
            
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test)
            
            train_arr=np.c_[input_feature_train_arr,np.array(targeted_feature_train)]
            test_arr=np.c_[input_feature_test_arr,np.array(targeted_feature_test)]
            
            logging.info(f"saved preprocessing object")
            
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
                
            )
        except Exception as e:
            raise CustomException(e,sys)
            