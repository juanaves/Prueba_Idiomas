import json
from pathlib import Path
import requests
import os
import sys


try:
    def numero_pruebas(datos):
        print("Numero de pruebas : %s"%len(datos))
    
    def pruebas_mas_2_horas(datos):
        for curso in datos:
            if curso["Horas"]>2:
                print(curso['Titulo'])

    def url_pruebas_no_presencial(datos):
        for curso in datos:
            if curso["TipoFormacion"]=="NoPresencial":
                print(curso['URL'])

    def titulo_profesores_id_prueba(datos):
        id_prueba=input("Introduce el id de la prueba: ")
       
        for curso in datos:
            if curso["id_prueba"]==id_prueba:
                #print (type(curso["id_prueba"]))
                print("Titulo del curso : %s"%curso['Titulo'])
                print("Profesor/es imparten este curso:")
                print("--------------------------------")
                for profesor in curso["Profesorado"]:
                    print(profesor["NombreCompleto"])


    def titulo_profesores_todas_pruebas(datos):
        for curso in datos:
            print("")
            print("Titulo del curso : %s"%curso["Titulo"])
            for profesor in curso["Profesorado"]:
                print("Profesor/es imparten este curso:")
                print("--------------------------------")
                print(profesor["NombreCompleto"])
                
        
    

            



#vamos a cambiar el utf para que me aparezcan los caracteres ñ y acentos
#para ellos necesitamos importar la libreria sys
    codificacion_actual=sys.stdout.encoding
    print(codificacion_actual) #nos visualizaria utf-8
    input ("Pulsa una tecla para continuar ....")



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
        elif opcion == 5:
            titulo_profesores_todas_pruebas(datos)
        elif opcion == 6:
            break
        else:
            print ("Introduce un numero entre 1 y 3")
        
        input ("Pulsa una tecla para continuar ....")

  

    
    input ("Pulsa una tecla para terminar ....")

except Exception as e: # 
    print("Ha ocurrido un error no previsto", type(e).__name__ )
