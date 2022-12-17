import math
import numpy


EACH_CLASS_LENGTH = 50
AMOUNT_OF_PARAMETERS = 4


class Bayes:

    def __init__(self, filename, *attrs):
        self.filename = filename
        self.attrs = attrs
        with open(self.filename, 'r') as f:
            data = f.readlines()
            self.iris_setosa = [[float(x) for x in sublist.split(',')[:AMOUNT_OF_PARAMETERS]] for sublist in
                                data[:EACH_CLASS_LENGTH]]
            self.iris_versicolor = [[float(x) for x in sublist.split(',')[:AMOUNT_OF_PARAMETERS]] for sublist in
                                    data[EACH_CLASS_LENGTH:EACH_CLASS_LENGTH * 2]]
            self.iris_verginica = [[float(x) for x in sublist.split(',')[:AMOUNT_OF_PARAMETERS]] for sublist in
                                   data[-EACH_CLASS_LENGTH:]]

    @staticmethod
    def get_mean_values(dataset):
        mean_val = [round(float(sum(col)) / len(col), 3) for col in zip(*dataset)]
        return mean_val

    @staticmethod
    def get_standard_deviation(dataset):
        index_of_elem = 0
        stds_list = []
        sublist = []
        for x in range(4):
            for slist in dataset:
                sublist.append(slist[index_of_elem])
                if len(sublist) == 50:
                    stds_list.append(numpy.std(sublist))
                    sublist.clear()
                    index_of_elem += 1
        return stds_list

    def get_probability(self, mean_val, std):

        probability_list = []
        index = 0
        for attribute in self.attrs:
            p = (1 / (math.sqrt(2 * math.pi) * std[index])) * \
                math.exp((- math.pow(attribute - mean_val[index], 2)) / (2 * math.pow(std[index], 2)))
            probability_list.append(p)
            index += 1

        probability = probability_list[0] * probability_list[1] * probability_list[2] * probability_list[3]
        return probability

    def make_decision(self):
        satosa_probability = self.get_probability(self.get_mean_values(self.iris_setosa),
                                                  self.get_standard_deviation(self.iris_setosa))
        versicolor_probability = self.get_probability(self.get_mean_values(self.iris_versicolor),
                                                      self.get_standard_deviation(self.iris_versicolor))
        verginica_probability = self.get_probability(self.get_mean_values(self.iris_verginica),
                                                     self.get_standard_deviation(self.iris_verginica))

        probabilities = {
            'Iris-satosa': satosa_probability,
            'Iris-versicolor': versicolor_probability,
            'Iris-verginica': verginica_probability,
        }

        for k, v in probabilities.items():
            if v == max(probabilities.values()):
                return k

    def __str__(self):
        return f"1) Iris Setosa: \n" \
               f"Mean values: sepal length = {self.get_mean_values(self.iris_setosa)[0]}, sepal width = " \
               f"{self.get_mean_values(self.iris_setosa)[1]}, petal length = {self.get_mean_values(self.iris_setosa)[2]}" \
               f" petal width = {self.get_mean_values(self.iris_setosa)[3]} \n" \
               f"Standard deviation: sepal length = {self.get_standard_deviation(self.iris_setosa)[0]}, sepal width = " \
               f"{self.get_standard_deviation(self.iris_setosa)[1]}, petal length = {self.get_standard_deviation(self.iris_setosa)[2]}, " \
               f"petal width = {self.get_standard_deviation(self.iris_setosa)[3]} \n" \
               f"2) Iris Versicolor: \n" \
               f"Mean values: sepal length = {self.get_mean_values(self.iris_versicolor)[0]}, sepal width = " \
               f"{self.get_mean_values(self.iris_versicolor)[1]}, petal length = {self.get_mean_values(self.iris_versicolor)[2]}" \
               f" petal width = {self.get_mean_values(self.iris_versicolor)[3]} \n" \
               f"Standard deviation: sepal length = {self.get_standard_deviation(self.iris_versicolor)[0]}, sepal width = " \
               f"{self.get_standard_deviation(self.iris_versicolor)[1]}, petal length = {self.get_standard_deviation(self.iris_versicolor)[2]}, " \
               f"petal width = {self.get_standard_deviation(self.iris_versicolor)[3]} \n" \
               f"3) Iris Verginica: \n" \
               f"Mean values: sepal length = {self.get_mean_values(self.iris_verginica)[0]}, sepal width = " \
               f"{self.get_mean_values(self.iris_verginica)[1]}, petal length = {self.get_mean_values(self.iris_verginica)[2]}" \
               f" petal width = {self.get_mean_values(self.iris_verginica)[3]} \n" \
               f"Standard deviation: sepal length = {self.get_standard_deviation(self.iris_verginica)[0]}, sepal width = " \
               f"{self.get_standard_deviation(self.iris_verginica)[1]}, petal length = {self.get_standard_deviation(self.iris_verginica)[2]}, " \
               f"petal width = {self.get_standard_deviation(self.iris_verginica)[3]} \n\n" \
               f"Probabilities: \n" \
               f"Iris Setosa : {self.get_probability(self.get_mean_values(self.iris_setosa), self.get_standard_deviation(self.iris_setosa))} \n" \
               f"Iris Versicolor : {self.get_probability(self.get_mean_values(self.iris_versicolor), self.get_standard_deviation(self.iris_versicolor))} \n" \
               f"Iris Verginica : {self.get_probability(self.get_mean_values(self.iris_verginica), self.get_standard_deviation(self.iris_verginica))} \n\n" \
               f"This flower may belong to '{self.make_decision()}' class"



