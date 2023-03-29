import hashlib

class Hash_fun():
    def __init__(self,valor):
        self.valor = valor

    #Funcion en si de Hash
    def Funcion_Hash(self, valor):
        llave = 0
        for i in range(0,len(valor)):
            llave += ord(valor[i])
        return llave % 3