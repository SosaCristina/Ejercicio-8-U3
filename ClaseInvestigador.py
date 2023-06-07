from ClasePersonal import Personal
class Investigador(Personal):
    __areainv=""
    __tipoinv=""
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
    def getAreaInv(self):
        return self.__areainv
    def getTipoInv(self):
        return self.__tipoinv

    def toJson(self):
        dic=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldobasico=self.getBasico(),
                antiguedad=self.getAntiguedad(),
                areainv=self.__areainv,
                tipoinv=self.__tipoinv
            )
        )
        return dic

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, areainv, tipoinv):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)      # LLamado a clase base
        self.__areainv=areainv
        self.__tipoinv=tipoinv
    def getSueldo(self):
        total=0
        porcAnt=(self.getAntiguedad()*1)/100
        total=self.getBasico()+(self.getBasico()*porcAnt)
        return total

    def __str__(self):
        p=super().__str__()
        areainv="Area de investigacion: {} \n".format(self.__areainv)
        tipoinv="Tipo de investigacion: {} \n" .format(self.__tipoinv)
        Cadena=p + areainv + tipoinv
        return Cadena