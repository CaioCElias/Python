frase = 'curso em vídeo python'
# Mostra o 9 caractere
frase[9]

# Mostra do 9 caractere até o 13 (sem mostrar o 13)
frase[9:13]

# Mostra do 9 ao 21 pulando 2 caracteres casa vez
frase[9:21:2]

# Vai do 9 até o final pulando 3
frase[9::3]

# Mostra quantos caracteres tem no total (contando espaços)
len(frase)

# Mostra quantas vezes aparece o conjunto definido
frase.count('o')
frase.count('o', 0, 13) # Definindo onde deve procurar

# Prucura onde começa o seguinte conjunto
frase.find('deo')
frase.find('Android') # Se não achar, o resultado será -1

# Diz se existe a seguinte palavra dentro do conjunto
'Curso' in frase

# Modifica uma palavra escolhi por outra que vocÊ definiu
frase.replace('Python', 'Android')

# DEIXA MAIÚSCULO
frase.upper()

# deixa minúsculo
frase.lower()

# Deixa capitalizado
frase.capitalize()

# Deixa Em Formato De Título
frase.title()

# Separa as palavras das frases em subconjuntos
phrase.split()

# Adiciona o caractere definido entre os subconjuntos
'-'.join(frase)

phrase = '           Aprenda Python                          '

# Elimina os espaços desnecessários ANTES e DEPOIS da frase
phrase.strip()

# Elimina os espaços desnecessários DEPOIS da frase
phrase.rstrip()

# Elimina os espaços desnecessários ANTES da frase
phrase.lstrip()
