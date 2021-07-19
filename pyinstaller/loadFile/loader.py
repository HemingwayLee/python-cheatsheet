
import numpy as np
from tensorflow.keras.models import load_model

def foo():
    model = load_model('2021-07-07-02-28-19.h5')
    model.summary()

