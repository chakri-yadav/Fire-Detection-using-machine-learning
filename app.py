import os
import numpy as np
import pickle
from flask import Flask, render_template, request

# Create an instance of the Flask class
app = Flask(__name)

# Define the routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index', methods=['POST'])
def index():
    return render_template('index.html')

# Load the machine learning model
def load_model():
    return pickle.load(open("model/heart_model.pkl", "rb"))

# Prediction function
def value_predictor(to_predict_list, model):
    to_predict = np.array(to_predict_list).reshape(1, 13)
    result = model.predict(to_predict)
    return result[0]

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = [int(value) for value in request.form.values()]
        model = load_model()
        result = value_predictor(to_predict_list, model)
        
        if int(result) == 1:
            prediction = 'ABNORMAL'
        else:
            prediction = 'NORMAL'

        # Clear Keras session to avoid memory leaks
        from keras import backend as K
        K.clear_session()
            
        return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
