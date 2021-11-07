# print('Python', 'QA')
#
# print('hello ' + 'Python ' + 'qa ')
# Конкотинация - склейка строки
# print('hello', 'Python', 'qa', sep = '====')

# name = input('Input your name:')
# print('Hello, '+ name)

# len возвращает длину строки
# sorted - сортирует по буквам
# type - возвращает тип данных
# print(len('Alina'))
# Переменная должна начинатся с БУКВА или можно ничнее подчеркивание "_" (_name)

# name = 'Ali'
# name_len = len(name)
# sorted_name = sorted(name)
# name_type = type(120)

# print('Name:', name)
# print('Len:', name_len)
# print('Sorted_name:', sorted_name)
# print('Name_type:', name_type)

# есть зарезервированные слова, которыми нельзя называть переменные
# rise, true, and,. Поискать штук 17-25.

# Если склеиваем строки, то приводим к одному типу данных.(явное приведение данных)
name = 'Aliluzu'
age = 24

res = name + str(age)
print(name, age, res)
# fl_digit фло дижит - это плавающие данные 32.56

# array = list_type
list_type = ['123', '123fd', 23, True, ['12', '6759']]
print(list_type[4][1])

# typle_type не изменяемый список
typle_type = (12, '23')

# dict_type по факту это  JSON в питоне
dict_type = {'key1': 12,
             'name1': 'Ali',
                'inner_json':{'in_1item':777,
                              'in_2item':'Alinka'}
             }
print(dict_type['inner_json']['in_2item'])

PG = 'Check pycharm with GitHub'
print (PG)

