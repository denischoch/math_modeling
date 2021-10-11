a = int(input('Введите делимое'))
b = int(input('Введите делитель'))
if b == 0:
  print ('Человек')
elif a % b == 0:
  print(a/b, 'Остатка нет:')
elif a % b != 0:
  print(a/b, 'Остаток есть:', a%b)