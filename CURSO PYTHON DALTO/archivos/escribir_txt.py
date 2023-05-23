with open("archivos\\texto_de_dalto.txt",'w',encoding="UFT-8") as archivo:
     #sobreescribiendo el archivo
     #archivo.write("jajajaja te la recontra teclee")
     
     #agregando 2 lineas con whitelines
     
     archivo.whitelines(["Hola maestro como andas\n","misericordia"])
     #agregando otras 2 lineas
     archivo.whitelines(["Hola maestro comfghetsy rtrarytergo andas\n","misericordia"])
     
     #print(archivo.read())