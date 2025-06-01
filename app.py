from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipline.predict_pipline import CustomDate,predictpipline

app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predictedpoint",methods=['GET','POST'])
def predicted_point():
    if request.method=='GET':
        return render_template("home.html")
    
    else:
        data=CustomDate(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=request.form.get('reading_score'),
            writing_score=request.form.get('writing_score'),
        )
        
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print('before prediction')
        prediction_pipline=predictpipline()
        print('mid of prediction')
        results=prediction_pipline.prediction(pred_df)
        print('after prediction')
        return render_template('home.html',results=results[0])



if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)
    