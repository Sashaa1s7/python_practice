value = [2, 4, 5, 6]
addition = [2,5]
value = value + addition
print(value)

value = [2, 4, 5, 6]
addition = [2,5]
value += addition
print(value)

value = [2, 4, 5, 6]
addition = [2,5]
ss = value
value = value + addition
print(ss)

value = [2, 4, 5, 6]
addition = [2,5]
ss = value
value += addition
print(ss)

##для изменяемых типов будет разный результат, а для неизменяемых одно и тоже
