#LIST - CREA UNA LISTA

#LEN - CUENTA LA CANTIDAD DE ELEMENTOS DE UNA LISTA

#APPEND - AGREGA UN ELEMENTO A LA LISTA
#INSERT - AGREGA UN ELEMENTO A LA LISTA EN EL INDICEESPECIFICADO
#EXTEND - AGREGA VARIOS ELEMENTOS A LA LISTA

#POP - ELIMINA UN ELEMENTO DE UNA LISTA
#REMOVE - REMUEVE UN ELEMENTO DE UNA LISTA PIDE VALOR
#CLEAR - ELIMINA TODOS LOS ELEMENTOS DE UNA LISTA

#SORT - ORDENA UNA LISTA DE FORMA ASCENDENTE A DESCENTENTE
#REVERSE - INVIERTE LOS ELEMENTOS DE UNA LISTA 


#creando una lista con list()
lista = list(["hola","dalto",34,35,346,True])

#devuelve la cantidad de elementos de le lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append("jajajaja")

#agregando un elemento a la lista de un indice especifico
lista.insert(2,"toma mama")

#agregando varios elementos a la lista 
lista.extend([2030])

#eliminando un elemento de la lista (por su indice)
lista.pop(0)  #para eliminar el ultimo elemento de la lista coloco (-1)
              #(-2)para eliminar el anteultimo y asi sucesivamente 

#removiendo un elemento de la lista (por su valor)
lista.remove("toma mama")

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro reverse=true lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado =  lista.index(56)

#si es  