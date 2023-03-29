import pickle
from PIL import Image
import PIL.ImageOps 
import numpy as np
from pathlib import Path

directory = Path(__file__).resolve().parent

def recog_digit(pic_name):
    with open(directory/"model.pickle", 'rb') as f:
        clf_load = pickle.load(f)
    image = Image.open(directory/"../static/uploaded/"/pic_name).resize((28,28))
    inverted_image = PIL.ImageOps.invert(image.convert('RGB'))
    np_img = np.array(inverted_image)[:,:,0]
    data = np_img.reshape((1,-1))
    return clf_load.predict(data)
