
from ClasePersonal import Personal
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocInv import DocenteInvestigador
from ClasePersonalApoyo import PersonalApoyo
from ClaseDecodif import ObjectEncoder
from ClaseColeccion import Coleccion
from Menu import Menu
import json

if __name__ == "__main__":
    personal=Coleccion()
    Json=ObjectEncoder()
    dic=Json.LeerArchivo('Personal.json')
    personal=Json.DecodificarDiccionario(dic)
    menu=Menu()
    ban=False
    while not ban:
        
        print("1. Insertar Agente.")
        print("2. Agregar Agente.")
        print("3. Mostra tipo de agente por posicion.")
        print("4. Generar listado ordenado de datos por nombre de carrera.")
        print("5. Mostrar cantidad de agentes por area.")
        print("6. Generar listado de datos por apellido.")
        print("7. Listar datos por categorias.")
        print("8. Guardar Datos.")
        print("9. Mostrar Lista.")
        print("10. Ingresar como Tesorero.")
        print("11. Ingresar como Director")
        
        print("0. Salir")
        opcion=input("Ingrese una opcion: ")
        opcion=int(opcion)
        menu.opcion(opcion,personal)
        ban=opcion==0