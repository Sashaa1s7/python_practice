ar = [4, 789,7,0,44,8]
print('функция sorted(arr)')
print(sorted(ar))
print(ar)
ar = sorted(ar)
print(ar)
ar = [4, 789,7,0,44,8]
print('метод sort()')
ar.sort()
print(ar)

##Функция sorted () не влияет на исходную итеративную последовательность,
##поскольку обеспечивает новый отсортированный вывод

##Метод sort () сортирует элементы массива на месте без создания копии массива.

##sort () работает только со списками и сортирует уже имеющийся список
##sorted () работает с любыми итерируемыми объектами
##и возвращает новый отсортированный список
ar = (6,6,5,0,1)
print(sorted(ar))
print(ar)
