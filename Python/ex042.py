# Refaça o EXERCÍCIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Da para formar um triângulo!')
    if a == b == c:
        print('O triângulo é EQUILÁTERO')
    elif a != b != c:
        print('O triângulo é ESCALENO')
    else:
        print('O triângulo é ISÓSCELES')
else:
    print('Não da para formar um triângulo!')
