from statistics import mean
from numpy import array, average

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

            avg_satosa = [round(float(sum(col)) / len(col), 3) for col in zip(*iris_setosa)]
            avg_versicolor = [round(float(sum(col)) / len(col), 3) for col in zip(*iris_versicolor)]
            avg_verginica = [round(float(sum(col)) / len(col), 3) for col in zip(*iris_verginica)]

            print(f"Iris-satosa mean: {avg_satosa}")
            print(f"Iris-versicolor mean: {avg_versicolor}")
            print(f"Iris-verginica mean: {avg_verginica}")

            # print(avg_satosa)
            # print(avg_versicolor)
            # print(avg_verginica)
            # print(*map(mean, zip(*iris_setosa)))
            # print(*map(mean, zip(*iris_versicolor)))
            # print(*map(mean, zip(*iris_verginica)))

            satosa_sepal_len_el = [[x for x in sublist[0]] for sublist in iris_setosa]
            print(satosa_sepal_len_el)


b1 = Bayes('iris.data')
b1.get_data_from_file()
