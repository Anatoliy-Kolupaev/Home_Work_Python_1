# Задача № 5   
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки А')
x1, y1 = int(input("Координата по Х: ")), int(input("Координата по Y: ")),
print('Введите координаты точки B')
x2, y2 = int(input("Координата по Х: ")), int(input("Координата по Y: ")),
print(format(((x1 - x2)**2 + (y1 - y2)**2)**0.5, '.2f'))


