def divide():
    
    try:
        op1=(float(input("Introduce el primer n°: ")))
        op2=(float(input("Introduce el segundo n°: ")))

        print("El resultado es: " + str(op1/op2))
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except ValueError:
        print("El valor introducido no es numérico")
    finally:
        print("Se ha intentado ejecutar la función en su totalidad")

divide()

print("Calculo finalizado. Continuamos con el programa")