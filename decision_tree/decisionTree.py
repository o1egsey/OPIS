

class DecisionTree:

    def __init__(self, filename, *attrs):
        self.filename = filename
        self.attrs = attrs
        self.satosa = self.specify_datasets()[0]
        self.versicolor = self.specify_datasets()[1]

    def specify_datasets(self):
        with open(self.filename, 'r') as f:
            data = f.readlines()
            iris_setosa = [[float(x) for x in sublist.split(',')[:4]] for sublist in
                           data[:50]]
            iris_versicolor = [[float(x) for x in sublist.split(',')[:4]] for sublist in
                               data[50:100]]
        return iris_setosa, iris_versicolor

    def get_min_dataset_values(self):
        min_satosa = [min(x[0] for x in self.satosa),
                      min(x[1] for x in self.satosa),
                      min(x[2] for x in self.satosa),
                      min(x[3] for x in self.satosa)]
        min_versicolor = [min(x[0] for x in self.versicolor),
                          min(x[1] for x in self.versicolor),
                          min(x[2] for x in self.versicolor),
                          min(x[3] for x in self.versicolor)]

        return min_satosa, min_versicolor

    def get_max_dataset_values(self):
        max_satosa = [max(x[0] for x in self.satosa),
                      max(x[1] for x in self.satosa),
                      max(x[2] for x in self.satosa),
                      max(x[3] for x in self.satosa)]
        max_versicolor = [max(x[0] for x in self.versicolor),
                          max(x[1] for x in self.versicolor),
                          max(x[2] for x in self.versicolor),
                          max(x[3] for x in self.versicolor)]

        return max_satosa, max_versicolor

    def count_values(self):
        satosa_counter = [0, 0, 0, 0]
        for x in self.satosa:
            if x[0] >= self.attrs[0]:
                satosa_counter[0] += 1
            if x[1] >= self.attrs[1]:
                satosa_counter[1] += 1
            if x[2] >= self.attrs[2]:
                satosa_counter[2] += 1
            if x[3] >= self.attrs[3]:
                satosa_counter[3] += 1
        irA = [x/50 for x in satosa_counter]
        print(satosa_counter)
        print(irA)

        versicolor_counter = [0, 0, 0, 0]
        for x in self.versicolor:
            if x[0] >= self.attrs[0]:
                versicolor_counter[0] += 1
            if x[1] >= self.attrs[1]:
                versicolor_counter[1] += 1
            if x[2] >= self.attrs[2]:
                versicolor_counter[2] += 1
            if x[3] >= self.attrs[3]:
                versicolor_counter[3] += 1
        irB = [x/50 for x in versicolor_counter]
        print(versicolor_counter)
        print(irB)


d1 = DecisionTree('iris.data', 6.0, 2.4, 4.7, 1.5)

print(d1.get_min_dataset_values())
print(d1.get_max_dataset_values())
# d1.count_values()