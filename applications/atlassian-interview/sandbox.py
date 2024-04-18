import heapq
import random
from functools import reduce

# x = {1,6,4}
# print(type(x))
# y = {3: "c", 4:"b"}
# print(type(y))

# print(x)
# z = list(x)
# a = list(y)
# print(z)
# print(a)
# print(list(y.items()))

# xfilter = filter(lambda x: x%2==0, x)
# l = list(set(xfilter))
# yvalues = y.values()

# arr_size = 100
# x = [round(random.randint(1,1000),3) for _ in range(arr_size)]
# # x_max_heap = list(map(lambda x: -x, x))
# x_max_heap = [-item for item in x if item > 0.5]
# # x = [1,2,3,54,8,356,6,8,5,3,47,2]
# heapq.heapify(x_max_heap)
# print(x_max_heap)

f = lambda n: 1 if n < 2 else n*f(n-1)
int_range = 10
ave_mult = f(int_range) ** (1/10)

for _ in range(20):
    x = [random.randint(1,int_range) for _ in range(100000)]
    print(reduce(lambda x, y: x*y/ave_mult, x))