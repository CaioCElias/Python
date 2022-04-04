"""
EXERCÍCIO 073: Tuplas com Times de Futebol
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
A) Os 5 primeiros.
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição está o time da Chapecoense.
"""

times = 'Goiás', 'São Paulo', 'Sport Recife', 'Grêmio', 'Botafogo', 'Flamengo', 'Fluminense', 'Corinthians', \
        'Atlético mineiro', 'Coritiba', 'Vasco da Gama', 'Fortaleza', 'Atlético Goianiense', 'Santos', \
        'Ceará', 'Athletico-PR', 'Bahia', 'Brangatino', 'Palmeiras', 'Internacional'

# Todos os times
print(f'Os times do Campeonato Brasileiro são: {times}')

# A) Os 5 primeiros.
print(f'Os primeiros 5 times são: {times[:5]}')

# B) Os últimos 4 colocados.
print(f'Os últimos 4 times são: {times[16:]}')

# C) Times em ordem alfabética.
print(f'Os times em ordem alfabética são: {sorted(times)}')

# D) Em que posição está o time da Chapecoense.
# Como a Chapecoense não está na lista, irei escolher o Flamengo
flamengo = times.index("Flamengo") + 1
print(f'O Flamengo está na {flamengo}ª posição')
