def funcion_decoradora(funcion_parametro):

    def funcion_interna():

        print("A continuación voy a realizar un calculo")

        funcion_parametro()

        print("Ya he terminado el trabajo")

    return funcion_interna


@funcion_decoradora
def suma():

    print(25+30)

@funcion_decoradora
def resta():
    print(80-25)

suma()

resta()