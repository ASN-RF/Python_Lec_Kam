# Задача 1. В файле храняться числа, нужно выбрать четные и составить список пар (число, квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]
# --------- МОЙ ВАРИАНТ-----------------
# def kvadrat (x):
#     return x**2
# data = open('D:\\GB\\Python_Lec_Kam\\3_lec\\Spisok.txt', 'r')
# Spisok = data.read().split()
# Spisok_int = []
# for i in Spisok:
#     Spisok_int.append(int(i))
# print (Spisok_int)
# Rezult = [(i, kvadrat(i)) for i in Spisok_int if i % 2 == 0]
# data.close
# print (Rezult)


# --------- ВАРИАНТ СЕРГЕЯ 1 -----------------
# path = 'D:\\GB\\Python_Lec_Kam\\3_lec\\Spisok.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print (out)

# --------- ВАРИАНТ СЕРГЕЯ 2 -----------------
# def select (f, col):
#     return [f(x) for x in col]

# def where (f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)
# ---- АНАЛОГО с MAP -----

# def where(f, col):
#     return [x for x in col if f(x)]


# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = where(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# ---- АНАЛОГО с MAP и FILTER -----
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# --------- MAP  ------

# li = [x for x in range(1, 20)]
# print (li)
# li = list(map(lambda x: x+10, li))
# print (li)

# Задача 3
# data = list (map(int, input().split()))
# print (data)

# аналог
# data = map(int, input().split())
# for e in data:
#     print (e)

# data = map(int, '1 2 3'.split())  # буз указания list, можно пройти только один раз пожтому надо добавлять list
# for e in data:
#     print (e)

# print ('--')
# for e in data:
#     print(e)


# ----- FILTER -----
# data = [x for x in range(10)]
# res = list (filter(lambda x: not x % 2, data))
# print(res)


# --------- ZIP  ------
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]   # функция zip будет выводить значения по размеру наименьшей переменной
# data = list(zip(users, ids, salary))
# print(data)

# --------- ZIP  ------
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]  
data = list(enumerate(users))
print(data)
