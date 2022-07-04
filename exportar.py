import reduccion_redundancias as buscar


def exportar_resultados(requisitos_extraidos):
    lista, promedio = buscar.similitudes(requisitos_extraidos)
    archivo = open('requisitos_agrupados_similares.txt', 'w')
    prom = open('promedio_similitud.txt', 'w')
    prom.write(str(promedio))
    prom.close()
    for linea in lista:
        a = " ".join([str(_) + ", " for _ in linea])
        archivo.write(a + "\n")
    archivo.close()

def exportar_resultados_coseno(requisitos_extraidos):
    lista = buscar.similitud_coseno(requisitos_extraidos)
    archivo = open('requisitos_agrupados_similares_coseno.txt', 'w')
    for linea in lista:
        a = " ".join([str(_) + ", " for _ in linea])
        archivo.write(a + "\n")
    archivo.close()