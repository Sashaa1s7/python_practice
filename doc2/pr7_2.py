##k = "Ехал Грека через реку.\nВидит Грека в реке рак.\nСунул в реку руку Грека.\nРак за руку Греку цап.\n"
##k = k.split()
####print(k)
######k = enumerate(k)
######for i in k:
######    print(i)
####
####for index, value in enumerate(k):
####    print(list((index, value)))
##slova = []
####kk = list(k)
##for i in range(len(k)):
##    if k[i].istitle():
##        slova.append(k[i])
####
####print(slova)
######kk = enumerate(k)
######for i in kk:
######    print(i)
##
##for i, val in enumerate(k, start=0):
##     print(f' {i} - {val}')
##
##buf = []
##for i, val in enumerate(k, start=0):
##    if val in slova and val not in buf:
##        print(f' {i} - {val}')
##        buf = buf.append(val)
import sys
 
t = "Ехал Грека через реку.\nВидит Грека в реке рак.\nСунул в реку руку Грека.\nРак за руку Греку цап.\n"
t = t.split()
#t = [elem.strip(' .,/:;!?') for elem in sys.stdin.read().split()]
word = set()
lol = []
words = sorted(filter(lambda x: x[1].istitle(), enumerate(t)), key=lambda el: el[1])
for i in words:
    if i[1] not in word:
        word.add(i[1])
        lol.append(i)
 
for x in sorted(lol, key=lambda el: el[1]):
    print(f'{x[0]} - {x[1]}')
