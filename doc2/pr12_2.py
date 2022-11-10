import math
from functools import reduce
##raw = input('Введите последовательность чисел через пробел: ')
##int_array = [int(i) for i in raw.split(' ') if i.isdigit()]

mas = []
row = True

while row:
    row = input()
    if row:
        mas.append(int(row))
        
#mas = [36, 12, 144, 18]

print(reduce(lambda x, y: math.gcd(x, 1) if math.gcd(x, 1) > math.gcd(x, y) else math.gcd(x, y), mas)) 

result = []
row = True


