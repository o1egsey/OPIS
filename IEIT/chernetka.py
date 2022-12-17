# forest_pixel_values = numpy.array(list(forest.getdata()))
# forest_pixel_values = list(forest.getdata())
# sand_pixel_values = numpy.array(list(sand.getdata()))
# sand_pixel_values = list(sand.getdata())
# water_pixel_values = list(water.getdata())
# water_pixel_values = numpy.array(list(water.getdata()))
#
# forest_pixels = []
# sublist = []
#
# for x in forest_pixel_values:
#     if len(sublist) < 50:
#         sublist.append(x)
#     else:
#         forest_pixels.append(sublist)
#         sublist = []


# print(sum(forest_pixel_values[:50]))
# print(forest_pixels)
# print(sand_pixel_values)
# print(water_pixel_values)

# forest_avg_pixel = list(numpy.mean(forest_pixels, axis=0))
# sand_avg_pixel = numpy.mean(sand_pixel_values, axis=0)
# water_avg_pixel = numpy.mean(water_pixel_values, axis=0)
#
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


def get_avg(matrix):
    return list(numpy.mean(matrix, axis=0))

forest_pixels = []
sublist = []

for x in forest_pixel_values:
    if len(sublist) < 50:
        sublist.append(x)
    else:
        forest_pixels.append(sublist)
        sublist = []