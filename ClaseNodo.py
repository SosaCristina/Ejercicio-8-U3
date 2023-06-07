class Nodo:
    __persona=None
    __siguiente=None
    def __init__(self, persona):
        self.__persona=persona
        self.__siguiente=None

    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__persona

    def setDato(self,dato):
        self.__persona=dato
        
    def getNombreClase(self):
        return self.__persona.__class__.__name__