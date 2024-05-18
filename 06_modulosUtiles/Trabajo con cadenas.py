nUsuario = input("Introduce tu usuario: ")

# Upper() pasa todo a mayusculas
print("El usuario introducido es: ", nUsuario.upper())
# capitalize pone la primer letra en mayuscula
print("El usuario introducido es: ", nUsuario.capitalize())

edad=input(" Introduce tu edad, por favor: ")

# isdigit() para saber si el valor introducido es un digito
while edad.isdigit()==False:

    print("El valor introducido no es correcto")

    edad=input(" Introduce tu edad, por favor: ")
    
if(int(edad)<18):

    print("NO puedes pasar")

else:

    print("Puedes pasar")