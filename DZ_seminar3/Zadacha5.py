# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))

f1 = []
f2 = []
for i in range(0, n, 2):
    if i == 0:
        a = 1
        f1.append(a)
        b = -1
        f1.append(b)
    else: 
        a = a-b
        b = b-a
        f1.append(a)
        f1.append(b)
if n%2==0:
    f1.reverse()
else:
    f1.remove(f1[-1])
    f1.reverse()

for i in range(0, n+1, 2):
    if i == 0:
        a = 0
        f2.append(a)
        b = 1
        f2.append(b)
    else: 
        a = a+b
        b = b+a
        f2.append(a)
        f2.append(b)
if n%2==0:
    f2.remove(f2[-1])

f3 = f1 + f2
print(f3)




