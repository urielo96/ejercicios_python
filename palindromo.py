# Ejercicio que comprueba si un strin es un palindromo
# Inico 5:34

palabra = 'raasdfasdllar'
reversed_word = ''

# ¿ Como se si una palabra es palindromo ?
# Primero leer de izquierda a derecha y despues de leer de derecha izquierda

for letra in reversed(palabra.lower()):
    reversed_word += letra 



if palabra.lower() == reversed_word:
    print('La palabra es un palindromo')
else:
    print('La palabra no es un palindromo')



# for i in range(len(palabra)- 1 ,-1,-1):
#     print(palabra[i])