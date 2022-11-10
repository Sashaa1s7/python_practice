def print_operation_table(operation, num_rows=9, num_columns=9):
    for i in range(1, num_rows + 1):
         answer = []
         for j in range(1, num_columns + 1):
             answer.append(str(operation(i, j)))
         print(''.join(f'{e:<4}' for e in answer))

##Метод join в Python отвечает за объединение списка строк
##с помощью определенного указателя. Часто это используется
##при конвертации списка в строку. Например,
##так можно конвертировать список букв алфавита в разделенную запятыми строку
##для сохранения.
print_operation_table(lambda x, y: x * y)
print('_____________')
print_operation_table(lambda x, y: x * y, 5)
