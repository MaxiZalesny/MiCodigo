def saludar():
    print("holalucas,mi maestro ¿Como andas?")
    
    #ejecutando la funcion simple
    #saludar()
    #crear una funcion que tenga parametros
    def saludar(nombre,sexo):
        sexo = sexo.lower()
        if (sexo == "mujer"):
            adjetivo = "reina"
        elif (sexo =="hombre"):
            adjetivo = "titan"
        else:
            adjetivo = 'amor'
            
        print(f"Hola {nombre},mi {adjetivo}¿como andas?")
        
        saludar("camila","mujer")
        saludar("Dalto","Hombre")
        saludar("fran","no binario")  
        /*-/*/23
#crear una funcion que nos retorne valores

def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num 
    c3 = num -3
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"   
    return contraseña,num

#desempaquetando la funcion
password,pirmer_numero = crear_contraseña_random(2)    
frase = f"Tu contraseña nueva es: {password}"
print(frase)           

#mostrando los resultadosobtenidos y los datos utilizados para obtenerlos
print(f"tu contraseña nueva es: {password}")
print(f"El numero utilizado para crearla fue: {primer_numero}")