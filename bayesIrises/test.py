from bayes import Bayes

b = Bayes('iris.data', 5.0,3.4,1.6,0.4)  # Iris satosa
print(b)
b2 = Bayes('iris.data', 6.1,2.9,4.7,1.4)  # Iris versicolor
print(b2)
b3 = Bayes('iris.data', 7.4,2.8,6.1,1.9)  # Iris verginica
print(b3)
# print(b.get_probability('satosa', 5.1, 3.5, 1.4, 0.2))
# print(b.get_probability('versicolor', 5.1, 3.5, 1.4, 0.2))
# print(b.get_probability('verginica', 5.1, 3.5, 1.4, 0.2))
# print(b.get_mean_values(b.iris_versicolor))
