"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(datatype):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    datatype = datatype
    if datatype == 1:
        data_structs = {
            "data": None,
        }

        data_structs["data"] = lt.newList(datastructure="ARRAY_LIST",
                                        cmpfunction=compare)

        return data_structs
    else:
        data_structs = {
            "data": None,
        }

        data_structs["data"] = lt.newList(datastructure="SINGLE_LINKED",
                                        cmpfunction=compare)

        return data_structs    

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    d = new_data(data["Año"], data["Código actividad económica"], data["Nombre actividad económica"],
    data["Código sector económico"], data["Nombre sector económico"], data["Código subsector económico"],
    data["Nombre subsector económico"], data["Total ingresos netos"], data["Total costos y gastos"], 
    data["Total saldo a pagar"], data["Total saldo a favor"])
    lt.addLast(data_structs["data"], d)
    return data_structs

def codigoActividadEconomicaSize(control): ### CAMBIOS ### 
    return lt.size(control['Código actividad económica'])


# Funciones para creacion de datos

def new_data(Año, Codigo_acti_eco,Nombre_acti_eco,Codigo_sec_eco,Nombre_sec_eco,Codigo_sub_eco,Nombre_sub_eco,Total_ing_net,Total_cst_gst,Total_sld_pag,Total_sld_fvr):
    """
    Crea una nueva estructura para modelar los datos
    """
    data = {"Año":Año,"Código actividad económica":Codigo_acti_eco,"Nombre actividad económica":Nombre_acti_eco,"Código sector económico":Codigo_sec_eco,"Nombre sector económico":Nombre_sec_eco,"Código subsector económico":Codigo_sub_eco,"Nombre subsector económico":Nombre_sub_eco,"Total ingresos netos":Total_ing_net,"Total costos y gastos":Total_cst_gst,"Total saldo a pagar":Total_sld_pag,"Total saldo a favor":Total_sld_fvr}
    

    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    x = 1
    listaporAños = lt.newList(datastructure="ARRAY_LIST")
    añoA = lt.firstElement(data_structs["data"])["Año"]
    listaDAño = lt.newList(datastructure="ARRAY_LIST" )
    while x < lt.size(data_structs["data"]) : 
        data = lt.getElement(data_structs["data"], x)
        año = int(data["Año"])
        if año  == añoA:
            lt.addLast(listaDAño, data)
        else:
            lt.addLast(listaporAños, listaDAño)
            listaDAño = lt.newList(datastructure="ARRAY_LIST" )
            lt.addLast(listaDAño, data)
        x+= 1
        añoA = int(data["Año"])
    lt.addLast(listaporAños, listaDAño)
    
    i = 2
    listaN = lt.newList(datastructure="ARRAY_LIST")
    while i < (lt.size(listaporAños)):
        elm = lt.getElement(listaporAños,(i))
        sa.sort(elm,cmptotalsaldop)
        x = lt.getElement(elm,1)
        lt.addLast(listaN,x)
        i+=1
    return listaN

def cmptotalsaldop(data_1,data_2):
    return int(data_1["Total saldo a pagar"]) > int(data_2["Total saldo a pagar"])

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    x = 1
    listaporAños = lt.newList(datastructure="ARRAY_LIST")
    añoA = lt.firstElement(data_structs["data"])["Año"]
    listaDAño = lt.newList(datastructure="ARRAY_LIST" )
    while x < lt.size(data_structs["data"]) : 
        data = lt.getElement(data_structs["data"], x)
        año = int(data["Año"])
        if año  == añoA:
            lt.addLast(listaDAño, data)
        else:
            lt.addLast(listaporAños, listaDAño)
            listaDAño = lt.newList(datastructure="ARRAY_LIST" )
            lt.addLast(listaDAño, data)
        x+= 1
        añoA = int(data["Año"])
    lt.addLast(listaporAños, listaDAño)

    i = 2
    listaN = lt.newList(datastructure="ARRAY_LIST")
    while i < (lt.size(listaporAños)):
        elm = lt.getElement(listaporAños,(i))
        sa.sort(elm,cmpcodigo)
        x = lt.getElement(elm,1)
        lt.addLast(listaN,x)
        i+=1
    return listaN
    
def cmpcodigo(data_1,data_2):
    return int(data_1["Código sector económico"]) > int(data_2["Código sector económico"])

def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs,Top,AnioI,AnioF):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    N = int(Top)
    anioInicio = 2021 - int(AnioI) 
    anioFinal = 2021 - int(AnioF)
    
    x = 1
    listaporAños = lt.newList(datastructure="ARRAY_LIST")
    añoA = lt.firstElement(data_structs["data"])["Año"]
    listaDAño = lt.newList(datastructure="ARRAY_LIST" )
    while x < lt.size(data_structs["data"]) : 
        data = lt.getElement(data_structs["data"], x)
        año = int(data["Año"])
        if año  == añoA:
            lt.addLast(listaDAño, data)
        else:
            lt.addLast(listaporAños, listaDAño)
            listaDAño = lt.newList(datastructure="ARRAY_LIST" )
            lt.addLast(listaDAño, data)
        x+= 1
        añoA = int(data["Año"])
    lt.addLast(listaporAños, listaDAño)
    
    listaperiodo = lt.newList(datastructure="ARRAY_LIST")
    
    while (anioInicio) >= anioFinal:
        
        elem = lt.getElement(listaporAños,(anioInicio + 2))
        pos = 0
        while pos <= lt.size(elem):
            dato = lt.getElement(elem,pos)
            lt.addLast(listaperiodo,dato)
            pos += 1
        anioInicio -= 1
    quk.sort(listaperiodo,cmptotalc_g)
    count = 0
    Lista_top = lt.newList(datastructure="ARRAY_LIST")
    
    while count < N:
        lt.addLast(Lista_top,lt.getElement(listaperiodo,count))
        count +=1
    return Lista_top

def cmptotalc_g(element_1,element_2):
    return int(element_1["Total costos y gastos"]) < int(element_2["Total costos y gastos"])

def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1["id"] > data_2["id"]:
        return 1
    elif data_1["id"] < data_2["id"]:
        return -1
    else:
        return 0

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """

    if (data_1["Año"] > data_2["Año"]):
        return True
    elif (data_1["Año"] < data_2["Año"]):
        return False
    if (data_1["Año"] == data_2["Año"]):
        if (data_1["Código actividad económica"] > data_2["Código actividad económica"]):
            return True
        else:
            return False

#def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
#    sa.sort(data_structs["data"], sort_criteria)
    
def sortSelection(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    se.sort(data_structs["data"], sort_criteria)

def sortInsertion(data_structs):

    ins.sort(data_structs["data"], sort_criteria)

def sortShell(data_strucs):

    sa.sort(data_strucs["data"], sort_criteria)
    
def sortMerge(data_strucs):
    
    merg.sort(data_strucs["data"], sort_criteria)

def sortQuick(data_strucs):
    
    quk.sort(data_strucs["data"], sort_criteria)