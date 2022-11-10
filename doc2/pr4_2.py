##def pro(string):
##    ss=[]
##    k = 0
##    for i in range(len(string)):
##        if string[i] == ' ':
##            ss.append(i)
##
##            
##     for i in range(len(ss)):
##         for j in range(len(string)):
##             k = sentence.count('a',i0,ss[i])
##             print(k)
##         i0 = i
##         
##    print(ss)        
##
##pro('gggh hgh kk gg')
song = input()
volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
parts = song.split()
itog = list()
for item in parts:
    k = 0
    for letter in item:
        if letter in volwes:
            k += 1
    itog.append(k)
if len(set(itog)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
