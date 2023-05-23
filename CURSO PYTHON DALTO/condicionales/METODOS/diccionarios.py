#keys() -> devuelve las claves , y tambien nos sirve para iterar
#get() -> devuelve el valor de una clave
#clear() -> elimina todos los elementos
#pop() -> elimina un elemento 
#items() -> para iterar el dict



diccionario = {
    "nombre0" : 'lucas',
    "apellido" : 'dalto',
    "subs" : 1000000 
    
    }

#nos devuelve un objeto dict_item
claves = diccionario.keys()

print(claves)


#obteniendo un elemento con get() (no me lanza una exepcion y
# si no encuentra nada el programa continua)
claves = diccionario.get("nombre")

print(claves)

#Eliminando TODO EL DICCIONARIO
diccionario.clear()

print(diccionario)

#eliminando un elementgo del diccionario
diccionario.pop("subs","nombre")
print (diccionario)

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
