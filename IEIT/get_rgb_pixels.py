from PIL import Image
import numpy
import logging

forest = Image.open('forest_10.png').convert("L")
sand = Image.open('sand_10.png').convert("L")
water = Image.open('water_10.png').convert("L")

# forest_pixel_values = list(forest.getdata())
# sand_pixel_values = list(sand.getdata())
# water_pixel_values = list(water.getdata())


def image_to_matrix(image):
    """ func for converting image to matrix of RGBs """
    matrix = []
    sublist = []

    for x in list(image.getdata()):
        if len(sublist) < 50:
            sublist.append(x)
        else:
            matrix.append(sublist)
            sublist = []

    return matrix


forest_matrix = image_to_matrix(forest)
sand_matrix = image_to_matrix(sand)
water_matrix = image_to_matrix(water)

print(forest_matrix)
print(sand_matrix)
print(water_matrix)

forest_avg_pixel = list(numpy.mean(forest_matrix, axis=0))
sand_avg_pixel = list(numpy.mean(sand_matrix, axis=0))
water_avg_pixel = list(numpy.mean(water_matrix, axis=0))
print(f"Forest AVG: {forest_avg_pixel}")
print(f"Sand AVG: {sand_avg_pixel}")
print(f"Water AVG: {water_avg_pixel}")


def get_limits(pixel_avg):
    high_limit = []
    low_limit = []
    index = 0
    for pixel in pixel_avg:
        high_limit.append(pixel_avg[index] + 20)
        low_limit.append(pixel_avg[index] - 20)
        index += 1

    return high_limit, low_limit


forest_limits = get_limits(forest_avg_pixel)
print(f"Forest HIGH limit: {forest_limits[0]} \n"
      f"Forest LOW limit: {forest_limits[1]}")
sand_limits = get_limits(sand_avg_pixel)
print(f"sand HIGH limit: {sand_limits[0]} \n"
      f"sand LOW limit: {sand_limits[1]}")
water_limits = get_limits(water_avg_pixel)
print(f"water HIGH limit: {water_limits[0]} \n"
      f"water LOW limit: {water_limits[1]}")


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
print(binary_forest)
binary_sand = to_binary(sand_matrix, sand_limits[0], sand_limits[1])
print(binary_sand)
binary_water = to_binary(water_matrix, water_limits[0], water_limits[1])
print(binary_water)


def get_etalon(binary_matrix):
    counter_0 = [0] * 10
    counter_1 = [0] * 10

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

    print(f"counter_0: {counter_0}")
    print(f"counter_1: {counter_1}")

    return etalon


forest_bin_etalon = get_etalon(binary_forest)
print(f"Forest ETALON: {forest_bin_etalon}")
sand_bin_etalon = get_etalon(binary_sand)
print(f"Sand ETALON: {sand_bin_etalon}")
water_bin_etalon = get_etalon(binary_water)
print(f"Water ETALON: {water_bin_etalon}")


def get_neighbor():
    pass