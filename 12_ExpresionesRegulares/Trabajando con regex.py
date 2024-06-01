import re

cadena="estoy trabajando con Python en domingo y Semana Santa. El proximo domingo no pienso grabar ningún video"

busqueda="domingo"

texto_encontrado=re.search(busqueda, cadena)

# start() devuelve la posicion en donde empieza el texto encontrado

print(texto_encontrado.start())

# end() caracter donde termina
print(texto_encontrado.end())

# span() posicion inicial y final
print(texto_encontrado.span())

# findall() busqueda de todas las veces que se repite la busqueda
print(len(re.findall(busqueda, cadena)))

