import json

class Personal:
    __cuil=0
    __apellido=""
    __nombre=""
    __sueldobasico=0
    __antiguedad=0
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,areainv="",tipoinv="",carrera="",cargo="",catedra=""):
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldobasico=sueldobasico
        self.__antiguedad=antiguedad

    def getCuil(self):
        return self.__cuil
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getBasico(self):
        return self.__sueldobasico
    def getAntiguedad(self):
        return self.__antiguedad
        
    def toJson(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.__cuil,
                apellido=self.__apellido,
                nombre=self.__nombre,
                sueldobasico=self.__sueldobasico,
                antiguedad=self.__antiguedad
            )
        )
        return d

    def __str__(self):
        cuil="Cuil: {} \n".format(self.__cuil)
        apellido="Apellido: {} \n" .format(self.__apellido)
        nombre="Nombre: {} \n".format(self.__nombre)
        sueldobasico="Sueldo Basico: {} \n".format(self.__sueldobasico)
        antiguedad="Antiguedad: {} \n".format(self.__antiguedad)
        Cadena=cuil + apellido + nombre+sueldobasico+antiguedad
        return Cadena