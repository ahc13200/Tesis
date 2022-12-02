

def exportar_resultados_sintactica(requisitos_extraidos):
    archivo = open('requisitos_agrupados_sintactica.txt', 'w')
    for linea in requisitos_extraidos:
        #a = " ".join([str(_) + ", " for _ in linea])
        archivo.write(str(linea) + "\n")
    archivo.close()

def exportar_resultados_semantica(requisitos_extraidos, promedio_calidad):
    archivo = open('requisitos_agrupados_semantica.txt', 'w')
    for linea in requisitos_extraidos:
        for l in linea:
            #a = " ".join([str(_) + ", " for _ in l])
            archivo.write(l + "\n")
        archivo.write("\n" + "\n")
    archivo.write(str(promedio_calidad))
    archivo.close()
