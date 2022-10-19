import cargar_varios_archivos as cargar_texto
import pre_procesamiento as pre_procesamiento
import extraccion_requisitos_candidatos as extraccion_requisitos_candidatos
import reduccion_redundancias as reduccion_redundancias
import exportar as exportar
import metricas as metricas

# -----------------Cargar documento
texto = cargar_texto.cargar_contenido()


if texto != "":
    # ----------------- Pre-peocesamiento ------------------------
    texto_procesado = pre_procesamiento.pre_proces(texto)

    # ----------------- Extraccion de requisitos candidatos -----------
    requisitos_extraidos = extraccion_requisitos_candidatos.patrones_lexicos_sintacticos(texto_procesado)
    #requisitos_extraidos = extraccion_requisitos_candidatos.analisis_dependencias(texto_procesado)

    # ----------------- Extraccion de requisitos candidatos -----------
    requisitos_extraidos_reducidos = reduccion_redundancias.similitudes(requisitos_extraidos)
    requisitos_extraidos_reducidos = reduccion_redundancias.similitud_coseno(requisitos_extraidos)

    # ----------------- Exportar resultados ------------------------
    exportar.exportar_resultados(requisitos_extraidos_reducidos)
    exportar.exportar_resultados_coseno(requisitos_extraidos_reducidos)

    # -----------------Metricas de calidad ------------------------
    #metricas.medidaf(requisitos_extraidos_reducidos)

    print("Requisitos candidatos extraídos satisfactoriamente")

else:
    print("Debe escoger un archivo a procesar")


