#creando una funcion de tres parametros
#def frase(nombre,apellido,adjetivo):
#    return f'hola{nombre} {apellido},sos muy {adjetivo}'

#utilizando keyword arguments
#frase_resultante = frase(adjetivo = "capo",nombre = "lucas"apellido ="dalto")


#creando la misma funcion con un parametro opcional y un valor por defecto
def frace(nombre,apellido,adjetivo = "Tonto"):
    return f'hola{nombre}{apellido}sos muy {adjetivo}'

frase_resultante = frase("lucas","dalto","inteligente")
print(frase_resultante) 