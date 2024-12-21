import numpy as np
import cv2
from PIL import ImageGrab
from constants import *
from statistics import mode
import time

def get_color():
    img = ImageGrab.grab()
    imgNP = np.array(img)

    # Take 10 random pixels from the image
    height, width, _ = imgNP.shape
    random_indices = np.random.randint(0, height * width, size=NUM_SAMPLES)
    sampled_pixels = imgNP.reshape(-1, 3)[random_indices]

    # Convert the sampled pixels to float32 for k-means
    pixels = np.float32(sampled_pixels)

    # Perform k-means clustering
    n_colors = 5
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)

    # Count the pixels in each cluster and find the dominant color
    _, counts = np.unique(labels, return_counts=True)
    dominant = palette[np.argmax(counts)]

    # Print the dominant color
    return dominant