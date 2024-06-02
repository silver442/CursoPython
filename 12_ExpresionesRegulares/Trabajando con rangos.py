import re

lista_terminos=["Ma1","Se1","Ma2","Va1","Ba1","Se2","Ma3","Ma4","Se3","SeA","Va2","SeC"]

for termino in lista_terminos:
    if re.findall("Se[0-2A-B]", termino):
        print(termino)