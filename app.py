from flask import Flask, render_template, jsonify, request, send_file
from src.exception import CustomException
from src.logger import logging as lg
import os,sys

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify("home")

@app.route("/train")
def train_route():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
    
    except Exception as e:
        raise CustomException(e,sys)