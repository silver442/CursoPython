def validarUsuario(user):

    if(15<len(user) or len(user)<5):
        if len(user) < 5:
            print("el suario no puede tener menos de 5 caracteres")
            return  False
        else:
            print("El ususrio no puede tener más de 15 caracteres")
            return False
        
    else:
        if user.isalnum():
            return True
    
        else:
            return False
    

'''La función de validación de contraseñas debe cumplir las siguientes restricciones:

Debe tener más de 10 caracteres. Si se incumple esta restricción, la función devolverá el mensaje “La contraseña debe tener más de 10 caracteres”
Debe contener al menos un carácter que no sea ni letra ni número. Si se incumple esta restricción, la función devolverá el mensaje “La contraseña debe contener un carácter que no sea ni letra ni número”
Debe contener al menos una letra mayúscula y una letra minúscula. Si se incumple esta restricción, la función devolverá el mensaje “La contraseña no es segura”
No puede tener espacios en blanco. Si se incumple esta restricción, la función devolverá el mensaje “La contraseña no puede contener espacios en blanco”
Si el usuario es correcto, la función devolverá True.'''

def validarContraseña(password):

    if len(password) < 10:
        print("La contraseña debe tener más de 10 caracteres")
        return False

    elif password.isalnum():
        print("La contraseña debe contener un caracter que no sea ni letra ni número")
        return False
    
    elif password.islower() or password.isupper():
        print("La contraseña no es segura. Combina mayusculas y minusculas")
        return False
    elif " " in password:
        print("La contraseña no puede contener espacios en blanco")
        return False
    else:
        return True

    
