import math
from collections import OrderedDict
from itertools import islice

EACH_CLASS_LENGTH = 50
AMOUNT_OF_PARAMETERS = 4


class KNN:

    def __init__(self, filename, k, *attrs):
        self.filename = filename
        self.k = k
        self.attrs = attrs
        self.satosa = self.specify_datasets()[0]
        self.versicolor = self.specify_datasets()[1]
        self.verginica = self.specify_datasets()[2]

    def specify_datasets(self):
        with open(self.filename, 'r') as f:
            data = f.readlines()
            iris_setosa = [[float(x) for x in sublist.split(',')[:AMOUNT_OF_PARAMETERS]] for sublist in
                           data[:EACH_CLASS_LENGTH]]
            iris_versicolor = [[float(x) for x in sublist.split(',')[:AMOUNT_OF_PARAMETERS]] for sublist in
                               data[EACH_CLASS_LENGTH:EACH_CLASS_LENGTH * 2]]
            iris_verginica = [[float(x) for x in sublist.split(',')[:AMOUNT_OF_PARAMETERS]] for sublist in
                              data[-EACH_CLASS_LENGTH:]]
        return iris_setosa, iris_versicolor, iris_verginica

    def calculate_distance(self, dataset, index):
        return math.sqrt(math.pow(dataset[index][0] - self.attrs[0], 2) +
                         math.pow(dataset[index][1] - self.attrs[1], 2) +
                         math.pow(dataset[index][2] - self.attrs[2], 2) +
                         math.pow(dataset[index][3] - self.attrs[3], 2))

    def get_all_distances(self):
        dstns_name_dict = {}
        index = 0
        for x in range(50):
            dstns_name_dict[self.calculate_distance(self.satosa, index)] = 'satosa'
            index += 1
        index = 0
        for x in range(50):
            dstns_name_dict[self.calculate_distance(self.versicolor, index)] = 'versicolor'
            index += 1
        index = 0
        for x in range(50):
            dstns_name_dict[self.calculate_distance(self.verginica, index)] = 'verginica'
            index += 1

        sordet_dict = OrderedDict(sorted(dstns_name_dict.items()))

        pre_sliced_dict = islice(sordet_dict.items(), self.k)
        sliced_dict = OrderedDict(pre_sliced_dict)

        return sliced_dict

    def make_decision(self):
        satosa_c = 0
        versicolor_c = 0
        verginica_c = 0
        for k, v in self.get_all_distances().items():
            if v == 'satosa':
                satosa_c += 1
            elif v == 'versicolor':
                versicolor_c += 1
            else:
                verginica_c += 1

        if satosa_c > versicolor_c and satosa_c > verginica_c:
            return "This flower is Iris-satosa"
        elif verginica_c > versicolor_c and verginica_c > satosa_c:
            return "This flower is Iris-verginica"
        elif versicolor_c > satosa_c and versicolor_c > verginica_c:
            return "This flower is Iris-versicolor"
        else:
            return "Unknown flower :("


knn = KNN('iris.data', 3,  6.5,3.0,5.5,1.8)
knn.get_all_distances()
print(knn.make_decision())
