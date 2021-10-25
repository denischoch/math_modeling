
a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
 
if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
elif a != b and a != c and b != c:
    print("Разносторонний")
elif a == b == c:
    print("Равносторонний")
else:
    print("Равнобедренный")