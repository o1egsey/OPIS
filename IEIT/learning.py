from PIL import Image
import numpy
import math
from prettytable import PrettyTable

from IEIT import IEIT


class RecognClass:

    def __init__(self, filename):
        self.filename = filename
        self.delta = 20
        self.size = 50
        self.matrix = []
        self.binary_matrix = []
        self.avg_vector = []
        self.higher_limit = []
        self.lower_limit = []
        self.etalon_vector = []
        self.perfect_radius = 0
        self.neighbor_id = 0
        self.neighbor = 0

    def image_to_matrix(self):
        """Convert image to matrix with values of pixel RGBs"""
        image = Image.open(self.filename).convert("L")
        alist = list(image.getdata())
        length = len(alist)
        self.matrix = [alist[i * length // self.size: (i + 1) * length // self.size] for i in range(self.size)]
        return [alist[i * length // self.size: (i + 1) * length // self.size] for i in range(self.size)]

    def get_avg_vector(self):
        self.avg_vector = list(numpy.mean(self.matrix, axis=0))
        return list(numpy.mean(self.matrix, axis=0))

    def get_limits(self):
        high_limit = []
        low_limit = []
        index = 0
        for pixel in self.avg_vector:
            high_limit.append(self.avg_vector[index] + self.delta)
            low_limit.append(self.avg_vector[index] - self.delta)
            index += 1

        self.higher_limit = high_limit
        self.lower_limit = low_limit
        return high_limit, low_limit

    def matrix_to_binary(self):
        binary_matrix = []

        for i in self.matrix:
            row = []
            for j in i:
                if self.lower_limit[0] <= j <= self.higher_limit[0]:
                    row.append(1)
                else:
                    row.append(0)
            binary_matrix.append(row)

        self.binary_matrix = binary_matrix
        return binary_matrix

    def get_etalon_vector(self):
        counter_0 = [0] * 50
        counter_1 = [0] * 50
        etalon = []

        for row in self.binary_matrix:
            index = 0
            for num in row:
                if num == 0:
                    counter_0[index] += 1
                else:
                    counter_1[index] += 1
                index += 1
        for i, j in zip(counter_0, counter_1):
            if i > j:
                etalon.append(0)
            else:
                etalon.append(1)

        self.etalon_vector = etalon
        return etalon

    def get_vector(self, row_id):
        """This function returns one row from binary matrix"""
        return self.binary_matrix[row_id]

    # def optimize_radius(self, neighbor):
    #     """
    #         Надходять два класи: базовий та сусід.
    #         Рахуємо склільки реалізацій ближче до центру ніж радіус. Тобто порівнюємо спочатку в своєму класі з
    #         еталоном(центром), а потім еталон з вектором сусіда
    #     """
    #     radius = 0
    #     radius_table = PrettyTable(['Radius', 'Working Area', 'KFE'])
    #
    #     radius_dict = {}
    #
    #     for x in range(51):
    #         k1 = 0
    #         k3 = 0
    #
    #         for i in range(50):
    #             if IEIT.calculate_distance(self.etalon_vector, self.get_vector(i)) <= radius:
    #                 k1 += 1
    #             if IEIT.calculate_distance(self.etalon_vector, neighbor.get_vector(i)) <= radius:
    #                 k3 += 1
    #
    #         # k4 = 50 - k3
    #         # k2 = 50 - k1
    #
    #         t_d1 = k1 / 50
    #         t_betta = k3 / 50
    #         d1_b = t_d1 - t_betta
    #
    #         kfe = d1_b * math.log(1.0 + d1_b + 0.1) / (1.0 - d1_b + 0.1) / math.log(2.0)
    #
    #         if t_d1 >= 0.5 > t_betta:
    #             radius_table.add_row([radius, 'True', kfe])
    #             radius_dict[radius] = [True, kfe]
    #         else:
    #             radius_table.add_row([radius, 'False', kfe])
    #             radius_dict[radius] = [False, kfe]
    #
    #         radius += 1
    #
    #     true_area_radiuses = {}
    #     for key, value in radius_dict.items():
    #         if value[0] is True:
    #             true_area_radiuses[key] = value[1]
    #     # print(true_area_radiuses)
    #     # print(radius_dict)
    #     perfect_radius = max(true_area_radiuses, key=true_area_radiuses.get, default=0)
    #     self.perfect_radius = perfect_radius
    #     # print(perfect_radius)
    #     # print(perfect_radius)
    #
    #     return perfect_radius


