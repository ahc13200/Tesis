import cargar_varios_archivos as cargar_texto
import pre_procesamiento as pre_procesamiento
import buscar_similitud as agrupar_similitud
import exportar as exportar
import metricas as metricas


# -----------------Cargar documento
texto = cargar_texto.cargar_contenido()

# -----------------Pre-peocesamiento hasta el arbol de dependencias
requisitos_extraidos = pre_procesamiento.pre_proces(texto)

# ----------------- Exportar resultados
exportar.exportar_resultados(requisitos_extraidos)

# -----------------Metricas de calidad
#metricas.medidaf(requisitos_extraidos)

print("Esta listo todo")


