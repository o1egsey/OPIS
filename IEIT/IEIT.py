"""
    this module provides functionality for calculate_distance, get neighbors, optimize radius and delta.
"""
import math
from prettytable import PrettyTable


class IEIT:

    def __init__(self, classes):
        self.classes = classes

    @staticmethod
    def calculate_distance(etalon_1, etalon_2):
        distance = 0

        for x, y in zip(etalon_1, etalon_2):
            if x != y:
                distance += 1

        return distance

    def get_neighbor(self):
        class0_distances = {}
        class1_distances = {}
        class2_distances = {}

        distance = 0
        for x, y in zip(self.classes[0].etalon_vector, self.classes[1].etalon_vector):
            if x != y:
                distance += 1

        class0_distances[1] = distance
        class1_distances[0] = distance

        distance = 0
        for x, y in zip(self.classes[0].etalon_vector, self.classes[2].etalon_vector):
            if x != y:
                distance += 1
        class2_distances[0] = distance
        class0_distances[2] = distance

        distance = 0
        for x, y in zip(self.classes[1].etalon_vector, self.classes[2].etalon_vector):
            if x != y:
                distance += 1
        class2_distances[1] = distance
        class1_distances[2] = distance

        self.classes[0].neighbor_id = min(class0_distances, key=class0_distances.get)
        self.classes[1].neighbor_id = min(class1_distances, key=class1_distances.get)
        self.classes[2].neighbor_id = min(class2_distances, key=class2_distances.get)

        return class0_distances, class1_distances, class2_distances

