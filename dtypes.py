a = 3
b = 0.1
c = a != b 
print (c) 
a = 'привет'
b = 'мир'
x = 2
c = a + ' ' + b 
print (c) 
d = '{} {} {}!' .format(a,b,x)
print (d) 
user = 'Yan'
b = 'привет {name}'.format(name = user)
print (b) 
h = f"привет {user}"
print (h) 
print (len(h))  
a = 'привет'.upper()
print(a)
b = 'ПриВЕт'.lower()
print (b)
j = 'python'.capitalize() # с заглавной буквы
print (j)

a = '     при ве тмир  !  '
b = a.strip()  #убирает пробелы в начале и вконце
print (a)
print (b)

a = 'прив3т т3б3'
b = a.replace ('3', 'e')
print (a)
print (b)

a = 'привет приветЫ'.lower().replace('ы', '').capitalize()
print (a) # если не привести текст к нижнему регистру, то ы должна быть заглавной в команде replace

a = "learn.python.ru"
print (a.split('.')) # разбивает строку в список
b = a.split('.')
print (len(b))

a = None #проверить можем с помощью is
b = 0 
print (a is None)
print (b is None)

a = 2
b = 2.1
c = '2.40'
d = True
e = None
print (type(a), type(b), type(c), type(d), type(e))

name = input ('введи имя: ')
print (f'Привет, {name}')
age = input ('введи свой год рожденя: ')
age = 2019- int(age)
print (f'тебе {age} лет')

print(bool('привет'), 'привет')
print(bool(1), '1')
print(bool(None), 'None')
print(bool(), 'пустая строка')
print(bool(0), '0')
print(bool(-1), '-1')