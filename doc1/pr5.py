k = int(1)
name = 'name'
def polite_input(question):
    global k
    global name
    if k==1:
        name = input('Как вас зовут?\n')
        k=k+1
        
    if question == 'укажите возраст':
        print(name,', укажите возраст')
        age = input()
        return age
    elif question =='укажите номер школы':
        print(name,', укажите номер школы')
        school_number = input()
        return school_number
    elif question == 'укажите полный номер класса':
        print(name,', укажите полный номер класса')
        class_num = input()
        return class_num

    



age1 = polite_input('укажите возраст')
school_number2 = polite_input('укажите номер школы')
class_num3 = polite_input('укажите полный номер класса')

##Формат вывода
##Как вас зовут?
##(пользовательский ввод) Пётр
##Пётр, укажите возраст
##(пользовательский ввод) 16
##Пётр, укажите номер школы
##(пользовательский ввод) 1
##Пётр, укажите полный номер класса
##(пользовательский ввод) 9Б
