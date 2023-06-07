from zope.interface import Interface
from zope.interface import implementer

class IDirector(Interface):
    def modificarBasico(cuil, nuevoBasico):
        pass
    def modificarPorcentajeporcargo(cuil, nuevoPorcentaje):
        pass
    def modificarPorcentajeporcategoria(cuil, nuevoPorcentaje):
        pass
    def modificarImporteExtra (cuil,nuevoImporteExtra):
        pass