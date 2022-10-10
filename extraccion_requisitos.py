import cargar_varios_archivos as cargar_texto
import pre_procesamiento as pre_procesamiento
import exportar as exportar
import analisis_dependencias as anali_dependen
import metricas as metricas
import reduccion_redundancias as similitud


# -----------------Cargar documento
texto = cargar_texto.cargar_contenido()


if texto != "":
    # -----------------Pre-peocesamiento hasta el arbol de dependencias
    requisitos_extraidos = pre_procesamiento.pre_proces(texto)
    #requisitos_extraidos = anali_dependen.convertir(texto)

    # ----------------- Exportar resultados
    exportar.exportar_resultados(requisitos_extraidos)
    exportar.exportar_resultados_coseno(requisitos_extraidos)

    # -----------------Metricas de calidad
    #requi_coseno = similitud.similitud_coseno(requisitos_extraidos)
    #metricas.medidaf(requisitos_extraidos)

    print("Esta listo todo")

else:
    print("Debe escoger un archivo a procesar")


