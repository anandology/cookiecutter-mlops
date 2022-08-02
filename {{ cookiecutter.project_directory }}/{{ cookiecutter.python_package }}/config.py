"""Configuraton for the project
"""
import os

# base path for the project
BASE_PATH = os.path.dirname(os.path.dirname(__file__))

# Set the random_state to a fixed value so that
# the ML pipeline is reproduceable
random_state = 0

# place to store the model
model_path = os.path.join(BASE_PATH, "models/model.pkl")

# Path to the input data for training
data_path = os.path.join(BASE_PATH, "data/data.csv")

# names of the columns to use for training
features = []

# nsme of the column to predict
target = None