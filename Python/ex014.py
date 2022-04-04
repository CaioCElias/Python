# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
celsius = float(input('Informe a temperatura em °C: '))
fahre = (celsius/5) * 9 + 32
print(f'A temperatura de {celsius}°C corresponde a {fahre:.2f}°F')
