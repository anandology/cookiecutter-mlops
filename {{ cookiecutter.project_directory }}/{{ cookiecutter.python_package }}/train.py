"""
Module to train the ML model
"""

from . import data
from . import preprocess
from . import models
from . import validate
from . import config
from sklearn.tree import DecisionTreeClassifier

def train(df):
    X = df[config.features]
    y = df[config.target]

    # TODO: replace this with the actual model that you want to build
    model = DecisionTreeClassifier()
    model.fit(X, y)

    return model

def main():
    df = data.load_data()
    validate.validate_data(df)
    df = preprocess.preprocess(df)
    model = train(df)
    models.save_model(model)
