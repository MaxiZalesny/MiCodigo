archivo_sin_leer = open("archivos\\texto_de_dalto.txt",encoding="UTF-8")

#LEER ARCHIVO COMPLETO
archivo = archivo_sin_leer.read()

# leer linea por linea
#archivo = archivo_sin_leer.readlines()

#LEER UNA SOLA LINEA
lineas = archivo_sin_leer.readlines(2)


#cerrar el archivo
archivo.close()


print(lineas)