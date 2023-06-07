from ClaseDocente import Docente
from ClaseInvestigador import Investigador

class DocenteInvestigador(Docente,Investigador):
    __CategIncentivos=0
    __importeExtra=0

    def getCuil(self):
        return super().getCuil()
    def getApellido(self):
        return super().getApellido()
    def getNombre(self):
        return super().getNombre()
    def getBasico(self):
        return super().getBasico()
    def getAntiguedad(self):
        return super().getAntiguedad()
    def getCarrera(self):
        return super().getCarrera()
    def getCargo(self):
        return super().getCargo()
    def getCatedra(self):
        return super().getCatedra()
    def getAreaInv(self):
        return super().getAreaInv()
    def getTipoInv(self):
        return super().getTipoInv()
    def getCategoria(self):
        return self.__CategIncentivos
    def getExtra(self):
        return self.__importeExtra

    def toJson(self):
        dic=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldobasico=self.getBasico(),
                antiguedad=self.getAntiguedad(),
                carrera=self.getCarrera(),
                cargo=self.getCargo(),
                catedra=self.getCatedra(),
                areainv=self.getAreaInv(),
                tipoinv=self.getTipoInv(),
                categoriaIncent=self.__CategIncentivos,
                importeExtra=self.__importeExtra
            )
        )
        return dic
    def getSueldo(self):
        total=Docente.getSueldo(self)+self.__importeExtra
        return total
    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad,
     carrera, cargo, catedra,areainv, tipoinv,categoriaIncent,importeExtra):

        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad,    
        carrera, cargo, catedra, areainv, tipoinv)
        self.__CategIncentivos=categoriaIncent
        self.__importeExtra=importeExtra
    def __str__(self):
        p=super().__str__()
        categoriaIncent="Categoria en el programa de incentivos: {} \n".format(self.__CategIncentivos)
        importeExtra="Importe Extra: {} \n" .format(self.__importeExtra)
        Cadena=p + categoriaIncent + importeExtra
        return Cadena    
    
    def SetImporte_extra(self,nuevoImporteExtra):
        self.__importeExtra=nuevoImporteExtra
    