"""
Autor: X
"""


#Nota: los primos son: Naturales, > 1, divisibles entre ellos mismo y entre 1
def esPrimo(n):
	"""
	Metodo para comprobar si un numero n dado es primo o no
	"""
	
	#Si es menor que 2 no puede ser primo
	if n < 2:	return False
	
	#El rango de 2 hasta n
	for i in range(2, n):
		if n % i == 0:	return False
	
	return True
	

primos = [3, 5, 7, 11, 13, 17, 19, 23, 29]
print [(x, esPrimo(x)) for x in primos]
