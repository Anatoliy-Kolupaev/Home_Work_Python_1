# Задача № 3 
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x, y = float(input('Введите координату Х: ')), float(input('Введите координату Y: '))
if x > 0 and y > 0: print('Точка в 1-й четверти')
elif x < 0 and y > 0: print('Точка в 2-й четверти')
elif x < 0 and y < 0: print('Точка в 3-й четверти')
elif x > 0 and y < 0: print('Точка в 4-й четверти')
else: print("Координаты Х или Y не должны быть = 0")