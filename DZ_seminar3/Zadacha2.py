# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

numb = 2, 3, 4, 5, 6
sum = []
for i in range(int(len(numb)/2)):
    sum.append(numb[i]*numb[-(i+1)])
if len(numb)%2 == 0:
    print(sum)
else:
    sum.append(numb[(int(len(numb)/2))]**2)
    print(sum)