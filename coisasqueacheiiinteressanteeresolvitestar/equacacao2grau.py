a = int(input('primeiro termo da equação '))
b = int(input('segundo termo da equação '))
c = int(input('terceira termo da equação '))
delta = b**2 - 4 * a * c
x1 = (-b + delta**0.5)/(2 * a)
x2 = (-b - delta**0.5)/(2 * a)
print (f'o x1 = {x1} e o x2 = {x2}')