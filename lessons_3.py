
a = True
b = False

 # == сравнение
x = 10
y = 5
# z = x == y

# != означает не равно
# z = x != y

# z = x > y
# z = x < y

# z = x <= y

# print('Z_result is ---',z)

age = 32
weight = 97
salary = 1000

# result = age == 32 and weight == 97

# result = age == 32 and weight == 150

# result = age == 32 or weight == 150

# or Хотя бы одно должно выполнится

# and_result = age == 32 and weight == 97 (то естсь and должео выполнить все слева направо) and всегда ищет True
# and_result = age == 34 and weight == 97 or salary == 1000 будет True , т.к. послея False все равное ищет True

result = age == 33 or weight == 150 and salary ==1005
print('Result ---', result)

# ожидается false если у нас не false, то у нас true

# not_result = not age == 35
# not age == 32 FALSE

not_result = not age == 35 or not weight == 150


print('NOT_Result ---', not_result)
not1_rel = not age == 32
print ('not_rel:', not1_rel)

if True:
    print('True--', True)
else:
    print('ELSE!!!!')


if False:
    print('True--', True)
else:
    print('ELSE!!!!')

if age == 32:
    print('True_age--', True)
else:
    print('AGE !!!!')

if age == 36:
    print('Value1--', True)
elif weight == 65:
    print('Weight==97----', True)
elif weight > 93:
    print('weight >93----', True)
else:
    print('Values3 !!!!')