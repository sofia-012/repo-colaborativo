import funcion_2 as f 

lista_actividades = f.registrar_habitos()
resumen = f.analizar_habitos(lista_actividades)

print("RESUMEN DE ACTIVIDADES DEL DÍA")
for actividad, cantidad in resumen.items():
    print(f"- {actividad}: {cantidad} veces")
