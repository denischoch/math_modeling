n = int(input('Введите n (число элементов):'))
d = int(input('Введите d (разность):') or -2)
a = int(input('Первый элемент'))
  
print(
    (2 * a + d * (n - 1))/2 * n,
    list(range(a, a + d * (n - 1) + d, d))
)