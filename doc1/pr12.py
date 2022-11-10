numbers = [2, 5, 7, 7, 8, 4, 1, 6] 
odd = []
even = [] 
for number in numbers: 
    if number % 2 == 0: 
        even.append(number) 
    else: 
        odd.append(number)
##ну типв должна в один список записать четные в другие нечет. 
##odd = even =[] ну тут видно что один массив присвоили другому отсюда и ошибка

##print(odd)
##print(even)
