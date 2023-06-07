
from ClasePersonal import Personal
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocInv import DocenteInvestigador
from ClasePersonalApoyo import PersonalApoyo
from ClaseDecodif import ObjectEncoder
class Menu:
    __userT="uTesorero"
    __passwT="ag@74ck"
    __userG="uDirector"
    __passwG="ufC77#!1"


    __switcher = None
    def  __init__ ( self ): 
        self.__switcher  = { 
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.opcion4,
            5: self.opcion5,
            6: self.opcion6,
            7: self.opcion7,
            8: self.opcion8,
            9: self.opcion9,
            0: self.salir
        }
    def  getSwitcher ( self ):
        return self. __switcher
    def  opcion ( self , op , personal ):
        func = self . __switcher.get(op, lambda:print ( "Opción no válida" ))
        func (personal)

    def salir ( self,personal):
        
        print ( 'Cerrando sistema... Por favor espere.' )
        
    
    def opcion1(self,personal):
        
        pos=input("Ingrese la posicion a insertar (Distinto de 0): ")
        try:
            pos=int(pos)
            if(pos==0 or pos>int(personal.getTope())):
                raise IndexError
            agente=input("Docente ---> (D)\nInvestigador ---> (I)\nPersonal de apoyo ---> (P)\nDocente Investigador ---> (DI) \nOpcion: ")
            agente=agente.lower()
           
            if(agente=='d'):        #Carga de datos Docentes
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                carrera=input("Carrera: ")
                cargo=input("Cargo: ")
                catedra=input("Cátedra: ")
                docente=Docente(cuil,apellido,nombre,sueldobasico,antig,carrera,cargo,catedra)
                personal.InsertarAgente(pos,docente)
                
                

            if(agente=='i'):            # Carga datos Investigador
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                areainv=input("Area de Investigacion: ")
                tipoinv=input("Tipo de investigacion: ")
                inves=Investigador(cuil,apellido,nombre,sueldobasico,antig,areainv,tipoinv)
                personal.InsertarAgente(pos,inves)

            if(agente=='p'):            # Carga datos Personal de apoyo
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                categ=input("Categoria: ")
                pers=PersonalApoyo(cuil,apellido,nombre,sueldobasico,antig,categ)
                personal.InsertarAgente(pos,pers)

            if(agente=='di'):            # Carga datos Docente Investigador
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                carrera=input("Carrera: ")
                cargo=input("Cargo: ")
                catedra=input("Cátedra: ")

                areainv=input("Area de Investigacion: ")
                tipoinv=input("Tipo de investigacion: ")
                
                catincent=input("Categoria en el prog. de Incentivos (I, II, III, IV o V): ")
                impextra=float(input("Importe Extra: "))

                pers=DocenteInvestigador(cuil,apellido,nombre,sueldobasico,antig,carrera,cargo,catedra,areainv,tipoinv,catincent,impextra)
                personal.InsertarAgente(pos,pers)

        except ValueError:
            print("Debe ingresar un valor numerico. ")
            
        except IndexError:
            print("No es posible insertar en esta posicion. ")
            


    def opcion2(self,personal):
        try:
            agente=input("Docente ---> (D)\nInvestigador ---> (I)\nPersonal de apoyo ---> (P)\nDocente Investigador ---> (DI) \nOpcion: ")
            
            
            if(agente=='d'):                 #Carga de datos Docentes
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                carrera=input("Carrera: ")
                cargo=input("Cargo: ")
                catedra=input("Cátedra: ")
                docente=Docente(cuil,apellido,nombre,sueldobasico,antig,carrera,cargo,catedra)
                personal.AgregarAgente(docente)
                
            if(agente=='i'):                     # Carga datos Investigador
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                areainv=input("Area de Investigacion: ")
                tipoinv=input("Tipo de investigacion: ")
                inves=Investigador(cuil,apellido,nombre,sueldobasico,antig,areainv,tipoinv)
                personal.AgregarAgente(inves)

            if(agente=='p'):            # Carga datos Personal de apoyo
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                categ=input("Categoria: ")
                pers=PersonalApoyo(cuil,apellido,nombre,sueldobasico,antig,categ)
                personal.AgregarAgente(pers)

            if(agente=='di'):                    # Carga datos Docente Investigador
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                carrera=input("Carrera: ")
                cargo=input("Cargo: ")
                catedra=input("Cátedra: ")

                areainv=input("Area de Investigacion: ")
                tipoinv=input("Tipo de investigacion: ")
                
                catincent=input("Categoria en el prog. de Incentivos : ")
                impextra=float(input("Importe Extra: "))

                pers=DocenteInvestigador(cuil,apellido,nombre,sueldobasico,antig,carrera,cargo,catedra,areainv,tipoinv,catincent,impextra)
                personal.AgregarAgente(pers)

        except ValueError:
            print("Debe ingresar un valor numerico. ")

    def opcion3(self,personal):
        pos=int(input("Posicion: "))
        personal.Inciso3(pos-1)
        

    def opcion4(self,personal):
        carrera=input("Carrera: ")
        
        personal.ListadoPorNombre(carrera)
        input("Pulse ENTER para continuar...")

    def opcion5(self,personal):
        
        area=input("Ingrese el area de investigacion: ")
        
        personal.inciso5(area)
        

    def opcion6(self,personal):
        personal.OrdenaPorApellidos()
        for p in personal:
            print("*** Datos ***")
            print("Nombre: {}".format(p.getNombre()))
            print("Apellido: {}".format(p.getApellido()))
            print("Tipo de agente: {}".format(p.__class__.__name__))
            print("Sueldo: {}".format(p.getSueldo()))
        

    def opcion7(self,personal):
        cat=input("Ingrese categoria (I, II, III, IV o V): ")
        personal.BuscaPorCategorias(cat)
        
    def opcion8(self,ve):
        Nuevo=ve.toJson()
        Json=ObjectEncoder()
        Json.GuardarArchivo(Nuevo,('Personas Agentes.json'))
        
        print("*** ARCHIVO GUARDADO ***")
        


    
    def opcion9(self,per):
        per.mostrar()

    def opcion10(self,colec):
        ban=False
        while(ban==False):
            us=input("Usuario: ")
            ps=input("Contraseña: ")
            if(us==self.__userT and ps==self.__passwT):
                ban=True
                cuil=input("Ingrese CUIL: ")
                try:
                    
                    colec.gastosSueldoPorEmpleado(cuil)
                except ValueError:
                    print("Debe ingresar un valor Numerico.")
                    
            else:
                print("Usuario o contraseña incorrecto. Intente nuevamente.")
  
    def opcion11(self,colec):
        
        ban=False
        while(ban==False):
            us=input("Usuario: ")
            ps=input("Contraseña: ")
            if(us==self.__userG and ps==self.__passwG):
                ban=True
                cuil=input("Ingrese el CUIL: ")
                try:
                    
                    print("1. Modificar basico")
                    print("2. Modificar Porcentaje por cargo (Docente)")
                    print("3. Modificar Porcentaje por categoria (Personal de apoyo)")
                    print("4. Modificar importe extra (Docente Investigador)")
                    
                    print("0. Menu principal. ")
                    op=int(input("Ingrese su opcion: "))
                    while(op!=0):
                        if(op==1):
                            
                            nuevo=int(input("Ingrese el nuevo valor del básico: "))
                            colec.modificarBasico(cuil,nuevo)
                            
                        if(op==2):
                            
                            nuevo=int(input("Ingrese porcentaje por cargo: "))
                            colec.modificarPorcentajeporcargo(cuil,nuevo)
                            
                        if(op==3):
                            
                            nuevo=int(input("Ingrese porcentaje por categoria: "))
                            colec.modificarPorcentajeporcategoria(cuil,nuevo)
                        if (op==4):
                            nuevo=int(input("Ingrese importe Extra: "))
                            colec.modificarImporteExtra(cuil,nuevo)

                            

                        print("1. Modificar Basico E. Planta")
                        print("2. Modificar Viatico E. Externo")
                        print("3. Modificar Valor E. Por Hora")
                        print("0. Menu principal. ")
                        op=int(input("Ingrese su opcion: "))
                        
                except ValueError:
                    
                    print("Debe ingresar un valor Numerico.")
                    
            else:
                print("Usuario o contraseña incorrecto. Intente nuevamente.")
                