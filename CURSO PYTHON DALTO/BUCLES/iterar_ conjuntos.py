animales = {"pez","gato","perro","loro","cocodrilo"}
numeros = {52,16,14,72}


#recorriendo la conjunto animales
for numero in animales:
    print(f'ahora la variable animal es igual a : {animales}')
    
#recorriendo la lista numeros y multiplicando valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
        


#forma correcta de recorrer una lista con su indice   
for num in enumerate(numeros):
    indice = num[0] 
    valor = num[1]
    print(f'el indice es:{indice} y el valor es: {valor}')
    
#usando else
for numero in numeros:
    print(f"ejecutando el ultimo bucle;valor actual: {numero}")
else:
    print("el bucle termino")      
    
    
    
#todo lo anterior funcioma exactamente igual para tuplas   y listas      