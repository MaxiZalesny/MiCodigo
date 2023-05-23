animales = ["pez","gato","perro","loro","cocodrilo"]
numeros = [52,16,14,72]


#recorriendo la lista animales
for numero in animales:
    print(f'ahora la variable animal es igual a : {animales}')
    
#recorriendo la lista numeros y multiplicando valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
        
#iterando dos listas del mismo tamaño al mismo tiempo  
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")  

#forma no optima de recorer una lista
for num in range(len(numeros)):
    print(numeros[num])  


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
    
    
    
#todo lo anterior funcioma exactamente igual para tuplas   y conjuntos       