frases=["Los lunes son los mejores días para programar",
        "Python es moderno",
        "Veremos Inteligencia Artificial más adelante",
        "Lambda simplifica el código"]

'''def ordena_frases(f):
    return len(f.split())'''

frases.sort(key=lambda f:len(f.split()), reverse=True)

print(frases)