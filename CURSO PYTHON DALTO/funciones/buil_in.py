numeros = [4,7,1,42,15]


#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrando el numero menor de una lista 
numero_mas_bajo=min(numeros)
print(numero_mas_bajo)

#redondeando a 6 decimales
numero = round(12.34567,4)#despues de la coma va la cantidad de decimales 

#retorna Falce -> 0 ,vacio,False,none \ true -> distinto a 
# 0 , true, cadena, datos no vacios

resultado_bool = bool("greftgwergr")

#retorna true,  si todos los valores son verdaderos
resultado_all = all ([None],"True",[345,45])
print(resultado_all)

#suma todos los valores de un iterable
suma_total = sum(numero)

print(suma_total)