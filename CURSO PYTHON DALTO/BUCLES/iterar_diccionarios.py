diccionario = {
    "nombre" : "lucas",
    "apellido" :"dalto",
    "subs": 10000
}


#recorriendo diccionario para obtener las claves


#recorriendo diccionario con items para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {value}")