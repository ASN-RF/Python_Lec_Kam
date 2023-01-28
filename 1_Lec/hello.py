# 1 задание print ('Hello world')

# 2 задание. Type
# value = None
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))

# 3 задание. Строки Ковычки
# s = 'hello \"world"'
# s1 = "hello 'world'"
# s2 = "hello \n'world'"
# print (s)
# print (s1)
# print (s2)

# 4 задание. Логические
# f = True
# print (f)

# 5 задание. Массив он-же список
# list = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# list3= [1, 'b', 64, 'hello']
# print(list)
# print(list2)
# print(list3)

# 6 задание. Ввод и Вывод данных
# x = 3
# s = 2
# print('Введите a:')
# a = input(f'{x}+{s} = {x%s} сколько будет:')
# print('Введите b:')
# b = input()
# print(f'{x}**{s} = {x**s}')

# 7 задание. Арифметические действия и округления числа
# a = 12
# b = 5
# c = round(a/b, 2)
# print(c)

# 8 задание. Сокращенные операции
# a = 3
# a +=5 # Тоже самое что a = a + 5
# print (a)

# 9 задание. Логические операции
# a = 1 < 4  # True
# print(a)
# a = 1 < 4 and 5 < 2   # False  !!! Оба условия должны выполняться
# print(a)
# a = 1 < 4 and 5 > 2   # True
# print(a)
# a = 1 < 4 or 5 < 2   # True      !!! Хотя бы одно условие должно выполняться
# print(a)
# a = 1 < 4 or 5 > 2   # True
# print(a)
# a = 3 == 4
# print(a) # False
# a = 'qwe'
# b = 'qwe'
# print(a==b) # True
# a = [1,2,3]
# b = [1,2,3]
# print(a==b) # True

# 10 задание. Нахождение значения в списке и проверка на четность
# f = [1, 2, 3, 4]
# # print (f)
# # print (2 in f)
# is_odd = not f[0] % 2 # is_odd = f[0] % 2 == 0
# print (is_odd)

# 11 задание. if, if-else
# a) Найти максимум
# a = int(input('Введите значение: '))
# b = int(input('Введите значение: '))
# if a > b:
#     print(a)
# else:
#     print(b)
# b) if-elif

# 12 задание. if - elif
# a) Найти условие
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Маша')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print(f'Привет, {username}')

# 13 задание. While
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted*10+(original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)      # Развернули число

# 14 задание. For
# for i in 1,2,3,4,5,6:
#     print (i**2, end=', ')
# list = [1, 2, 3, 4, 5, 6]
# for i in list:
#     print(i**2, end=', ')
# r = range(5)
# for i in r:
#     print(i)
# # Эквивалент:
# for i in range(5):
#     print(i)

# 15 задание. Строки
# text = 'съешь ещё этих мягких французских булок'
# print(len(text))      #39
# print('ещё' in text)    # True
# print(text.isdigit())   # False
# print(text.islower())   # True
# print(text.replace('ещё', 'ЕЩЁ'))
# print(text.lower()) # съешь ещё этих мягких французских булок
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК



# for c in text:
#     print (c)

# 16 задание. Строки-Срезы
# text = 'съешь ещё этих мягких французских булок'
# print(text[0])  # c
# print(text[1])  # ъ
# # print(text[len(text)])  # IndexError => счет с нуля
# print(text[len(text)-1])  # к
# print(text[-5])  # 6
# print(text[:])  # print(text)
# print(text[:2])  # съ
# print(text[len(text)-2:])  # ок
# print(text[2:9])  # ешь ещё
# print(text[6:-18])  # ещё этих мягких
# print(text[0:len(text):6])  # соикакл
# print(text[::6])  # соикакл

# 16 задание. Списки: введение

# 1 вариант
# numbers = [1,2,3,4,5]
# print(numbers)    # [1, 2, 3, 4, 5]

# 2 вариант
# ran = range(1, 6)
# numbers = list(ran) # Эквивалент numbers = list(range(1, 6))
# print(numbers)            # [1, 2, 3, 4, 5]

# numbers[0]=10
# print(numbers)             # [10, 2, 3, 4, 5]

# for i in numbers:
#     i *=2
#     print(i, end=',') # 20,4,6,8,10,
# print(numbers)  # [10, 2, 3, 4, 5]

# 17 задание. Списки: дополнение
# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)   # red green blue

# for e in colors:
#     print(e*2)   # redred greengreen blueblue

# colors.append('gray')  # добавить в конец
# colors.remove('red')  # Эквивалент del colors [0] -> удалить элемент

# 18 задание. Функции
# def f(x):
#     if x ==1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# arg = 2.3
# print (f(arg))
# print (type (f(arg)))