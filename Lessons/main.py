import time

print("Hello, the same Python Iteration")

a = 10
b = 15
c: int = a + b
print(type(c), c)

d = 'Alina'
print(type(d), d)

e = 1.5
print(type(e), e)

y = False
print(type(y), y)

l = [a, b, c, d, e, y, 'Zheka', ['Zhe', 32, True]]
print(type(l), l)


if a < 5:
    print("a>5")
else:
    print("Else")


count = 0
while count < 10:

    time.sleep(.700)
    count += 1
    print('count = ', count)
