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
diferencia_con_max = 100 - dalto_curso*1000 // otros_cursos_max * 100
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100
#calculando el porsentaje de tiempo vacio removido
tiempo_vacio_promedio - - otros_cursos_promedio = 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - otros_cursos = 1000 // crudo_dalto / 10



#mostrando las diferencias de durecion (ejercicio a)
print(f'El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido')
print(f'El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento')
print(f'El curso de Dalto dura un {diferencia_con_promedio}%menos que el promedio')

#mostrando la cantidad de espacios vacios que se remueven (ejercicio b)
print(f'Elcurso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimino el {tiempo_vacio_dalto})