# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
a = float(input('Primeira nota: '))
b = float(input('Segunda nota: '))
media = (a + b) / 2
if media < 5:
    print(f'Sua média foi {media:.1f}, Reprovado!')
elif 5 < media < 7:
    print(f'Sua média foi {media:.1f}, Recuperação!')
elif media >= 7:
    print(f'Sua média foi {media:.1f}, Aprovado!')
