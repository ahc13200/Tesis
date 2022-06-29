import buscar_similitud as buscar


def exportar_resultados(requisitos_extraidos):
    lista = buscar.similitudes(requisitos_extraidos)
    archivo = open('requisitos_agrupados_similares.txt', 'w')
    for linea in lista:
        a = " ".join([str(_) + ", " for _ in linea])
        archivo.write(a + "\n")
    archivo.close()
