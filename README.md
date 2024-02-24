# Project Readme: Digit Recognizer

## Overview
This project focuses on building a digit recognizer using Convolutional Neural Networks (CNN) and Artificial Neural Networks (ANN). It provides two different implementations: one using a CNN model with a Flask API, and another using an ANN model.

The project includes the following files:
- `digit_recognizer_using_cnn.py`: This file contains the code for the digit recognizer using a CNN model and Flask API. It uses TensorFlow, PIL, NumPy, and Pandas libraries for image processing, model loading, and prediction. The API provides two endpoints: `/predict` for predicting a single digit image and `/predict_file` for predicting multiple digits from a CSV file.
- `API.py`: This file contains the Flask API implementation for the digit recognizer using a CNN model. It loads the pre-trained model, accepts image inputs, preprocesses them, and returns the predicted digit.
- `ANN_from_scratch_using_OOP_.ipynb`: This Jupyter Notebook file contains the implementation of an Artificial Neural Network (ANN) from scratch using object-oriented programming (OOP) concepts. It includes the necessary libraries, loads the MNIST dataset, applies one-hot encoding for labels, and visualizes some of the data.
- `ANN_from_scratch_.ipynb`: This Jupyter Notebook file contains the implementation of an Artificial Neural Network (ANN) from scratch. It includes the necessary libraries, loads the MNIST dataset, applies one-hot encoding for labels, and visualizes some of the data.

## Usage
To use the digit recognizer models, follow the instructions below:

### CNN Model with Flask API
1. Ensure you have the required libraries installed (Flask, TensorFlow, PIL, NumPy, Pandas, flasgger).
2. Run the `API.py` file using Python.
3. Once the Flask API is running, you can access the following endpoints:
   - `/`: This endpoint displays a welcome message.
   - `/predict`: This endpoint accepts a single digit image and returns the predicted digit.
   - `/predict_file`: This endpoint accepts a CSV file containing multiple digit images and returns the predicted digits.

### ANN Model
1. Open the `ANN_from_scratch_using_OOP_.ipynb` or `ANN_from_scratch_.ipynb` file in Jupyter Notebook or any compatible environment.
2. Make sure you have the required libraries installed (NumPy, Pandas, Matplotlib, Keras, TensorFlow).
3. Run the notebook cells step by step to execute the code.
4. Follow the instructions provided in the notebook to load the MNIST dataset, preprocess the data, and train the ANN model.
5. Experiment with different parameters and configurations to improve the model's performance.

## Contributing
Contributions to this project are welcome. If you have any suggestions, improvements, or bug fixes, please create a pull request or open an issue to discuss further.

## License
The code in this project is available under the [MIT License](https://opensource.org/licenses/MIT).
