from learning import RecognClass
from IEIT import IEIT
from get_rgb_pixels import optimize_radius

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
#
# forest_field_distance = IEIT.calculate_distance(forest_class.etalon_vector, field_class.etalon_vector)
# forest_road_distance = IEIT.calculate_distance(forest_class.etalon_vector, road_class.etalon_vector)
# road_field_distance = IEIT.calculate_distance(road_class.etalon_vector, field_class.etalon_vector)
#
# print(forest_field_distance)
# print(forest_road_distance)
# print(road_field_distance)
#
# # pairs : forest - road, road-field
#
# forest_perfect_radius = optimize_radius(forest_class.binary_matrix, road_class.binary_matrix, forest_class.etalon_vector)
# field_perfect_radius = optimize_radius(field_class.binary_matrix, road_class.binary_matrix, field_class.etalon_vector)
# road_perfect_radius = optimize_radius(road_class.binary_matrix, field_class.binary_matrix, road_class.etalon_vector)
#
# forest_class.perfect_radius = forest_perfect_radius
# field_class.perfect_radius = field_perfect_radius
# road_class.perfect_radius = road_perfect_radius
#
# print(f"Forest radius: {forest_class.perfect_radius}")
# print(f"Field radius: {field_class.perfect_radius}")
# print(f"Road radius: {road_class.perfect_radius}")
#
# max_delta = 50
#
# for clas in classes:
#     # clas.image_to_matrix()
#     for x in range(max_delta):
#         clas.delta = x
#         clas.get_avg_vector()
#         clas.get_limits()
#         clas.matrix_to_binary()
#         clas.get_etalon_vector()
