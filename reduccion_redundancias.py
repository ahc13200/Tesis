from difflib import SequenceMatcher as SM
import sklearn
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import scale
import re, math
from collections import Counter
from hermetrics.levenshtein import Levenshtein



######################## Buscar similitudes ###############################


'''requisitos_extraidos = [['realizar', 'las', 'pruebas'], ['realizar', 'las', 'pruebas', 'químicas'], ['realizar', 'las', 'pruebas', 'químicas', 'ahi'], ['entregar', 'los', 'resultados'], ['tratar', 'una', 'enfermedad'], ['definir', 'las', 'indicaciones'], ['definir', 'las', 'indicaciones', 'médicas'], ['tomar', 'presión'], ['medir', 'la', 'temperatura'], ['evaluar', 'los', 'resultados'], ['hacer', 'el', 'laboratorio'], ['definir', 'las', 'indicaciones'], ['definir', 'las', 'indicaciones', 'médicas'],
                        ['indicar', 'las', 'pruebas'], ['indicar', 'las', 'pruebas', 'químicas'], ['definir', 'el', 'tratamiento'], ['recetar', 'medicamentos'], ['definir', 'las', 'indicaciones'], ['definir', 'las', 'indicaciones', 'médicas'], ['consultar', 'la', 'historia'], ['consultar', 'la', 'historia', 'clínica'], ['realizar', 'las', 'pruebas'], ['realizar', 'las', 'pruebas', 'clínicas'], ['examinar', 'las', 'muestras'], ['recoger', 'las', 'muestras'], ['realizar', 'los', 'exámenes'],
                        ['recoger', 'las', 'muestras'], ['extraer', 'muestras'], ['realizar', 'los', 'exámenes'], ['realizar', 'los', 'exámenes', 'siguientes']]'''

def convertir(requisitos_extraidos):
    listas = []
    for requi in requisitos_extraidos:
        r = " ".join([str(_) for _ in requi])
        listas.append(r)
    return listas

#print(convertir(requisitos_extraidos))



def refinamiento(requisitos_extraidos):
    lista = []
    requisitos = convertir(requisitos_extraidos)
    for i in range(len(requisitos)):
        repetido = False
        for j in range(i + 1, len(requisitos)):
            if requisitos[i] in requisitos[j] and requisitos[j] not in lista:
                lista.append(requisitos[j])
                repetido = True
                break
        if repetido == False and requisitos[i] not in lista:
            lista.append(requisitos[i])
    return lista

#print(refinamiento(requisitos_extraidos))

def similitudes(requisitos_extraidos):
    lev = Levenshtein()
    l = refinamiento(requisitos_extraidos)
    listaMayor = []
    indices_guardados = []
    for i in range(len(l)):
        filtro = []
        if i not in indices_guardados:
            for j in range(i+1, len(l)):
                valor = round(lev.similarity(l[i], l[j]), 1)
                if valor >= 0.90 and j not in indices_guardados:
                    filtro.append(l[j])
                    indices_guardados.append(j)
            filtro.append(l[i])
            listaMayor.append(filtro)
    return listaMayor

#similitudes(requisitos_extraidos)

def algoritmo_agrupamiento_jerarquico(requisitos_extraidos):
    l = refinamiento(requisitos_extraidos)
    #X_scaled = scale(refinamiento(requisitos_extraidos))
    modelo_hclust_ward = AgglomerativeClustering(
                                affinity = 'euclidean',
                                linkage  = 'ward',
                                distance_threshold = 0,
                                n_clusters         = None
                         )
    modelo_hclust_ward.fit(X=l)

#AgglomerativeClustering(distance_threshold=0, n_clusters=None)


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    WORD = re.compile(r'\w+')
    words = WORD.findall(text)
    return Counter(words)

def similitud_coseno (requisitos_extraidos):
    l = refinamiento(requisitos_extraidos)
    listaMayor = []
    indices_guardados = []
    for i in range(len(l)):
        filtro = []
        if i not in indices_guardados:
            for j in range(i + 1, len(l)):
                vector1 = text_to_vector(l[i])
                vector2 = text_to_vector(l[j])
                cosine = round(get_cosine(vector1, vector2), 1)
                if cosine >= 0.90 and j not in indices_guardados:
                    filtro.append(l[j])
                    indices_guardados.append(j)
            filtro.append(l[i])
            listaMayor.append(filtro)
    return listaMayor



