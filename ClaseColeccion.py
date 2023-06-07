from ClaseDocente import Docente
from ClaseDocInv import DocenteInvestigador
from ClaseInvestigador import Investigador
from ClasePersonal import Personal
from ClasePersonalApoyo import PersonalApoyo
from zope.interface import implementer
from InterfazTesorero import ITesorero
from InterfazDirector import IDirector
from ClaseNodo import Nodo
import json

class Coleccion:
    __comienzo=None
    __actual=None 
    __indice=0
    __tope=0
    def getTope(self):
        return self.__tope
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:        
            dato=self.__actual.getDato()
            self.__indice+=1  
            self.__actual=self.__actual.getSiguiente()        
            return dato
    
    def toJson(self):
        personal=[]
        for v in self:
            personal.append(v.toJson())
        dic=dict(__class__=self.__class__.__name__,datos=personal)
        return dic
    
    def mostrar(self):
        aux=self.__comienzo
        
        while(aux!=None):
             
            print(aux.getDato())
            aux=aux.getSiguiente()

    def AgregarAgente(self,persona):
        try:
            if(type(persona)==PersonalApoyo or type(persona)==Docente or type(persona)==Investigador or type(persona)==DocenteInvestigador):
                nodo=Nodo(persona)
                if(self.__comienzo==None):
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo=nodo
                    self.__actual=nodo
                    self.__tope+=1
                else:
                    aux=self.__comienzo
                    while(aux.getSiguiente()!=None):
                        aux=aux.getSiguiente()
                    nodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(nodo)
                    self.__tope+=1
                
                print ("Personal Agregado")   
                
        except TypeError:
            print('No es una persona')

    def InsertarAgente(self,pos,Agente):
        try:
            if(pos<=self.__tope):
                nodo=Nodo(Agente)
                if(pos==0):
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo=nodo
                    self.__tope+=1
                    
                    print ("Personal Insertado")   
                    
                else:
                    num=1
                    aux=self.__comienzo
                    while(num<pos):
                        aux=aux.getSiguiente()
                        num+=1
                    nodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(nodo)
                    self.__tope+=1    
                    print ("Personal Insertado")   
                    
        except IndexError:
            print('Posicion Fuera De Rango')
            

    def Inciso3(self,pos):
        try:
            cont=0
            aux=self.__actual
            ban=False
            if(self.__tope>=pos):
                while((pos<=self.__tope)and(ban==False) and (aux!=None)):
                    if(pos==cont):
                        ban=True
                        print("Tipo de agente: {}" .format(aux.getDato().__class__.__name__))
                    else:
                        cont+=1
                        aux=aux.getSiguiente()
                        ban=False
            else:
                raise IndexError
        except IndexError:
            
            print('Error:Fuera de rango')

    def ListadoPorNombre(self,carrera):
        nombres=[]
        try:
            cont=0
            aux=self.__actual
            while((cont<=self.__tope) and (aux!=None)):
                if(isinstance(aux.getDato(),DocenteInvestigador)):
                    if(aux.getDato().getCarrera()==carrera):
                        nombres.append(aux.getDato().getNombre())
                cont+=1
                aux=aux.getSiguiente()
            else:
                if(cont<=self.__tope and nombres==None):
                    
                    print("No se encontraron agentes pertenecientes a la carrera.")
                    
            nombres.sort()
            
            for i in range(len(nombres)):
                aux=self.__comienzo
                
                while(aux!=None):
                    if(nombres[i]==aux.getDato().getNombre() and isinstance(aux.getDato(),DocenteInvestigador) ):
                        
                        print(aux.getDato())
                    aux=aux.getSiguiente()

        except IndexError:
            
            print('Error: Fuera De Rango')
        finally:
            print("Nombres: \n{}".format(nombres))

    def inciso5(self,areainv):
        contDI=0
        contI=0
        try:
            cont=0
            aux=self.__comienzo
            while((cont<=self.__tope) and (aux!=None)):
                if(isinstance(aux.getDato(),DocenteInvestigador)):
                    print(aux.getDato().getNombre())
                    if(aux.getDato().getAreaInv()==areainv):
                        contDI+=1
                else:
                    if(isinstance(aux.getDato(),Investigador)):
                        print(aux.getDato().getNombre())
                        if(aux.getDato().getAreaInv()==areainv):
                            contI+=1
                cont+=1
                aux=aux.getSiguiente()
            else:
                if(cont<=self.__tope and contDI==0 and contI==0):
                    
                    print("No se encontraron agentes pertenecientes a ésta área.")
                    
                else:
                    print("Docentes investigadores: {}" .format(contDI))
                    print("Investigadores: {}" .format(contI))
        except IndexError:
            
            print('Error:posicion Fuera De Rango')

    def OrdenaPorApellidos(self):
        try:
            k=cota=p=None
            aux=None

            while(k!=self.__comienzo):
                k=self.__comienzo
                p=self.__comienzo
                while(p.getSiguiente()!=cota):
                    if(p.getDato().getApellido() > p.getSiguiente().getDato().getApellido()):
                        aux=p.getSiguiente().getDato()
                        p.getSiguiente().setDato(p.getDato())
                        p.setDato(aux)
                        k=p
                    p=p.getSiguiente()
                cota=k.getSiguiente()
        except IndexError:
            
            print('Error:posicion Fuera De Rango')

    def BuscaPorCategorias(self, categoria):
        acum=0
        aux=self.__comienzo
        while(aux!=None):
            if(isinstance(aux.getDato(),DocenteInvestigador)):
                if(aux.getDato().getCategoria()==categoria):
                    
                    print("Nombre: {}".format(aux.getDato().getNombre()))
                    print("Apellido: {}".format(aux.getDato().getApellido()))
                    print("Importe Extra: {}".format(aux.getDato().getExtra()))
                    acum+=aux.getDato().getExtra()
            aux=aux.getSiguiente()
        print("\nCantidad total de dinero a solicitar: ${}".format(acum))
   
    def BuscarCUIL(self,cuil):
        aux=self.__comienzo
        ban=False    
        while aux!=None and not ban:
            if cuil == aux.getDato().getCuil():
                ban=True
                empleado=aux.getDato()
            aux=aux.getSiguiente()    
        return empleado    

            
                    
    

    
    @implementer(ITesorero)
    def gastosSueldoPorEmpleado(self,cuil):
        
        empl=self.BuscarCUIL(cuil)
        if(empl!=0 and empl!=-1):
            print("Empleado: {}".format(empl.getNom()))
            print("DNI: {}".format(cuil))
            print("Sueldo: {}" .format(empl.Sueldo()))
        else:
            print("Empleado no encontrado.")
            
    


    @implementer(IDirector)
    def modificarBasico(cuil, nuevoBasico):
        empl=self.BuscarCUIL(cuil)
        empl.modificar_sueldo(nuevoBasico)
        
     
            

    @implementer(IDirector)        
    def modificarPorcentajeporcargo(cuil, nuevoPorcentaje):
        empl=self.BuscarCUIL(cuil)
        if(isinstance(empl,Docente)):
            empl.SetPorcentaje_cargo(nuevoPorcentaje)

    @implementer(IDirector)        
    def modificarPorcentajeporcategoria(cuil, nuevoPorcentaje):
        empl=self.BuscarCUIL(cuil)
        if(isinstance(empl,PersonalApoyo)):
            empl.SetPorcentaje_categoria(nuevoPorcentaje)
            
    @implementer(IDirector)
    def modificarImporteExtra (cuil,nuevoImporteExtra):  
        empl=self.BuscarCUIL(cuil)      
        if(isinstance(empl,DocenteInvestigador)):
            empl.SetImporte_extra(nuevoImporteExtra)
        