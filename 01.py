# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))
print('Print dictionary in ascendent values' , sorted_x)
sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse = True)
print('Print dictionary in descending values' , sorted_x)
