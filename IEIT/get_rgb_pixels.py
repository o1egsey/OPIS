from PIL import Image
import numpy
import math
import pandas
from prettytable import PrettyTable
import logging

DELTA = 20

forest = Image.open('images/forest.png').convert("L")
sand = Image.open('images/field.png').convert("L")
water = Image.open('images/road.png').convert("L")

# forest_pixel_values = list(forest.getdata())
# sand_pixel_values = list(sand.getdata())
# water_pixel_values = list(water.getdata())


# def image_to_matrix(image):
#     """ func for converting image to matrix of RGBs """
#     matrix = []
#     sublist = []
#
#     for x in list(image.getdata()):
#         if len(sublist) < 10:
#             sublist.append(x)
#         elif len(sublist) == 10:
#             matrix.append(sublist)
#             sublist = []
#             sublist.append(x)
#
#     return matrix


def split_list(image, wanted_parts=50):
    alist = list(image.getdata())
    length = len(alist)
    return [alist[i*length // wanted_parts: (i+1)*length // wanted_parts] for i in range(wanted_parts)]


# forest_matrix = image_to_matrix(forest)
forest_matrix = split_list(forest)
sand_matrix = split_list(sand)
water_matrix = split_list(water)

# print(len(forest.getdata()))
# print(list(forest.getdata()))
# print(forest_matrix)
# print(forest_matrix2)
# print(sand_matrix)
# print(water_matrix)

forest_avg_pixel = list(numpy.mean(forest_matrix, axis=0))
sand_avg_pixel = list(numpy.mean(sand_matrix, axis=0))
water_avg_pixel = list(numpy.mean(water_matrix, axis=0))
# print(f"Forest AVG: {forest_avg_pixel}")
# print(f"Sand AVG: {sand_avg_pixel}")
# print(f"Water AVG: {water_avg_pixel}")


def get_limits(pixel_avg):
    high_limit = []
    low_limit = []
    index = 0
    for pixel in pixel_avg:
        high_limit.append(pixel_avg[index] + DELTA)
        low_limit.append(pixel_avg[index] - DELTA)
        index += 1

    return high_limit, low_limit


forest_limits = get_limits(forest_avg_pixel)
# print(f"Forest HIGH limit: {forest_limits[0]} \n"
#       f"Forest LOW limit: {forest_limits[1]}")
sand_limits = get_limits(sand_avg_pixel)
# print(f"sand HIGH limit: {sand_limits[0]} \n"
#       f"sand LOW limit: {sand_limits[1]}")
water_limits = get_limits(water_avg_pixel)
# print(f"water HIGH limit: {water_limits[0]} \n"
#       f"water LOW limit: {water_limits[1]}")


def to_binary(pixels_matrix, h_limit, l_limit):
    binary_matrix = []

    for i in pixels_matrix:
        row = []

        for j in i:
            if l_limit[0] <= j <= h_limit[0]:
                row.append(1)
            else:
                row.append(0)

        binary_matrix.append(row)

    return binary_matrix


binary_forest = to_binary(forest_matrix, forest_limits[0], forest_limits[1])
# print(numpy.matrix(binary_forest))
# print(pandas.DataFrame(binary_forest))
binary_sand = to_binary(sand_matrix, sand_limits[0], sand_limits[1])
# print(binary_sand)
binary_water = to_binary(water_matrix, water_limits[0], water_limits[1])
# print(binary_water)


def get_etalon(binary_matrix):
    counter_0 = [0] * 50
    counter_1 = [0] * 50

    etalon = []

    for row in binary_matrix:
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

    # print(f"counter_0: {counter_0}")
    # print(f"counter_1: {counter_1}")

    return etalon


forest_etalon = get_etalon(binary_forest)
# print(f"Forest ETALON: {forest_etalon}")
sand_etalon = get_etalon(binary_sand)
# print(f"Sand ETALON: {sand_etalon}")
water_etalon = get_etalon(binary_water)
# print(f"Water ETALON: {water_etalon}")


def get_neighbor():
    neighbor_id = -1
    distance = -1

    pass


def calculate_distance(etalon_1: list, etalon_2: list):
    distance = 0

    for x, y in zip(etalon_1, etalon_2):
        if x != y:
            distance += 1

    return distance


forest_sand_distance = calculate_distance(forest_etalon, sand_etalon)
forest_water_distance = calculate_distance(forest_etalon, water_etalon)
water_sand_distance = calculate_distance(water_etalon, sand_etalon)
print(forest_sand_distance)
print(forest_water_distance)
print(water_sand_distance)


def get_vector(binary_matrix, row_id):
    """This function returns one row from binary matrix"""
    return binary_matrix[row_id]


def optimize_radius(base_matrix, neighbor_matrix, base_etalon):
    """
        Надходять два класи: базовий та сусід.
        Рахуємо склільки реалізацій ближче до центру ніж радіус. Тобто порівнюємо спочатку в своєму класі з
        еталоном(центром), а потім еталон з вектором сусіда
    """
    radius = 0
    radius_table = PrettyTable(['Radius', 'Working Area', 'KFE'])

    for x in range(51):
        k1 = 0
        k3 = 0

        for i in range(50):
            if calculate_distance(base_etalon, get_vector(base_matrix, i)) <= radius:
                k1 += 1
            if calculate_distance(base_etalon, get_vector(neighbor_matrix, i)) <= radius:
                k3 += 1

        k4 = 50 - k3
        k2 = 50 - k1

        t_d1 = k1 / 50
        t_betta = k3 / 50
        d1_b = t_d1 - t_betta

        kfe = d1_b * math.log(1.0 + d1_b + 0.1) / (1.0 - d1_b + 0.1) / math.log(2.0)

        # print(f"KFE: {kfe}")
        # print(f"k1 = {k1}, k3 = {k3}")
        # print(f"k1 = {k1}, k3 = {k3}")

        if t_d1 >= 0.5 > t_betta:
            # print(f"{radius} : True")
            radius_table.add_row([radius, 'True', kfe])
        else:
            # print(f"{radius} : False")
            radius_table.add_row([radius, 'False', kfe])

        radius += 1

    return radius_table


# optimization_forest = optimize_radius(binary_forest, binary_water, forest_etalon)
# print(optimization_forest)
# print('****************************')
# optimization_water = optimize_radius(binary_water, binary_forest, water_etalon)
# print(optimization_water)
# print('****************************')
# optimization_sand = optimize_radius(binary_sand, binary_water, sand_etalon)
# print(optimization_sand)

FOREST_RADIUS = 9
SAND_RADIUS = 29
WATER_RADIUS = 7


def optimize_delta(max_delta, base_matrix, neighbor_matrix, base_etalon, radius):

    delta_table = PrettyTable(['Delta', 'Working Area', 'KFE'])

    for x in range(max_delta):
        k1 = 0
        k3 = 0
        for i in range(50):
            if calculate_distance(base_etalon, get_vector(base_matrix, i)) <= radius:
                k1 += 1
            if calculate_distance(base_etalon, get_vector(neighbor_matrix, i)) <= radius:
                k3 += 1

        k4 = 50 - k3
        k2 = 50 - k1

        t_d1 = k1 / 50
        t_betta = k3 / 50
        d1_b = t_d1 - t_betta

        kfe = d1_b * math.log(1.0 + d1_b + 0.1) / (1.0 - d1_b + 0.1) / math.log(2.0)

        if t_d1 >= 0.5 > t_betta:
            delta_table.add_row([radius, 'True', kfe])
        else:
            delta_table.add_row([radius, 'False', kfe])

        print(delta_table)
        delta_table.clear()
        delta_table = PrettyTable(['Delta', 'Working Area', 'KFE'])


forest_delta = optimize_delta(50, binary_forest, binary_water, forest_etalon, FOREST_RADIUS)
print(forest_delta)

