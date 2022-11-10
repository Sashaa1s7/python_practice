from itertools import product
 
drop = input()
mas = ['пик', 'треф', 'бубен', 'червей']
nominals = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз') 
mas.remove(drop)
for n, s in product(nominals, mas):
    print(n, s)
