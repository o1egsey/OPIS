import math
from statistics import mean
# from numpy import array, average
import numpy
from math import sqrt

EACH_CLASS_LENGTH = 50
AMOUNT_OF_PARAMETERS = 4


class Bayes:

    def __init__(self, filename):
        self.filename = filename

    def get_data_from_file(self):
        with open(self.filename, 'r') as f:
            data = f.readlines()
            # iris_setosa = [x.split(',')[:AMOUNT_OF_PARAMETERS] for x in data[:EACH_CLASS_LENGTH]]
            iris_setosa = [[float(x) for x in sublist.split(',')[:AMOUNT_OF_PARAMETERS]] for sublist in
                           data[:EACH_CLASS_LENGTH]]
            iris_versicolor = [[float(x) for x in sublist.split(',')[:AMOUNT_OF_PARAMETERS]] for sublist in
                               data[EACH_CLASS_LENGTH:EACH_CLASS_LENGTH * 2]]
            iris_verginica = [[float(x) for x in sublist.split(',')[:AMOUNT_OF_PARAMETERS]] for sublist in
                              data[-EACH_CLASS_LENGTH:]]

            # print(iris_setosa)
            # print(iris_versicolor)
            # print(iris_verginica)

            self.avg_satosa = [round(float(sum(col)) / len(col), 3) for col in zip(*iris_setosa)]
            self.avg_versicolor = [round(float(sum(col)) / len(col), 3) for col in zip(*iris_versicolor)]
            self.avg_verginica = [round(float(sum(col)) / len(col), 3) for col in zip(*iris_verginica)]

            print(f"Iris-satosa mean: {self.avg_satosa}")
            print(f"Iris-versicolor mean: {self.avg_versicolor}")
            print(f"Iris-verginica mean: {self.avg_verginica}")

            # print(avg_satosa)
            # print(avg_versicolor)
            # print(avg_verginica)
            # print(*map(mean, zip(*iris_setosa)))
            # print(*map(mean, zip(*iris_versicolor)))
            # print(*map(mean, zip(*iris_verginica)))

            satosa_sepal_len_el = [x[0] for x in iris_setosa]
            satosa_sepal_wid_el = [x[1] for x in iris_setosa]
            satosa_petal_len_el = [x[2] for x in iris_setosa]
            satosa_petal_wid_el = [x[3] for x in iris_setosa]
            # print(satosa_sepal_len_el)
            # print(satosa_sepal_wid_el)
            # print(satosa_petal_len_el)
            # print(satosa_petal_wid_el)

            satosa_sepal_len_el_std = numpy.std(satosa_sepal_len_el)
            satosa_sepal_wid_el_std = numpy.std(satosa_sepal_wid_el)
            satosa_petal_len_el_std = numpy.std(satosa_petal_len_el)
            satosa_petal_wid_el_std = numpy.std(satosa_petal_wid_el)

            # print(satosa_sepal_len_el_std)
            # print(satosa_sepal_wid_el_std)
            # print(satosa_petal_len_el_std)
            # print(satosa_petal_wid_el_std)

            self.satosa_stds = [satosa_sepal_len_el_std, satosa_sepal_wid_el_std, satosa_petal_len_el_std,
                                satosa_petal_wid_el_std]

    def get_probability(self, sl, sw, pl, pw):
        p_sl_satosa = (1 / (math.sqrt(2 * math.pi) * self.satosa_stds[0])) * \
                      math.exp((- math.pow(sl - self.avg_satosa[0], 2)) / (2 * math.pow(self.satosa_stds[0], 2)))
        p_sw_satosa = (1 / (math.sqrt(2 * math.pi) * self.satosa_stds[1])) * \
                      math.exp((- math.pow(sw - self.avg_satosa[1], 2)) / (2 * math.pow(self.satosa_stds[1], 2)))
        p_pl_satosa = (1 / (math.sqrt(2 * math.pi) * self.satosa_stds[2])) * \
                      math.exp((- math.pow(pl - self.avg_satosa[2], 2)) / (2 * math.pow(self.satosa_stds[2], 2)))
        p_pw_satosa = (1 / (math.sqrt(2 * math.pi) * self.satosa_stds[3])) * \
                      math.exp((- math.pow(pw - self.avg_satosa[3], 2)) / (2 * math.pow(self.satosa_stds[3], 2)))

        print(p_sl_satosa)
        print(p_sw_satosa)
        print(p_pl_satosa)
        print(p_pw_satosa)
        p = p_sl_satosa * p_pl_satosa * p_pw_satosa * p_sw_satosa

        return f"Probality of satosa: {p}"


b1 = Bayes('iris.data')
b1.get_data_from_file()
print(b1.get_probability(5.1, 3.5, 1.4, 0.2))
print(b1.get_probability(5.006, 3.418, 1.464, 0.244))
