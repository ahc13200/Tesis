import re
import Levenshtein
import reduccion_redundancias as similitud_sintactica

################## FORMULAS DE LAS METRICAS ######################

def requi_correctos():
    with open('requisitos.txt', 'r', encoding="utf8") as archivo:
        requisitos_correctos = [linea.strip() for linea in archivo]
    return requisitos_correctos

#print(requi_correctos())


def comparacion_correctos_con_extraidos (requisitos_extraidos):
    requisitos_correctos = requi_correctos()
    requisitos_extraidos_correctos = []
    for r in requisitos_extraidos:
        #a = " ".join([str(_) for _ in r])
        for requi in requisitos_correctos:
            valor = round(Levenshtein.ratio(r, requi), 1)
            '''vector1 = similitud_sintactica.text_to_vector(a)
            vector2 = similitud_sintactica.text_to_vector(requi)
            valor = round(similitud_sintactica.get_cosine(vector1, vector2), 1)'''
            if valor >= 0.60:
                requisitos_extraidos_correctos.append(r)
                break
    return requisitos_extraidos_correctos


def medidaf_patrones(requisitos_extraidos):
    requisitos_extraidos_correctos = comparacion_correctos_con_extraidos(requisitos_extraidos)
    requisitos_correctos = requi_correctos()

    precision = (len(requisitos_extraidos_correctos) / len(requisitos_extraidos))*100
    cobertura = (len(requisitos_extraidos_correctos) / len(requisitos_correctos))*100

    if cobertura > 0 and precision > 0:
        medida = 2 * ((precision * cobertura) / (precision + cobertura))
    else:
        medida = 0

    archivo = open('medidaF_PATRONES.txt', 'w')
    archivo.write('La precision es : ' + str(precision) + "\n"
                'La cobertura es: ' + str(cobertura) + "\n"
                'La medida-F es: ' + str(medida))
    archivo.close()


def medidaf_dependencias(requisitos_extraidos):
    requisitos_extraidos_correctos = comparacion_correctos_con_extraidos(requisitos_extraidos)
    requisitos_correctos = requi_correctos()

    precision = (len(requisitos_extraidos_correctos) / len(requisitos_extraidos))*100
    cobertura = (len(requisitos_extraidos_correctos) / len(requisitos_correctos))*100

    if cobertura > 0 and precision > 0:
        medida = 2 * ((precision * cobertura) / (precision + cobertura))
    else:
        medida = 0

    archivo = open('medidaF_DEPENDENCIAS.txt', 'w')
    archivo.write('La precision es : ' + str(precision) + "\n"
                'La cobertura es: ' + str(cobertura) + "\n"
                'La medida-F es: ' + str(medida))
    archivo.close()


def medidaf_hibrido(requisitos_extraidos):
    requisitos_extraidos_correctos = comparacion_correctos_con_extraidos(requisitos_extraidos)
    requisitos_correctos = requi_correctos()

    precision = (len(requisitos_extraidos_correctos) / len(requisitos_extraidos))*100
    cobertura = (len(requisitos_extraidos_correctos) / len(requisitos_correctos))*100

    if cobertura > 0 and precision > 0:
        medida = 2 * ((precision * cobertura) / (precision + cobertura))
    else:
        medida = 0

    archivo = open('medidaF_HIBRIDO.txt', 'w')
    archivo.write('La precision es : ' + str(precision) + "\n"
                'La cobertura es: ' + str(cobertura) + "\n"
                'La medida-F es: ' + str(medida))
    archivo.close()