# Sumador de números naturales, hasta valor dado, forma recursiva
def sumador(numero):
    if numero <= 1:
        return numero
    else: 
        return numero + sumador(numero - 1)
    
print(sumador(int(input("Ingrese un número: "))) )