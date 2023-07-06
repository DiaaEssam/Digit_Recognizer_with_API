from flask import Flask,request
import pandas as pd
import tensorflow as tf
from flasgger import Swagger
from PIL import Image
import numpy as np
import os

app=Flask(__name__) # it's a common step to start with this
Swagger(app) # pass the App to Swagger

current_directory = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(current_directory, "model")

classifier=tf.keras.models.load_model(model_path)

@app.route('/') # must be written to define the root page or main page to display
# this will display a web page having welcome all in it
def welcome():
    return "Welcome All"

# a page for predicting one sample, can be used through Postman
@app.route('/predict',methods=["POST"]) # by default it's GET method because we will pass our features as parameters
def predict_A_sample():
    """
    Let's see what is the digit
    ---
    parameters:
        
        - name: image
          in: formData
          type: file
          required: true

    responses:
        200:
            description: The output value

    """
    image=request.files.get("image")

    image = Image.open(image)
    image = image.convert('L')
    image = np.array(image.resize((28, 28)))
    image = image.astype('float32')
    image = image / 255.
    image = image.reshape((1, 28, 28,1))

    prediction=np.argmax(tf.nn.softmax(classifier.predict(image)[0]))
    return "The digit is: " + str(prediction)

# a page for predicting csv file, can be used through Postman
@app.route('/predict_file',methods=["POST"])
def predict_A_File():

    """
    Let's see what is the digit
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true
    
    responses:
        200:
            description: The output values
    """
    df_test=pd.read_csv(request.files.get("file")) # must be done through Postman
    test_data=np.array(df_test)
    test_data=test_data.reshape(test_data.shape[0],28,28,1)
    prediction=classifier.predict(test_data)
    return "The digits are: " + str(list(np.argmax(prediction,axis=1)))



if __name__=='__main__':
    app.run()
