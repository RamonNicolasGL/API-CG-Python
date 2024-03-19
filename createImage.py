import numpy as np

def createImage(image_width, image_height):
    return np.zeros((image_width, image_height), dtype=np.uint8)