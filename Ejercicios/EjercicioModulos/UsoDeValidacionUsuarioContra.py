from validadionUsuarioContra import *

Usuario=input("Captura tu usuario: ")

while validarUsuario(Usuario)==False:
    Usuario=input("Captura tu usuario: ")

contraseña=input("Captura tu contraseña: ")

while validarContraseña(contraseña)==False:
    contraseña=input("Captura tu contraseña: ")

print("Acceso a la aplicación...")
