# Задача 1, ДЗ, Семинар 1
# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним

def GetNumber():
    try:
        user_input = int(input())
        return user_input
    except ValueError:
        return GetNumber()
    
print('Длина стороны a? ', end='')
a = abs(GetNumber())
print('Длина стороны b? ', end='')
b = abs(GetNumber())
print('Длина стороны c? ', end='')
c = abs(GetNumber())

if (a == b) and (a == c):
    print('Треугольник равносторонний')
elif (a + b) > c and (a + c) > b and (c + b) > a:
     if a == b or a == c or c == b:
        print('Треугольник равнобедренный')
     else:
        print('Треугольник разносторонний')
else:
    print('Треугольник не существует')