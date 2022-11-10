import cargar_varios_archivos as cargar_texto
import pre_procesamiento as pre_procesamiento
import extraccion_requisitos_candidatos as extraccion_requisitos_candidatos
import reduccion_redundancias as reduccion_redundancias
import exportar as exportar
import metricas as metricas
import agrupamiento as agrupamiento

# -----------------Cargar documento
texto = cargar_texto.cargar_contenido()


if texto != "":
    # ----------------- Pre-peocesamiento ----------------------------------------------------------------------------------
    texto_procesado = pre_procesamiento.pre_proces(texto)

    # ----------------- Extraccion de requisitos candidatos ----------------------------------------------------------------
    requisitos_extraidos_PATRONES = extraccion_requisitos_candidatos.patrones_lexicos_sintacticos(texto_procesado)
    requisitos_extraidos_DEPENDENCIAS = extraccion_requisitos_candidatos.analisis_dependencias(texto_procesado)
    requisitos_extraidos_HIBRIDO = extraccion_requisitos_candidatos.metodo_hibrido(texto_procesado)

    # ----------------- Reduccion de redundancias --------------------------------------------------------------------------
    requisitos_extraidos_reducidos_PATRONES = reduccion_redundancias.similitudes_sintactica(requisitos_extraidos_PATRONES)
    requisitos_extraidos_reducidos_DEPENDENCIAS = reduccion_redundancias.similitudes_sintactica(requisitos_extraidos_DEPENDENCIAS)
    requisitos_extraidos_reducidos_HIBRIDO = reduccion_redundancias.similitudes_sintactica(requisitos_extraidos_HIBRIDO)

    # ----------------- Agrupamiento basado en la semantica ---------------------------------------------------------------
    requisitos_agrupados, promedio_calidad = agrupamiento.topic_identification(requisitos_extraidos_reducidos_PATRONES)

    # ----------------- Exportar resultados --------------------------------------------------------------------------------
    exportar.exportar_resultados_sintactica(requisitos_extraidos_reducidos_HIBRIDO)
    exportar.exportar_resultados_semantica(requisitos_agrupados, promedio_calidad)

    # -----------------Metricas de calidad ---------------------------------------------------------------------------------
    metricas.medidaf_patrones(requisitos_extraidos_reducidos_PATRONES)
    metricas.medidaf_dependencias(requisitos_extraidos_reducidos_DEPENDENCIAS)
    metricas.medidaf_hibrido(requisitos_extraidos_reducidos_HIBRIDO)

    print("Requisitos candidatos extraídos satisfactoriamente")

else:
    print("Debe escoger un archivo a procesar")


