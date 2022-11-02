from numpy import array, average

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

array_lol = array(list_of_lists)
column_average = average(array_lol, axis=0)

# row_average = average(array_lol, axis=1)
print(column_average)
# print(row_average)  # Returns# [2. 5. 8.]# [4. 5. 6.]
