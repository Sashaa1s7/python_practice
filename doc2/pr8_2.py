matrix = [[4, 9, 2],[3, 5, 7],[8, 1, 6]]

mag = sum(matrix[0])

if all([sum(x) == mag for x in matrix]) and all([sum(x) == mag for x in list(zip(*matrix))]):
    print('YES')
else:
    print('NO')
##мы передаем матрицу в zip с помощью оператора *.
##Мы вызываем каждую строку, а затем преобразуем эту строку в новый список,
##который становится транспонированной матрицей.
