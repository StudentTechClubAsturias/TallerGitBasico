"""
Autor: X
"""


#Nota: los primos son: Naturales, > 1, divisibles entre ellos mismo y entre 1
def esPrimo(n):
	"""
	Metodo para comprobar si un numero n dado es primo o no
	params: un numero n
	return: True si es primo y False de no serlo
	"""
	
	#Si es menor que 2 no puede ser primo
	if n < 2:	return False
	
	#El rango de 2 hasta n
	for i in range(2, n):
		if n % i == 0:	return False
	
	return True

def esPrimoIntervalo(i, k):
	"""
	Metodo que comprueba si los numeros de un intervalo son primos o no
	params: intervalo [i ,k)
	return: retorna una lista de duplas
	"""
	return [(x, esPrimo(x)) for x in range(i, k)]


"""
#Probando que funciona <<esPrimo(n)>>
primos = [3, 5, 7, 11, 13, 17, 19, 23, 29]
print [(x, esPrimo(x)) for x in primos]
"""

"""
#Probando que funciona <<esPrimoIntervalo(n)>>
print esPrimoIntervalo(0, 1000)
"""
