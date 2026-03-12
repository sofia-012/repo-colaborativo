# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:21:29 2026

@author: mimib
"""

def  analizar_habitos(lista):
    """
    Recibe una lista de actividades y devuelve un diccionario con la cantidad de apariciones de cada una

    Parameters
    ----------
    lista : list/string
        Es una lista de palabras de actividades

    Returns
    -------
    diccionario : dic
        Diccionario con claves de actividades y valores de la cantidad de veces que aparece en la lista

    """
    diccionario= {}
    redesociales= 0
    estudiar = 0
    hacerejercicio = 0
    dormir= 0
    trabajar = 0 
    for actividades in lista:
        if actividades == "redes sociales":
            redesociales= redesociales + 1
        elif actividades == "estudiar":
            estudiar = estudiar + 1
        elif actividades == "hacer ejercicio":
            hacerejercicio = hacerejercicio + 1
        elif actividades == "dormir":
             dormir = dormir + 1
        elif actividades == "trabajar":
             trabajar= trabajar + 1
            
        diccionario["redes sociales"]= redesociales
        diccionario["estudiar"]= estudiar
        diccionario[" hacer ejercicio "]= hacerejercicio
        diccionario["dormir"]= dormir
        diccionario["trabajar"]= trabajar
        
    return diccionario
        
        
        