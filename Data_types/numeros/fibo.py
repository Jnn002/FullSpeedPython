# Calcular la serie de FIbonacci hasta un número dado
num1, num2 = 0, 1
limite = int(input('Ingrese hasta que número desea la serie de Fibonacci: '))
# Ciclo para calcular la serie de Fibonacci
while num1 <= limite:
    print(num1, end=',')
    num1, num2 = num2, num1 + num2