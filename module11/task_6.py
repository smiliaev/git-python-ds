print('Задача 6. Ход конём')


# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
# 
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

def get_coord(prompt):
  print(prompt)
  while True:
    try:
      x = float(input('x: '))
      y = float(input('y: '))
      if x < 0 or y < 0 or x > 0.8 or y > 0.8:
        raise ValueError
      break
    except ValueError:
      print('Введите числа в границах доски от 0 до 0.8')
  return x, y

###
knight_x, knight_y = get_coord('Введите местоположение коня:')
point_x, point_y = get_coord('Введите местоположение точки на доске:')

knight_x, knight_y = int(knight_x * 10), int(knight_y * 10)
point_x, point_y = int(point_x * 10), int(point_y * 10)

dx, dy = abs(point_x - knight_x), abs(point_y - knight_y)

print(f'Конь в клетке ({knight_x}, {knight_y}). Точка в клетке ({point_x}, {point_y})')

if dx <= 2 and dy <= 2 and dx + dy == 3:
  print('Да, конь может ходить в эту точку.')
else:
  print('Нет, конь не может ходить в эту точку.')