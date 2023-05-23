#forma no optoma de sumar valores 
#def suma(lista):
#    numeros_sumados =  0
#    for numeros in lista:
#        numeros_sumados = numeros_sumados + numeros 
#    return Uneros_sumados


#resultado =  suma([5,54,6,64,67,7,8])            


print(resultado)
#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,54,6,64,67,7,8])

#lo mismo que arriba pero utilizando el operador *como argumento  (*arg)
def suma(*numeros):
    return f"{nombre}, la suma de tus numeros es:{sum(numeros)}"
resultado = suma("lucas"5,54,6,64,67,7,8)
print(resultado)    