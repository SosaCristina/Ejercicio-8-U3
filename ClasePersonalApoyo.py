from ClasePersonal import Personal
class PersonalApoyo(Personal):
    __categoria=""
    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__categoria=categoria
    def getSueldo(self):
        total=0
        porcAnt=(self.getAntiguedad()*1)/100
        if(int(self.__categoria)<=10 and int(self.__categoria)>=1):
            porcCat=self.getBasico()*0.10
        else:
            if(int(self.__categoria)<=20 and int(self.__categoria)>=11):
                porcCat=self.getBasico()*0.20
            else:
                if(int(self.__categoria)<=22 and int(self.__categoria)>=21):
                    porcCat=self.getBasico()*0.30
        total=self.getBasico()+(porcAnt*self.getBasico()+porcCat)
        return total
    
    def SetPorcentaje_categoria (self,nuevoPorcentaje):
        print("CAMBIAR POCENTAJE")