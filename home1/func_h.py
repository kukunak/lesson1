#Создайте функцию get_summ(one, two, delimiter='&') которая принимает 
# два парамтера, приводит их к строке и отдает объединеными 
# через разделитель delimteter
#Вызовите функцию, пердав в нее два аргумента "Learn" и "python", 
# положите результат в переменную и выведите ее значение на экран
#Сделайте так, чтобы результирующая строка выводилась заглавными буквами

def get_summ (one, two, delimiter='&'):
    one = str (one)
    two = str (two)
    return (f'{one}{delimiter}{two}')

p = get_summ ('learn', 'python')
print (p)
a = p.upper()
print(a)







 