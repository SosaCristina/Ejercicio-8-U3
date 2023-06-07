import json
from pathlib import Path
from ClaseDocente import Docente
from ClaseDocInv import DocenteInvestigador
from ClasePersonalApoyo import PersonalApoyo
from ClaseInvestigador import Investigador
from ClaseColeccion import Coleccion
from ClasePersonal import Personal

class ObjectEncoder(object):
    def GuardarArchivo(self,dic,archi):
        with Path(archi).open('w',encoding="UTF-8") as destino:
            json.dump(dic,destino,indent=4)
            destino.close()
    def LeerArchivo(self,archi):
        with Path(archi).open(encoding="UTF-8") as fuente:
            dic=json.load(fuente)
            fuente.close
            return dic
    def DecodificarDiccionario(self,dic):
        if '__class__' not in dic:
            return dic
        else:
            class_name=dic['__class__']
            class_=eval(class_name)
            if(class_name=='ListaPersonal'):
                personal=dic['personal']
                lista=class_()
                for i in range(len(personal)):
                    dPersonal=personal[i]
                    print(dPersonal)
                    class_name=dPersonal.pop('__class__')
                    class_=eval(class_name)
                    atributos=dPersonal['__atributos__']
                    unpersonal=class_(**atributos)
                    lista.AgregarAgente(unpersonal)
            return lista