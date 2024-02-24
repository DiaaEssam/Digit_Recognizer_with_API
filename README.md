# Digit Recognizer Project

This project implements a digit recognizer using artificial neural networks (ANN) and convolutional neural networks (CNN). It provides two main components: an API for real-time digit prediction and a Jupyter Notebook for training and evaluating the models.

## Table of Contents
- [Files](#files)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Files

The project consists of the following files:

1. `API.py`: This file contains the code for the Flask API that serves the digit recognition model. It accepts image input and returns the predicted digit as output.

2. `digit_recognizer_using_cnn.py`: This file contains the code for training and evaluating the CNN model for digit recognition. It loads the MNIST dataset, applies one-hot encoding to the labels, and visualizes some of the data. The model is then trained and evaluated using the dataset.

3. `digit_recognizer_using_ann.py`: This file contains the code for training and evaluating the ANN model for digit recognition. It follows a similar process as the CNN model, but without the convolutional layers.

4. `ANN_from_scratch_using_OOP_.ipynb`: This Jupyter Notebook provides an implementation of an artificial neural network (ANN) from scratch using object-oriented programming (OOP) concepts. It covers the architecture of the network, forward and backward propagation, and training process.

5. `ANN_from_scratch_.ipynb`: This Jupyter Notebook provides an implementation of an artificial neural network (ANN) from scratch without using OOP concepts. It covers similar topics as the previous notebook but uses a different coding approach.

## Usage

To use the project, follow these steps:

1. Install the required dependencies by running `pip install -r requirements.txt`.

2. Train the models by running the respective training scripts (`digit_recognizer_using_cnn.py` or `digit_recognizer_using_ann.py`).

3. Once the models are trained, you can run the API by executing `API.py`. This will start the Flask server.

4. Use a tool like Postman to send POST requests to the API endpoint `/predict` with an image file containing a handwritten digit. The API will return the predicted digit as a response.

## Acknowledgements

The project is based on the MNIST dataset and utilizes the TensorFlow and Keras libraries for training and evaluating the models.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to explore the code and experiment with different models and architectures to improve the digit recognition accuracy.
