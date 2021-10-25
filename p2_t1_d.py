a = int(input('Введите коэффицент a:'))
b = int(input('Введите коэффицент b:'))
c = int(input('Введите коэффицент c:'))
d = b*b-(4*a*c)
if d > 0:
  print('Два корня')
elif d < 0:
  print ('Корней нет')
else d == 0:
  print ('Один корень')

