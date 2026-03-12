#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def registrar_habitos(actividad):
    """
    Esta función recibe distintas actividades ingresadas por el usuario, con un ciclo while que le pregunta 
    al usuario si ya terminó de ingresar o decide agregar más actividades. Luego, guarda las actividades en una lista y las devuelve.
    

    Parameters
    ----------
    actividad : Actividades realizadas durante el día por el usuario

    Returns
    -------
    actividades : Lista de actividades

    """
  
    actividades= []
    input("Ingrese una actividad que realizó durante el día: ")
    decision = input("¿Desea agregar mas actividades?: ")
    actividades.append(decision)
    while decision == "Si":
        actividades.append(decision)
        decision= input("Ingrese una actividad que realizó durante el día: ")
    return actividades         
        
    