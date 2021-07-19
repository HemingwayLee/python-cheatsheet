
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow import keras

def convert_prediction(p):
    return p[0].index(max(p[0]))

def foo():
    model = load_model('2021-07-07-02-28-19.h5')
    model.summary()
    
    (_, _), (x_test, y_test) = keras.datasets.mnist.load_data()
    x_test = x_test.astype("float32") / 255
    x_test = np.expand_dims(x_test, -1)

    for i in range(8):
        pred = model.predict(np.array([x_test[i]]))
        print(f"prediction: {convert_prediction(pred.tolist())}")


