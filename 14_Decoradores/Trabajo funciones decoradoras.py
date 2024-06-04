def funcion_decoradora(funcion_parametro):

    def funcion_interna(*args, **kwargs):

        print("A continuación voy a realizar un calculo")

        funcion_parametro(*args, **kwargs)

        print("Ya he terminado el trabajo")

    return funcion_interna


@funcion_decoradora
def suma(num1, num2):

    print(num1+num2)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):

    print(pow(base, exponente))

suma(5,7)

resta(20,5)

potencia(5,3)