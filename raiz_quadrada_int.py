import math

def main():
	for i in range(0, 1000, 1):
		raiz_quadrada = math.sqrt(i)
		if raiz_quadrada.is_integer():
			print(i)

main()