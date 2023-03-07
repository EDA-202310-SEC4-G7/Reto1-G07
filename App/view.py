"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import textwrap

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(datatype):
    """
        Se crea una instancia del controlador
    """
    datat = datatype
    control = controller.new_controller(datat)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Obtener dato dado un ID")
    print("11- Cargar información con un TAD y algoritmo de ordenamiento especifico")
    print("0- Salir")


def load_data(control,filesize,data_type):
    """
    Carga los datos
    """
    filesizex = filesize
    data_types = data_type
    data = controller.load_data(control,filesizex,data_types)
    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.get_data(control, id)
    print("El dato con el ID", id, "es:", data)


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    print(controller.req_1(control))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    print(controller.req_2(control))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print(controller.req_3(control))


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print(controller.req_4(control))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    print(controller.req_5(control))


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print(controller.req_6(control))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    print(controller.req_7(control))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print(controller.req_8(control))

def print_dict_a(control):
    print(controller.dict_a(control))
# Se crea el controlador asociado a la vista
control = new_controller(1)

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                filesize = 0
                x = 1
                filesizei = input("Que tamaño de muestra desea cargar: \n1.5pct \n2.10pct \n3.20pct \n4.30pct \n5.50pct \n6.80pct \n7.large \n8.small \n")
                if int(filesizei) == 1:
                    filesize = "5pct"
                if int(filesizei) == 2:
                    filesize = "10pct"
                if int(filesizei) == 3:
                    filesize = "20pct"
                if int(filesizei) == 4:
                    filesize = "30pct"
                if int(filesizei) == 5:
                    filesize = "50pct"
                if int(filesizei) == 6:
                    filesize = "80pct"
                if int(filesizei) == 7:
                    filesize = "large"
                if int(filesizei) == 8:
                    filesize = "small"
                print("Cargando información de los archivos ....\n")
                data = load_data(control,filesize,3)
                size = lt.size(data["data"])
                last_3 = lt.getElement(data["data"],1)
                last_2 = lt.getElement(data["data"],2)
                last_1 = lt.getElement(data["data"],3)
                first_1 = lt.getElement(data["data"], size)
                first_2 = lt.getElement(data["data"], size-1)
                first_3 = lt.getElement(data["data"], size-2)
                table_size = [["El Total de filas cargadas",size]]
                print (tabulate(table_size, tablefmt="fancy_grid"))
                
                print (tabulate({f'{type}':['1','2','3','4','5','6'],\
                                 'Año':[textwrap.fill(text=textwrap.dedent(text=first_1["Año"])),textwrap.fill(text=textwrap.dedent(text=first_2["Año"])),textwrap.fill(text=textwrap.dedent(text=first_3["Año"])),textwrap.fill(text=textwrap.dedent(text=last_1["Año"])),textwrap.fill(text=textwrap.dedent(text=last_2["Año"])),textwrap.fill(text=textwrap.dedent(text=last_3["Año"]))],\
                                 "Código actividad económica" : [textwrap.fill(text=textwrap.dedent(text=first_1["Código actividad económica"])),textwrap.fill(text=textwrap.dedent(text=first_2["Código actividad económica"])),textwrap.fill(text=textwrap.dedent(text=first_3["Código actividad económica"])),textwrap.fill(text=textwrap.dedent(text=last_1["Código actividad económica"])),textwrap.fill(text=textwrap.dedent(text=last_2["Código actividad económica"])),textwrap.fill(text=textwrap.dedent(text=last_3["Código actividad económica"]))],\
                                 "Nombre actividad económica" : [textwrap.fill(text=textwrap.dedent(text=first_1["Nombre actividad económica"])),textwrap.fill(text=textwrap.dedent(text=first_2["Nombre actividad económica"])),textwrap.fill(text=textwrap.dedent(text=first_3["Nombre actividad económica"])),textwrap.fill(text=textwrap.dedent(text=last_1["Nombre actividad económica"])),textwrap.fill(text=textwrap.dedent(text=last_2["Nombre actividad económica"])),textwrap.fill(text=textwrap.dedent(text=last_3["Nombre actividad económica"]))],\
                                 "Nombre actividad económica" : [textwrap.fill(text=textwrap.dedent(text=first_1["Nombre actividad económica"])),textwrap.fill(text=textwrap.dedent(text=first_2["Nombre actividad económica"])),textwrap.fill(text=textwrap.dedent(text=first_3["Nombre actividad económica"])),textwrap.fill(text=textwrap.dedent(text=last_1["Nombre actividad económica"])),textwrap.fill(text=textwrap.dedent(text=last_2["Nombre actividad económica"])),textwrap.fill(text=textwrap.dedent(text=last_3["Nombre actividad económica"]))],\
                                 "Código sector económico" : [textwrap.fill(text=textwrap.dedent(text=first_1["Código sector económico"])),textwrap.fill(text=textwrap.dedent(text=first_2["Código sector económico"])),textwrap.fill(text=textwrap.dedent(text=first_3["Código sector económico"])),textwrap.fill(text=textwrap.dedent(text=last_1["Código sector económico"])),textwrap.fill(text=textwrap.dedent(text=last_2["Código sector económico"])),textwrap.fill(text=textwrap.dedent(text=last_3["Código sector económico"]))],\
                                 "Nombre sector económico" : [textwrap.fill(text=textwrap.dedent(text=first_1["Nombre sector económico"])),textwrap.fill(text=textwrap.dedent(text=first_2["Nombre sector económico"])),textwrap.fill(text=textwrap.dedent(text=first_3["Nombre sector económico"])),textwrap.fill(text=textwrap.dedent(text=last_1["Nombre sector económico"])),textwrap.fill(text=textwrap.dedent(text=last_2["Nombre sector económico"])),textwrap.fill(text=textwrap.dedent(text=last_3["Nombre sector económico"]))],\
                                 "Código subsector económico" : [textwrap.fill(text=textwrap.dedent(text=first_1["Código subsector económico"])),textwrap.fill(text=textwrap.dedent(text=first_2["Código subsector económico"])),textwrap.fill(text=textwrap.dedent(text=first_3["Código subsector económico"])),textwrap.fill(text=textwrap.dedent(text=last_1["Código subsector económico"])),textwrap.fill(text=textwrap.dedent(text=last_2["Código subsector económico"])),textwrap.fill(text=textwrap.dedent(text=last_3["Código subsector económico"]))],\
                                 "Nombre subsector económico" : [textwrap.fill(text=textwrap.dedent(text=first_1["Nombre subsector económico"])),textwrap.fill(text=textwrap.dedent(text=first_2["Nombre subsector económico"])),textwrap.fill(text=textwrap.dedent(text=first_3["Nombre subsector económico"])),textwrap.fill(text=textwrap.dedent(text=last_1["Nombre subsector económico"])),textwrap.fill(text=textwrap.dedent(text=last_2["Nombre subsector económico"])),textwrap.fill(text=textwrap.dedent(text=last_3["Nombre subsector económico"]))],\
                                 "Total ingresos netos" :[textwrap.fill(text=textwrap.dedent(text=first_1["Total ingresos netos"])),textwrap.fill(text=textwrap.dedent(text=first_2["Total ingresos netos"])),textwrap.fill(text=textwrap.dedent(text=first_3["Total ingresos netos"])),textwrap.fill(text=textwrap.dedent(text=last_1["Total ingresos netos"])),textwrap.fill(text=textwrap.dedent(text=last_2["Total ingresos netos"])),textwrap.fill(text=textwrap.dedent(text=last_3["Total ingresos netos"]))],\
                                 "Total costos y gastos" :[textwrap.fill(text=textwrap.dedent(text=first_1["Total costos y gastos"])),textwrap.fill(text=textwrap.dedent(text=first_2["Total costos y gastos"])),textwrap.fill(text=textwrap.dedent(text=first_3["Total costos y gastos"])),textwrap.fill(text=textwrap.dedent(text=last_1["Total costos y gastos"])),textwrap.fill(text=textwrap.dedent(text=last_2["Total costos y gastos"])),textwrap.fill(text=textwrap.dedent(text=last_3["Total costos y gastos"]))],\
                                 "Total saldo a pagar" :[textwrap.fill(text=textwrap.dedent(text=first_1["Total saldo a pagar"])),textwrap.fill(text=textwrap.dedent(text=first_2["Total saldo a pagar"])),textwrap.fill(text=textwrap.dedent(text=first_3["Total saldo a pagar"])),textwrap.fill(text=textwrap.dedent(text=last_1["Total saldo a pagar"])),textwrap.fill(text=textwrap.dedent(text=last_2["Total saldo a pagar"])),textwrap.fill(text=textwrap.dedent(text=last_3["Total saldo a pagar"]))],\
                                 "Total saldo a favor" :[textwrap.fill(text=textwrap.dedent(text=first_1["Total saldo a favor"])),textwrap.fill(text=textwrap.dedent(text=first_2["Total saldo a favor"])),textwrap.fill(text=textwrap.dedent(text=first_3["Total saldo a favor"])),textwrap.fill(text=textwrap.dedent(text=last_1["Total saldo a favor"])),textwrap.fill(text=textwrap.dedent(text=last_2["Total saldo a favor"])),textwrap.fill(text=textwrap.dedent(text=last_3["Total saldo a favor"]))]\
                                 },headers='keys', tablefmt='fancy_grid'))

            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_dict_a(control)

            elif int(inputs) == 10:
                id = input("Ingrese un id: ")
                print_data(control, id)
            
            elif int(inputs) == 11:
                x = int(input("Que tipo de TAD desea utilizar: 1.Array_list 2.Single_linked"))
                control = new_controller(int(x))
                filesize = 0
                filesizei = input("Que tamaño de muestra desea cargar: \n1.5pct \n2.10pct \n3.20pct \n4.30pct \n5.50pct \n6.80pct \n7.large \n8.small \n")
                if int(filesizei) == 1:
                    filesize = "5pct"
                if int(filesizei) == 2:
                    filesize = "10pct"
                if int(filesizei) == 3:
                    filesize = "20pct"
                if int(filesizei) == 4:
                    filesize = "30pct"
                if int(filesizei) == 5:
                    filesize = "50pct"
                if int(filesizei) == 6:
                    filesize = "80pct"
                if int(filesizei) == 7:
                    filesize = "large"
                if int(filesizei) == 8:
                    filesize = "small"
                sort = int(input("Elija el algoritmo de ordenamiento que desea usar: \n 1. Selection \n 2. Insertion \n 3. Shell \n 4. Merge \n 5. Quick \n"))
                
                print("Cargando información de los archivos ....\n")
                data = load_data(control,filesize,sort)
                size = lt.size(data["data"])
                last_3 = lt.getElement(data["data"],1)
                last_2 = lt.getElement(data["data"],2)
                last_1 = lt.getElement(data["data"],3)
                first_1 = lt.getElement(data["data"], size)
                first_2 = lt.getElement(data["data"], size-1)
                first_3 = lt.getElement(data["data"], size-2)

                print("El total de filas cargadas es: " + str(size)+"\n")
                print("Estos son los primeros tres elementos de la lista: "+str(first_1)+" , "+str(first_2)+" , "+str(first_3)+"\n")
                print("Estos son los últimos tres elementos de la lista: "+str(last_1)+" , "+str(last_2)+" , "+str(last_3)+"\n")
                
            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese una opción válida.\n")
    sys.exit(0)
