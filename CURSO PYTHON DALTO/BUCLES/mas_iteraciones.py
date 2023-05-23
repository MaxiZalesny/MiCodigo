
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "HolaDalto"
numeros = [2,5,8,10]
#evitanado que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'me voy a comer una {fruta}')
    
    
    #evitar que el bucle siga ejecutandose(el else no se ejecuta tampoco)
    for fruta in frutas:
           print(f'me voy a comer una {fruta}')
    if fruta == 'pera':
            break
    else:
        
        print(f'me voy a comer una {fruta}')

#recorer una cadena de texto
for letra in cadena:
    print(letra)
    
    
#for en una sola linea de codigo
numeros_duplicados = list()
for numero in numeros: 
    numeros_duplicados.append(numero*2)  
    
print(numeros_duplicados)

# o mas facil
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
