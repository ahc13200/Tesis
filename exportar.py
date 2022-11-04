import reduccion_redundancias as buscar


def exportar_resultados_sintactica(requisitos_extraidos):
    archivo = open('requisitos_agrupados_sintactica.txt', 'w')
    for linea in requisitos_extraidos:
        #a = " ".join([str(_) + ", " for _ in linea])
        archivo.write(str(linea) + "\n")
    archivo.close()

def exportar_resultados_semantica(requisitos_extraidos):
    archivo = open('requisitos_agrupados_semantica.txt', 'w')
    for linea in requisitos_extraidos:
        a = " ".join([str(_) + ", " for _ in linea])
        archivo.write(a + "\n")
    archivo.close()