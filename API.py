from flask import Flask,request
import pandas as pd
import pickle
from flasgger import Swagger
from digit_recognizer_using_cnn import Sample
import os

app=Flask(__name__) # it's a common step to start with this
Swagger(app) # pass the App to Swagger

# unpickle the object from the pickle file
current_directory = os.path.abspath(os.path.dirname(__file__))
pickle_file_path = os.path.join(current_directory, "Classifier.pkl")

pickle_in=open(pickle_file_path,'rb') # Reading pickle file
classifier=pickle.load(pickle_in) # taking back the object from the file

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

    prediction=classifier.predict(image)
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
    prediction=classifier.predict_file(df_test)
    return "The digits are: " + str(list(prediction))



if __name__=='__main__':
    app.run()
