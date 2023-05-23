#creando una lista (se pueden modificar)
lista = ["Lucas Dalto","Soy Dalto",True,1.85]

#creando una tupla (no pueden modificar)
tupla = ("Lucas Dalto","Soy Dalto",True,1.85)

#esto es valido 
lista[3] = "Maquinola"

#esto no
# tupla[3] = "Maquinola" 

#creando un conjunto (set)(no se accede a elementos por indece, 
# no almacena datos duplicados)

conjunto = {"Lucas Dalto","Soy Dalto",True,1.85,"SoyDalto"}

#print(conjunto[3]) -> no puede acceder al elemento

#creando un diccionario (dict)(la extructura es key: value y separamos con comas)tantas comas como elementos aya menos 1
diccionario = {
    'nombre' : "Lucas Dalto",
    'canal' : "Soy Dalto",
    'esta_emocionado' : true,
    'altura',
    
}
 
   print(diccionario['altura'])
