import json
from pathlib import Path
import requests
import os
import sys


try:
    def numero_pruebas(datos):
        print("Numero de pruebas : %s"%len(datos))
    
    def pruebas_mas_2_horas(datos):
        for prueba in datos:
            if prueba["Horas"]>2:
                print(prueba['Titulo'])

    def url_pruebas_no_presencial(datos):
        for prueba in datos:
            if prueba["TipoFormacion"]=="NoPresencial":
                print(prueba['URL'])

    def titulo_profesores_id_prueba(datos):
        id_prueba=int(input("Introduce el id de la prueba: "))
        if datos["$id"]==id_prueba:
            print("datos['Titulo']")
            for profesor in datos["Profesorado"]:
               print(profesor["NombreCompleto"])
            






#estas 3 lineas es para abrir un fichero xml, son siempre las mismas y me devuelve en la ¿variable(objeto)? arbol todo el xml
    
    base_path = Path(__file__).parent
    file_path = (base_path / "prueba_idiomas.json").resolve()
    with open(file_path,'r') as file:
        #json.load. devuelve un objeto de tipo diccionario sobre el que se puede iterar.
        datos = json.load(file)
    

    while True:
        os.system("cls")
        print("1.- ¿Cuantas pruebas de idiomas están descritas en el documento?")
        print("2.- Devuelve el título de las pruebas de nivel que van a durar más de dos horas.")
        print("3.- De las pruebas de tipo “No Presencial” devuelve la URL de información.")
        print("4.- Recibe el código de la prueba “ID” y muestra su título y profesores.")
        print("5.- Para cada uno de las pruebas, muestra su título y sus profesores..")
        print("6.- Salir")
        while True:
            try:
                opcion = int(input("Introduce un numero entero: "))
                break
            except ValueError:
                print('Error, introduce un numero entero')
        if opcion == 1:
            numero_pruebas(datos)
        elif opcion == 2:
            pruebas_mas_2_horas(datos)
        elif opcion == 3:
            url_pruebas_no_presencial(datos)
        elif opcion == 4:
           titulo_profesores_id_prueba(datos)
        elif opcion == 6:
            break
        else:
            print ("Introduce un numero entre 1 y 3")
        
        input ("Pulsa una tecla para continuar ....")

  

    
    input ("Pulsa una tecla para terminar ....")

except Exception as e: # 
    print("Ha ocurrido un error no previsto", type(e).__name__ )
