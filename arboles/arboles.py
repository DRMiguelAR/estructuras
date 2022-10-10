class Nodo:
    def __init__(self, valor):
        self.valor= valor
        self.padre= None
        self.hijos= []
    def __repr__(self):
        return "N-"+str(self.valor)
    def es_hoja(self):
        return not self.hijos

class Arbol:
    def __init__(self, nodo):
        self.raiz= nodo
    def es_ancestro(self, ancestro, descendiente):
        explorador= descendiente
        while True:
            if explorador== ancestro:
                return True
            if explorador== self.raiz:
                return False
            explorador= explorador.padre
    

def padre_hijo(n1, n2):
    n1.hijos.append(n2)
    n2.padre= n1

def es_padre(padre, hijo):
    return hijo in padre.hijos

def es_hijo(hijo, padre):
    return hijo.padre is padre
