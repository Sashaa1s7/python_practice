def pr(value): return sum(map(lambda x : x*x , filter(lambda x : x % 9 == 0, value)))

#print(pr([4, 9, 18,3]))
