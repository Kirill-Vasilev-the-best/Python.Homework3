#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках 
#записаны N целых чисел Ai. Последняя строка содержит число X

N = int(input("Введите кол-во чисел: "))
a = [int(input("Введите число: ")) for i in range(N)]
x = int(input("Введите заданое число: "))
b = [abs(a(i)-x) for i in range(len(a))]
print(a[b.index(min(b))])

