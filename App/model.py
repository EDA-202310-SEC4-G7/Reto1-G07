﻿"""
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
    data["Total saldo a pagar"], data["Total saldo a favor"], data["Total retenciones"])

    lt.addLast(data_structs["data"], d)
    
    return data_structs

def codigoActividadEconomicaSize(control): ### CAMBIOS ### 
    return lt.size(control['Código actividad económica'])


# Funciones para creacion de datos

def new_data(Año, Codigo_acti_eco,Nombre_acti_eco,Codigo_sec_eco,Nombre_sec_eco,Codigo_sub_eco,Nombre_sub_eco,Total_ing_net,Total_cst_gst,Total_sld_pag,Total_sld_fvr,Total_ret):
    """
    Crea una nueva estructura para modelar los datos
    """
    data = {"Año":Año,"Código actividad económica":Codigo_acti_eco,"Nombre actividad económica":Nombre_acti_eco,"Código sector económico":Codigo_sec_eco,"Nombre sector económico":Nombre_sec_eco,"Código subsector económico":Codigo_sub_eco,"Nombre subsector económico":Nombre_sub_eco,"Total ingresos netos":Total_ing_net,"Total costos y gastos":Total_cst_gst,"Total saldo a pagar":Total_sld_pag,"Total saldo a favor":Total_sld_fvr, "Total retenciones": Total_ret}
    

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
    pass


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

    """Create list of lists by year"""
    num = 1
    listByYears = lt.newList(datastructure="ARRAY_LIST")
    Year_1 = lt.firstElement(data_structs["data"])["Año"]
    listYear = lt.newList(datastructure="ARRAY_LIST" )
    while num < lt.size(data_structs["data"]) : 
        data = lt.getElement(data_structs["data"], num)
        year = int(data["Año"])
        if year  == Year_1:
            lt.addLast(listYear, data)
        else:
            lt.addLast(listByYears, listYear)
            listYear = lt.newList(datastructure="ARRAY_LIST" )
            lt.addLast(listYear, data)
        num+= 1
        Year_1 = int(data["Año"])
    lt.addLast(listByYears, listYear)

    #return listByYears["elements"][10]

    """For 2012"""
    list_2012 = listByYears["elements"][10]
    for value in range(len(list_2012["elements"])):
        sublist = list_2012["elements"][value]
        subsector_info = sublist["Nombre sector económico"], sublist["Total retenciones"]
        Newlist = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(Newlist, subsector_info)
        print(Newlist)
        #print (Newlist[subsector])


    """For 2013"""
    list_2013 = listByYears["elements"][9]
    """For 2014"""
    list_2014 = listByYears["elements"][8]
    """For 2015"""
    list_2015 = listByYears["elements"][7]
    """For 2016"""
    list_2016 = listByYears["elements"][6]
    """For 2017"""
    list_2017 = listByYears["elements"][5]
    """For 2018"""
    list_2018 = listByYears["elements"][4]
    """For 2019"""
    list_2019 = listByYears["elements"][3]
    """For 2020"""
    list_2020 = listByYears["elements"][2]
    """For 2021"""
    list_2021 = listByYears["elements"][1]


    """Get the minor value of total retentions"""

    #for year in listByYears[0]:
     #   return (year)

        
            
        
            
            

    



def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


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


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


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
    
def compareYears(year_1, year_2):
    if year_1["Año"] < year_2["Año"]:
        return True
    elif year_1["Año"] > year_2["Año"]:
        return False
    elif year_1["Año"] == year_2["Año"]:

        if year_1["Nombre subsector"] < year_2["Nombre subsector"]:
            return True
        elif year_1["Nombre subsector"] > year_2["Nombre subsector"]:
            return False
        elif year_1["Nombre subsector"] == year_2["Nombre subsector"]:

            if year_1["Total retenciones"] < year_2["Total retenciones"]:
                return True
            elif year_1["Total retenciones"] > year_2["Total retenciones"]:
                return False
            else:
                return False

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