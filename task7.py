#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

a,b,c = int(input()),int(input()),int(input())
ac = abs(a - c)
bc = abs(b - c)
summ = ac + bc
print(f'AC = {ac}\n'
      f'BC = {bc}\n'
      f'Сумма AC и BC = {summ}')