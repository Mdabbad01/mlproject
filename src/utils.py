
import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.exceptions import CustomException


def save_object(file_path, obj):
    """
    Saves any Python object (e.g. preprocessor, model) to the given file path using pickle.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    """
    Loads a Python object from a pickle file.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)
