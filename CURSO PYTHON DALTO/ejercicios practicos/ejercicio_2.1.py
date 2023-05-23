#Falto el profe y los pibes van a armar la clase.
#pedir el nombre y la edad de los compañeros que vinieron hoy a clase .
def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: "))
        compañero = (nombre,edad)
       
       #agregando la informacion a la lista
        compañeros.append(compañero)
    
    #ordenando de menor a mayor segun su edad 
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros[x] devuelve una tupla con ( nombre,edad) y 
    # despues accedemos al nombre
    #paradefinir al asistentey al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente, profesor
    
    #desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)
    
print(f"el profesor es:{profesor} y su asistente es {asistente}")    