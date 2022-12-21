"""
    this module provides functionality for calculate_distance, get neighbors, optimize radius and delta.
"""
import math
from prettytable import PrettyTable
import csv


class IEIT:

    def __init__(self, classes: list):
        self.classes = classes

    @staticmethod
    def calculate_distance(vector_1, vector_2):
        distance = 0

        for x, y in zip(vector_1, vector_2):
            if x != y:
                distance += 1

        return distance

    def get_neighbor(self):
        """
            This method find neighbor for all classes.
        """
        for cl in self.classes:
            cl_distances_dict = {}
            cc = self.classes.copy()
            if cc.index(cl) != 0:
                cc.remove(cl)
                cc.insert(0, cl)

            friend_id = 1
            for x in range(len(self.classes)-1):
                cl_distances_dict[cc[friend_id]] = IEIT.calculate_distance(cl.etalon_vector, cc[friend_id].etalon_vector)
                friend_id += 1

            print(f"Neighbor of class {cl} is : {min(cl_distances_dict, key=cl_distances_dict.get)}")

            print(cl_distances_dict)


        # class0_distances = {}
        # class1_distances = {}
        # class2_distances = {}
        #
        # distance = 0
        # for x, y in zip(self.classes[0].etalon_vector, self.classes[1].etalon_vector):
        #     if x != y:
        #         distance += 1
        #
        # class0_distances[1] = distance
        # class1_distances[0] = distance
        #
        # distance = 0
        # for x, y in zip(self.classes[0].etalon_vector, self.classes[2].etalon_vector):
        #     if x != y:
        #         distance += 1
        # class2_distances[0] = distance
        # class0_distances[2] = distance
        #
        # distance = 0
        # for x, y in zip(self.classes[1].etalon_vector, self.classes[2].etalon_vector):
        #     if x != y:
        #         distance += 1
        # class2_distances[1] = distance
        # class1_distances[2] = distance
        #
        # self.classes[0].neighbor_id = min(class0_distances, key=class0_distances.get)
        # self.classes[0].neighbor = self.classes[min(class0_distances, key=class0_distances.get)]
        # self.classes[1].neighbor_id = min(class1_distances, key=class1_distances.get)
        # self.classes[1].neighbor = self.classes[min(class1_distances, key=class1_distances.get)]
        # self.classes[2].neighbor_id = min(class2_distances, key=class2_distances.get)
        # self.classes[2].neighbor = self.classes[min(class2_distances, key=class2_distances.get)]
        #
        # return class0_distances, class1_distances, class2_distances

    def optimize_radius(self):
        """
            Надходять два класи: базовий та сусід.
            Рахуємо склільки реалізацій ближче до центру ніж радіус. Тобто порівнюємо спочатку в своєму класі з
            еталоном(центром), а потім еталон з вектором сусіда
        """
        for cl in self.classes:
            radius = 0
            radius_dict = {}

            for x in range(51):
                k1 = 0
                k3 = 0
                for i in range(50):
                    if IEIT.calculate_distance(cl.etalon_vector, cl.get_vector(i)) <= radius:
                        k1 += 1
                    if IEIT.calculate_distance(cl.etalon_vector, cl.neighbor.get_vector(i)) <= radius:
                        k3 += 1

                t_d1 = k1 / 50
                t_betta = k3 / 50
                d1_b = t_d1 - t_betta
                kfe = d1_b * math.log(1.0 + d1_b + 0.1) / (1.0 - d1_b + 0.1) / math.log(2.0)

                if t_d1 >= 0.5 > t_betta:
                    radius_dict[radius] = [True, kfe]
                else:
                    radius_dict[radius] = [False, kfe]

                radius += 1
            true_area_radiuses = {}
            for key, value in radius_dict.items():
                if value[0] is True:
                    true_area_radiuses[key] = value[1]

            perfect_radius = max(true_area_radiuses, key=true_area_radiuses.get, default=0)
            cl.perfect_radius = perfect_radius

    def optimize_delta(self, max_delta=50):
        """Method for optimization delta. It takes max delta, as param.
            Then for every value of delta it is calculating new limits, new binary matrix, etalon, neighbors, perfect
            radius and then calculate KFE for this delta.

            To-do: needed to implement algorithm for getting perfect delta automatically.
        """
        filename = 'deltas.csv'
        fields = ['Delta', 'Working area', 'KFE']
        with open(filename, 'w') as f:
            csvwriter = csv.writer(f)

            # take_neighbor = IEIT(classes)
            class_index = 0
            true_delta_dict = {}
            list_of_deltas = []

            for cl in self.classes:
                print(f"Class #{class_index}")
                for delta in range(1, max_delta):
                    cl.delta = delta
                    cl.get_limits()
                    cl.matrix_to_binary()
                    cl.get_etalon_vector()
                    IEIT.get_neighbor(self)
                    IEIT.optimize_radius(self)
                    print(cl.perfect_radius)
                    # cl.optimize_radius(self.classes[c.neighbor_id])

                    delta_table = PrettyTable(['Delta', 'Working Area', 'KFE'])

                    k1 = 0
                    k3 = 0
                    for i in range(cl.size):
                        if IEIT.calculate_distance(cl.etalon_vector, cl.get_vector(i)) <= cl.perfect_radius:
                            k1 += 1
                        if IEIT.calculate_distance(cl.etalon_vector, cl.neighbor.get_vector(i)) <= cl.perfect_radius:
                            k3 += 1
                    t_d1 = k1 / 50
                    t_betta = k3 / 50
                    d1_b = t_d1 - t_betta
                    kfe = d1_b * math.log(1.0 + d1_b + 0.1) / (1.0 - d1_b + 0.1) / math.log(2.0)

                    if t_d1 >= 0.5 > t_betta:
                        delta_table.add_row([delta, 'True', kfe])
                        csvwriter.writerow([delta, 'True', kfe])
                        true_delta_dict[delta] = kfe
                    else:
                        delta_table.add_row([delta, 'False', kfe])
                        csvwriter.writerow([delta, 'False', kfe])

                    # print(radius_table)
                class_index += 1
                print(true_delta_dict)
                # new_dict = {}
                # for k, v in true_delta_dict.items():
                #     if 1 <= k <= 8 or 17 <= k <= 22:
                #         # new_dict[k] = v
                #         list_of_deltas.append([k, v])
                #         # if k in list_of_deltas:
                #         #     list_of_deltas[k] += v
                #         # else:
                #         #     list_of_deltas.append([k, v])
                # # print(new_dict)
                # print(list_of_deltas)
                # # new_dict.clear()
                # list_of_deltas.clear()
                true_delta_dict = {}
            # print(list_of_deltas)
