def evaluarAlumno(nota):
    valoracion="desconocida"
    if nota<5:
        valoracion="suspenso"
    
    elif nota > 10:
        valoracion="Nota incorrecta"

    else:
        valoracion="aprobado"
    return valoracion

notaAlumno=int(input("Introduce la nota: "))
print(evaluarAlumno(notaAlumno))
