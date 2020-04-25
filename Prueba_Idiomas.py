import json
from pathlib import Path
import requests
import os
try:

#estas 3 lineas es para abrir un fichero xml, son siempre las mismas y me devuelve en la ¿variable(objeto)? arbol todo el xml
    
    base_path = Path(__file__).parent
    file_path = (base_path / "prueba_idiomas.json").resolve()
    

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
            listado_provincias(arbol)
        elif opcion == 2:
            listado_provincias_municipios(arbol)
        elif opcion == 3:
            municipios_provincia(arbol)
        elif opcion == 4:
            provincia_de_un_municipio(arbol)
        elif opcion == 5:
            break
        else:
            print ("Introduce un numero entre 1 y 3")

  

    
    input ("Pulsa una tecla para terminar ....")

except Exception as e: # 
    print("Ha ocurrido un error no previsto", type(e).__name__ )
