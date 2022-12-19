from PIL import Image
import numpy
import math
from prettytable import PrettyTable


class Learning:

    def __init__(self, filename):
        self.filename = filename
        self.delta = 20
        self.matrix = []

    def image_to_matrix(self, size=50):
        """Convert image to matrix with values of pixel RGBs"""
        image = Image.open(self.filename).convert("L")
        alist = list(image.getdata())
        length = len(alist)
        self.matrix = [alist[i * length // size: (i + 1) * length // size] for i in range(size)]
        return [alist[i * length // size: (i + 1) * length // size] for i in range(size)]

    def get_avg_vector(self):
        return list(numpy.mean(self.matrix, axis=0))

    def get_limits(self):
        pass

    def matrix_to_binary(self):
        pass

    def get_etalon_vector(self):
        pass

    def calculate_distance(self):
        pass

    def get_neighbor(self):
        pass

    def get_vector(self):
        pass

    def optimize_radius(self):
        pass

    def optimize_delta(self):
        pass

