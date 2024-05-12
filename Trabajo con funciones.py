# definición (creación) de la función
def imprimeMensajes():

    return "Este es el mensaje de la función"

def imprimeMensajePersonalizado(mensaje, valor1, valor2):

    return mensaje + str(valor1+valor2)

print(imprimeMensajePersonalizado("La suma es ", 10, 10))