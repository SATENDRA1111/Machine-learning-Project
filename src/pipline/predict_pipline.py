import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_obj



class predictpipline:
    def __init__(self):
        pass
    
    def prediction(self,feature):
        model_path=os.path.join('artificats','model.pkl')
        preprocessor_path=os.path.join('artificats','preprocessor.pkl')
        print('Before Loding')
        model=load_obj(file_path=model_path)
        preprocessor=load_obj(file_path=preprocessor_path)
        print('after_loading')
        scaled_data=preprocessor.transform(feature)
        preds=model.predict(scaled_data)
        return preds
        
    
 
 
 ## which data we are getting from front-end   
class CustomDate:
    def __init__(self,
                gender:str,
                race_ethnicity:str,
                parental_level_of_education,
                lunch:str,
                test_preparation_course:str,
                reading_score:int,
                writing_score:int):
        
        ## intilize the data
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score
        
        ## convert data as dataframe
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict={
                "gender":[self.gender],
                "race_ethnicity":[self.race_ethnicity],
                "parental_level_of_education":[self.parental_level_of_education],
                "lunch":[self.lunch],
                "test_preparation_course":[self.test_preparation_course],
                "reading_score":[self.reading_score],
                "writing_score":[self.writing_score],
            }
                
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(sys,e)
    