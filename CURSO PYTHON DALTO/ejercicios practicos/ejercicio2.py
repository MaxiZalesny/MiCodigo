frase = input("decime una frase y te calculo cuanto tardarias si tuvieras que decirla:")
palabras_separadas =frase .split("")
cantidad_de_palabras =len(palabras_separadas)
print(f'dijiste {cantidad_de_palabras}palabras,y tardarias {cantidad_de_palabras/2}segundos en decirlo')
print(f'Dalto lo diria en{cantidad_de_palabras/2*1.3}segundos en decirlo')
if cantidad_de_palabras > 120:
    print("para flaco tampoco te pedi un testamento")