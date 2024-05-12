def compararListas(lista1,lista2):
    
    if(len(lista1)!=len(lista2)):
        return False
    else:
        for i in range(0,len(lista1)):
            if(lista1[i]!=lista2[i]):
                return False
            
    return True
print(compararListas([1,"lisa",2],[1,"lisa"]))