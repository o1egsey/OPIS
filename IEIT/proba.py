from learning import RecognClass
from IEIT import IEIT
import math
from prettytable import PrettyTable
import csv


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


ieit = IEIT(classes)
ieit.get_neighbor()
# ieit.optimize_radius()
# ieit.optimize_delta()


# print(forest_class.neighbor_id)

# for clas in classes:
#     clas.optimize_radius(classes[clas.neighbor_id])
#
#
# print(forest_class.perfect_radius)
# print(field_class.perfect_radius)
# print(road_class.perfect_radius)


# def optimize_delta(classes, max_delta=50):
#     """Func for optimization delta. It takes one class, and max delta, as param.
#         Then for every value of value it is calculating new limits, new binary matrix, etalon, neighbors and calculate
#         new area and KFE.
#     """
#     filename = 'deltas.csv'
#     fields = ['Delta', 'Working area', 'KFE']
#     with open(filename, 'w') as f:
#         csvwriter = csv.writer(f)
#
#         take_neighbor = IEIT(classes)
#         class_index = 0
#         true_delta_dict = {}
#         list_of_deltas = []
#
#         for c in classes:
#             print(f"Class #{class_index}")
#             for delta in range(1, max_delta):
#                 c.delta = delta
#                 c.get_limits()
#                 c.matrix_to_binary()
#                 c.get_etalon_vector()
#                 take_neighbor.get_neighbor()
#                 c.optimize_radius(classes[c.neighbor_id])
#
#                 radius_table = PrettyTable(['Delta', 'Working Area', 'KFE'])
#
#                 k1 = 0
#                 k3 = 0
#                 for i in range(50):
#                     if IEIT.calculate_distance(c.etalon_vector, c.get_vector(i)) <= c.perfect_radius:
#                         k1 += 1
#                     if IEIT.calculate_distance(c.etalon_vector, classes[c.neighbor_id].get_vector(i)) <= c.perfect_radius:
#                         k3 += 1
#                 t_d1 = k1 / 50
#                 t_betta = k3 / 50
#                 d1_b = t_d1 - t_betta
#                 kfe = d1_b * math.log(1.0 + d1_b + 0.1) / (1.0 - d1_b + 0.1) / math.log(2.0)
#
#                 if t_d1 >= 0.5 > t_betta:
#                     radius_table.add_row([delta, 'True', kfe])
#                     csvwriter.writerow([delta, 'True', kfe])
#                     true_delta_dict[delta] = kfe
#                 else:
#                     radius_table.add_row([delta, 'False', kfe])
#                     csvwriter.writerow([delta, 'False', kfe])
#
#                 # print(radius_table)
#             class_index += 1
#             # print(true_delta_dict)
#             # new_dict = {}
#             for k, v in true_delta_dict.items():
#                 if 1 <= k <= 8 or 17 <= k <= 22:
#                     # new_dict[k] = v
#                     list_of_deltas.append([k, v])
#                     # if k in list_of_deltas:
#                     #     list_of_deltas[k] += v
#                     # else:
#                     #     list_of_deltas.append([k, v])
#             # print(new_dict)
#             print(list_of_deltas)
#             # new_dict.clear()
#             list_of_deltas.clear()
#             true_delta_dict = {}
#         # print(list_of_deltas)


# optimal_delta = optimize_delta(classes)

# 1-8, 17-22
avg_list = [10, 8.45, ]
