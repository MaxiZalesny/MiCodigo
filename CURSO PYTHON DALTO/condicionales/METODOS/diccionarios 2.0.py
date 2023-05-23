#creando diccionario con dict()
diccionario = dict(nombre="lucas",apellido="dalto")

#las listas no pueden ser clavs y usamos frozenset para meter conjuntos
diccionario = { frozenset(["dalto","rancio"]):"ajajhajh"}

#creando diccionarios con fromkeys() con dos parametros
diccionario = dict.fromkeys(["nombre","apellido" "seguidore"]) 

#creando diccionarios con fromkeys() con dos parametros
diccionario = dict.fromkeys("ABCDE","ALGUN VALOR FIJO")
print(diccionario)

3:29:26