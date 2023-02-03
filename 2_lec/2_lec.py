# # 1 вариант Запись
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors)  # разделителей не будет
# data.close

# 2 вариант Запись
# with open ('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
    
# # Чтение   
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# # Функции
# import sys
# sys.path.insert (0, "E:\GeekBrains\Developer\7. Common block\Hello Python\New\Lec\Python_Lec_Kam\1_lec")

# import hello as h
# print(h.f(1))

# def new_string(symbol, count = 3):
#     return symbol * count

# print (new_string('!', 5))
# print (new_string('!'))  # Будет ошибка, но можно в функции задавать значения по умолчанию => "count = 3"
# print (new_string(4))

def concatenation (*params):   # данная функция только для строк
    res: str = ''
    for item in params:
        res += item
    return res
print (concatenation('a', 's', 'd', 'w'))
print (concatenation('a', '1', 'd', '2'))

 