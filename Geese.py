import numpy as np


class SnowGoose:
    def __init__(self):
        self.lower = np.array([0, 0, 0])
        self.upper = np.array([179, 30, 255])


class Sheep:
    def __init__(self):
        self.lower = np.array([0, 0, 0])
        self.upper = np.array([48, 62, 255])
