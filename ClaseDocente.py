from ClasePersonal import Personal
class Docente(Personal):
    __carrera=""
    __cargo=""
    __catedra=""
   
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
        return self.__carrera
    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra
    
    def toJson(self):
        dic=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldobasico=self.getBasico(),
                antiguedad=self.getAntiguedad(),
                carrera=self.__carrera,
                cargo=self.__cargo,
                catedra=self.__catedra
            )
        )
        return dic
    def getSueldo(self):
        total=0
        porcAnt=(self.getAntiguedad()*1)/100
        if(self.__cargo.lower()=='simple'):
            porcCargo=self.getBasico()*0.10
            total=self.getBasico()+(porcAnt*self.getBasico())+porcCargo
        else:
            if(self.__cargo.lower()=='semiexclusivo'):
                porcCargo=self.getBasico()*0.20
                total=self.getBasico()+(porcAnt*self.getBasico())+porcCargo
            else:
                if(self.__cargo.lower()=='exclusivo'):
                    porcCargo=self.getBasico()*0.50
                    total=self.getBasico()+(porcAnt*self.getBasico())+porcCargo
        return total
    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra,areainv="",tipoinv=""):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad,areainv,tipoinv)          
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra

    def __str__(self):
        p=super().__str__()
        carrera="Carrera: {} \n".format(self.__carrera)
        cargo="Cargo: {} \n" .format(self.__cargo)
        catedra="Catedra: {} \n".format(self.__catedra)
        Cadena=p + cargo + carrera + catedra
        return Cadena
    
    def SetPorcentaje_cargo(self,nuevoPorcentaje):
        print("CAMBIAR PORCENTAJE")