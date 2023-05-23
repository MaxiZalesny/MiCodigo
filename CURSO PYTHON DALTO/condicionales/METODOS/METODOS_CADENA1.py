#DIR - DEVUELVE LA LISTA DE ATRIBUTOS VALIDOS DEL OBJETO PASADO

#UPPER - CONVIRETE A MAYUSCULA
#LOWER  - CONVIERTE A MINUSCULA                    
#CAPITALIZE - PRIMERA EN MAYUSCULA
#estos metodos convierten el valor


#FIND - METODO ENCUENTRA LA PRIMERA APARICION DEL VALOR ESPECIFICADO, SINO DEVUELVE UNA EXCEPCION
#INDEX - METODO ENCUENTRA LA PRIMERA APARICION DEL VALOR ESPECIFICADO, SI NO DEVUELVE UNA EXCEPCION
#estos metodos buscan un valor

#ISNUMERIC - SI ES N NUMERICO DEVUELVE TRUE
#ISALPHA  - SI ES ALFANUMERICO DEVUELVE TRUE
#estos metodos consultan si son numericos o alfanumericos

#COUNT - DEVUELVE EL NUMERO DE OCURRENCIAS DE UNA SUBCADENA EN LA CADENA DADA
#LEN - CUENTA LOS CARACTERES DE UNA CADENA

#ENDSWITH - VERIFICA SI UNA CADENA COMIENZA CON
#STARTSWITH - VERIFICA SI UNA CADENA TERMINA CON

#REPLACE - REMPLAZA UN VALOR POR OTRO
#SPLIT - SEPARA POR EL PARAMETRO DADO


cadena1 = "hola soy Dalto"
cadena2 = "Bienvenido maquinola"
#LOS METODOS SON EL : ELDATO.ELNOMBREDELMETODO Y LOS ()

#convierte a minusculas
minusc = cadena1.lower()
#convierte a mayuscula
minusc = cadena1.upper()

#primera letra en mayuscula
primer_letra_mayusc =cadena1.capitalize()


#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("d")

#buscamos una cadena en otra cadena,si no hay coincidencias lanza una excepcion
busqueda_index = cadena1.index("a")
#LA DIFERENCIA ENTRE FIND E INDEX ES QUE INDEX SI NO LO ENCUENTRA TIRA UNA ESEPCION
#si es numerico ,devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos true, si no devolvemos false
es_alfanumerico = cadena1.isalpha()

#contamosamos las coincidencias de una cadena dentro de otra cadena ,devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("la ma")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = cadena1,len()

#verificamos si una cadena empieza con otra cadena dada ,si es asi devuelve true
empieza_con = cadena.startswith("h")
#verificamos si una cadena termina con otra cadena dada , si es asi devuelve true
termina_con = cadena1.endswith("H") 

#si el valor 1 ,se encuentra en la cadena original, reemplaza el valor 1 de la misma por el valor 2
cadena_nueva = cadena1.replace("la","lu")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")  

print(es_numerico)

