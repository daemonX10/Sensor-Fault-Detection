from flask import Flask, render_template, jsonify, request, send_file
from src.exception import CustomException
from src.logger import logging as lg
import os,sys
from src.pipeline.train_pipeline import TrainPipeline
from src.pipeline.predict_pipeline import PredicationPipeline

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/train")
def train_route():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        
        return "Training Completed"
    except Exception as e:
        raise CustomException(e,sys)

@app.route('/upload',methods=['POST','GET'])
def upload():
    try:
        if request.method == "POST":
            predication_pipeline = PredicationPipeline(request)
            predication_file_details = predication_pipeline.runpipeline()
            
            lg.info("predication completed . Downloading Predication File .")
            return send_file(predication_file_details.predication_file_path,download_name=predication_file_details,as_attachment=True)
        else:
            return render_template('upload_file.html')
    except Exception as e:
        raise CustomException(e,sys)
    
if __name__ =="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)