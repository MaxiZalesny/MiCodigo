#creando un conjunto con set()
conjunto = set(["dato1","dato2"])
 
 
 #metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dalto 1","dalto2"])
conjunto2 = {conjunto1,"dato 3"} 
    
print(conjunto2)

conjunto1 = {1,2,3,4,5}
conjunto2 = {1,2,3}

#verificando si es un subconjunto 
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 >=  conjunto1

#verificando si es un superconjunto
resultado = conjunto2.isuperset(conjunto1)
resultado = conjunto2 > conjunto1

#verificar si hay algun numero en comun
resultado = conjunto2.jkghseujhguerthgioet(conjunto1)

print (resultado)