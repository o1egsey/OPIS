"""
    this module provides functionality for calculate_distance, get neighbors, optimize radius and delta.
"""
import math
from prettytable import PrettyTable

from learning import RecognClass
# from proba import classes


class IEIT:

    def __init__(self, etalons):
        self.etalons = etalons

    # @staticmethod
    # def calculate_distance(etalon_1, etalon_2):
    #     distance = 0
    #
    #     for x, y in zip(etalon_1, etalon_2):
    #         if x != y:
    #             distance += 1
    #
    #     return distance

    def calculate_distance(self):
        distances = []
        distance = 0
        for x, y in zip(self.etalons[0], self.etalons[1]):
            if x != y:
                distance += 1

        distances.append(distance)
        distance = 0
        for x, y in zip(self.etalons[0], self.etalons[2]):
            if x != y:
                distance += 1
        distances.append(distance)
        distance = 0
        for x, y in zip(self.etalons[1], self.etalons[2]):
            if x != y:
                distance += 1
        distances.append(distance)

        return distances

    def get_neighbor(self):
        pass


forest_class = RecognClass('images/forest.png')
field_class = RecognClass('images/field.png')
road_class = RecognClass('images/road.png')

classes = [forest_class, field_class, road_class]
for clas in classes:
    clas.image_to_matrix()
    clas.get_avg_vector()
    clas.get_limits()
    clas.matrix_to_binary()
    clas.get_etalon_vector()

etalons = [forest_class.etalon_vector, field_class.etalon_vector, road_class.etalon_vector]

ieit = IEIT(etalons)
print(ieit.calculate_distance())

    # def optimize_radius(self):
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
    #             if IEIT.calculate_distance(base_etalon, get_vector(base_matrix, i)) <= radius:
    #                 k1 += 1
    #             if IEIT.calculate_distance(base_etalon, get_vector(neighbor_matrix, i)) <= radius:
    #                 k3 += 1
    #
    #         k4 = 50 - k3
    #         k2 = 50 - k1
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
    #
    #     perfect_radius = max(true_area_radiuses, key=true_area_radiuses.get)
    #     # print(perfect_radius)
    #
    #     return perfect_radius

    # def optimize_delta(self):
    #     pass

