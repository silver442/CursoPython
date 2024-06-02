
musicos=["Paul McCarthey", "Bruce Springsteen", "Tina Turner", "Justin Bieber", "Elton John"]

# Ordenar por apellidos

'''def ordena_musicos(m):

    return m.split()[1]

musicos.sort(key=ordena_musicos)'''

musicos.sort(key=lambda m:m.split()[1])

print(musicos)