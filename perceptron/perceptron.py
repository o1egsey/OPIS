import math
import random
LEARNING_RATE = 0.1
MAX_ITER = 100
NUM_INST = 100
theta = 0

with open('iris.data', 'r') as f:
    data = f.readlines()
    satosa = [[float(x) for x in sublist.split(',')[:4]] for sublist in data[:50]]
    versicolor = [[float(x) for x in sublist.split(',')[:4]] for sublist in data[50:100]]
    dataset = [[float(x) for x in sublist.split(',')[:4]] for sublist in data]
    sep_l = []
    sep_w = []
    pet_l = []
    pet_w = []
    outputs = []

    index = 0
    for x in dataset:
        sep_l.append(float(x[0]))
        sep_w.append(float(x[1]))
        pet_l.append(float(x[2]))
        pet_w.append(float(x[3]))
        if index <= 49:
            outputs.append(1)
        else:
            outputs.append(0)
        index += 1

    # print(dataset)

localError = 0
# globalError = 0

# seed(1)
weights = []
for x in range(5):
    weights.append(random.random())
# weights.append(random())
# weights.append(random())
# weights.append(random())
# weights.append(random())  # bias


print(weights)


def calculate_output(theta, weights, sep_l, sep_w, pet_l, pet_w):
    # print(weights[0], weights[1], sep_l, sep_w, pet_l, pet_w)
    summ = sep_l * weights[0] + sep_w * weights[1] + pet_l * weights[2] + pet_w * weights[3] + weights[4]
    if summ >= theta:
        return 1
    else:
        return 0


iteration = 0
while True:
    iteration += 1
    globalError = 0

    index = 0
    for x in range(100):
        output = calculate_output(theta, weights, sep_l[index], sep_w[index], pet_l[index], pet_w[index])
        localError = outputs[index] - output

        weights[0] += LEARNING_RATE * localError * sep_l[index]
        weights[1] += LEARNING_RATE * localError * sep_w[index]
        weights[2] += LEARNING_RATE * localError * pet_l[index]
        weights[3] += LEARNING_RATE * localError * pet_w[index]
        weights[4] += LEARNING_RATE * localError

        globalError += (localError * localError)

        index += 1

    print(f"Iteration: {iteration}  RMSE: {math.sqrt(globalError/NUM_INST)}")

    if globalError == 0 or iteration > MAX_ITER:
        break

print('***********')
print('Decision boundary equation:')
print(f"{weights[0]}*sep_l + {weights[1]} * sep_w + {weights[2]} * pet_l + {weights[3]} * pet_w + {weights[4]} = 0")

for x in range(5):
    sep_l1 = random.randrange(4, 7)
    sep_w1 = random.randrange(2, 5)
    pet_l1 = random.randrange(1, 5)
    pet_w1 = random.randrange(0, 2)

    output = calculate_output(theta, weights, sep_l1, sep_w1, pet_l1, pet_w1)
    print('Random Iris:')
    print(f"sep_l = {sep_l1}, sep_w = {sep_w1}, pet_l = {pet_l1}, pet_w = {pet_w1}")
    print(f"Class = {output}")