#promedio de duracion
otros_cursos_max = 7 
otros_cursos_min = 2.5
otros_cursos_promedio = 4
dalto_curso = 1.5
#duracion de crudos
crudo_promedio =5
crudo_dalto =3.6
#diferencias de duracion

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso*1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando el porsentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

print("------------")

#mostrando las diferencias de durecion (ejercicio a)
print(f'El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido')
print(f'El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento')
print(f'El curso de Dalto dura un {diferencia_con_promedio}%menos que el promedio')
print("------------")

#mostrando la cantidad de espacios vacios que se remueven (ejercicio b)
print(f'Elcurso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio')
print("------------")
#Mostrando diferencias si los cursos duraran 10 hrs
print(f'Ver 10 horas de este curso quivalen a ver {otros_cursos_promedio * 1000 // dalto_curso / 100} horas de otros cursos')
      
print(f'Ver 10 horas de otros cursos quivalen a ver {otros_cursos_promedio  * 1000 // otros_cursos_promedio / 10} horas de otros cursos')
print("------------")    
      #2:59:03