import reduccion_redundancias as buscar


def exportar_resultados(requisitos_extraidos):
    lista = buscar.similitudes(requisitos_extraidos)
    archivo = open('requisitos_agrupados_similares.txt', 'w')
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