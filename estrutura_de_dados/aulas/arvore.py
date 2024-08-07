class Arvore:
    def __init__(self) -> None:
        self.raiz = None
        self.filhos = []

    def set_raiz(self, raiz):
        self.raiz = raiz

    def get_raiz(self):
        return self.raiz

    def __str__(self):
        return str(self.imprimeArvore())
    

    def imprimeArvore(self):
        retorno = [self.raiz]
        listaFilhos = []
        for filho in self.filhos:
            listaFilhos.append(filho.imprimeArvore())
        retorno.append(listaFilhos)
        return listaFilhos


    def altura(self):
        alt = 0
        altMax = 0
        for filho in self.filhos:
            altMax = max(altMax, filho.altura()+1)

        return alt+1

    def insereNo(self, valor):
        filho = Arvore()
        filho.set_raiz(valor)
        self.filhos.append(filho)

    def removeNo(self, valor):
        for filho in self.filhos:
            if filho.get_raiz() == valor:
                self.filhos.remove(filho)
                return filho
            else:
                neto = filho.removeNo(valor)
                if neto:
                    return neto
                
        return None

    def getNo(self, valor):
        for filho in self.filhos:
            if filho.get_raiz() == valor:
                return filho
            else:
                neto = filho.getNo(valor)
                if neto:
                    return neto.getNo(valor)

            
h = Arvore()

h.set_raiz(33)
h.insereNo(27)
h.insereNo(88)
h.insereNo(51)

no88 = h.getNo(88)
no88.insereNo(23)



print(h)
print("Altura: ", h.altura())


no88 = h.getNo(23)
no88.insereNo(76)

print(h)
print("Altura: ", h.altura())

