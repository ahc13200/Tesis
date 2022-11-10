from difflib import SequenceMatcher as SM
import sklearn
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import scale
import re, math
from collections import Counter
from hermetrics.levenshtein import Levenshtein



######################## Buscar similitudes ###############################

#Esto es para probar el modulo independiente
'''requisitos_extraidos = [['realizar', 'las', 'pruebas'], ['realizar', 'las', 'pruebas', 'químicas'], ['realizar', 'las', 'pruebas', 'químicas', 'ahi'], ['entregar', 'los', 'resultados'], ['tratar', 'una', 'enfermedad'], ['definir', 'las', 'indicaciones'], ['definir', 'las', 'indicaciones', 'médicas'], ['tomar', 'presión'], ['medir', 'la', 'temperatura'], ['evaluar', 'los', 'resultados'], ['hacer', 'el', 'laboratorio'], ['definir', 'las', 'indicaciones'], ['definir', 'las', 'indicaciones', 'médicas'],
                        ['indicar', 'las', 'pruebas'], ['indicar', 'las', 'pruebas', 'químicas'], ['definir', 'el', 'tratamiento'], ['recetar', 'medicamentos'], ['definir', 'las', 'indicaciones'], ['definir', 'las', 'indicaciones', 'médicas'], ['consultar', 'la', 'historia'], ['consultar', 'la', 'historia', 'clínica'], ['realizar', 'las', 'pruebas'], ['realizar', 'las', 'pruebas', 'clínicas'], ['examinar', 'las', 'muestras'], ['recoger', 'las', 'muestras'], ['realizar', 'los', 'exámenes'],
                        ['recoger', 'las', 'muestras'], ['extraer', 'muestras'], ['realizar', 'los', 'exámenes'], ['realizar', 'los', 'exámenes', 'siguientes']]
requisitos_extraidos = [['calcular', 'sus', 'niveles'], ['calcular', 'el', 'nivel'], ['amanda', 'y', 'thalia'], ['calcular', 'estos', 'niveles']]'''

# convertir las listas de palabras en listas de frases
def convertir(requisitos_extraidos):
    listas = []
    for requi in requisitos_extraidos:
        r = " ".join([str(_) for _ in requi])
        listas.append(r)
    return listas


#si requisito chico esta dentro de requisito grande
def reduccion(requisitos_extraidos):
    requisitos = convertir(requisitos_extraidos)
    lista = []
    for i in range(len(requisitos)):
        aux = []
        for j in range(i+1, len(requisitos)):
            if requisitos[i] in requisitos[j]:
                aux.append(requisitos[j])
        if aux and aux[-1] not in lista:
            lista.append(aux[-1])
        else:
            repetidos = False
            for k in lista:
                if requisitos[i] in k:
                    repetidos = True
                    break
            if not repetidos:
                lista.append(requisitos[i])
    return lista

# ---------------------------------- SIMILITUD SINTACTICA ------------------------------------------

#buscar similitud sintactica por Levenshtein
def similitudes_sintactica(requisitos_extraidos):
    lev = Levenshtein()
    l = reduccion(requisitos_extraidos)
    filtro = []
    for i in range(len(l)):
            for j in range(i+1, len(l)):
                valor = round(lev.similarity(l[i], l[j]), 1)
                if valor < 0.60 and l[j] not in filtro:
                    filtro.append(l[j])
                elif l[i] not in filtro:
                    filtro.append(l[i])
    return filtro

'''def similitudes_sintactica(requisitos_extraidos):
    lev = Levenshtein()
    l = reduccion(requisitos_extraidos)
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
    return listaMayor'''


#metrica similitud coseno
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


#buscar similitud sintactica por Coseno
def similitud_coseno (requisitos_extraidos):
    l = reduccion(requisitos_extraidos)
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