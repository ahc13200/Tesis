from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from nltk.corpus import wordnet
import numpy
from hermetrics.levenshtein import Levenshtein

'''phrases = ['de formas', 'el servicio', 'por correo', 'en cuenta', 'una estandarización', 'otra vía', 'sus certificados',
'una falta', 'una falta de información y orientación al público de los pasos a seguir para realizar los trámites que requieren',
'los documentos', 'los trámites', 'a cabo', 'la información', 'reporte de estadísticas', 'esta funcionalidad', 'un servicio',
'los registros', 'en consideración', 'internet', 'la posibilidad', 'solicitudes por esta vía']

phrases = ['una solicitud', 'el carné', 'disponibilidad del libro', 'la solicitud', 'al estudiante',
'las condiciones descritas', 'la cantidad', 'el libro', 'el comprobante','el préstamo',
'al estudiante', 'un libro', 'un comprobante', 'con ejemplares', 'un comprobante',
'los libros', 'la existencia', 'el libro', 'el libro', 'el comprobante',
'el catálogo', 'al estudiante', 'la solicitud', 'la aplicación', 'el cumplimiento',
'él el libro', 'el libro']'''


# Devuelve una lista con los objetos etiquetados con el id de cluster

def perform_clustering(phrases):
    print("Filling distance matrix...")
    results = fill_distance_matrix(phrases)
    distance_matrix = results[0]
    threshold = results[1]
    clusters = []

    clusters = perform_hac(distance_matrix, threshold)

    # Calcular la métrica silhouette
    unique_labels = set(clusters)
    if len(unique_labels) > 1:
        silhouette_avg = silhouette_score(distance_matrix, clusters)
    else:
        silhouette_avg = 1

    return clusters, silhouette_avg


def perform_hac(matrix, threshold):
    clusters = AgglomerativeClustering(affinity='precomputed', distance_threshold=threshold, n_clusters=None,
                                       linkage="average")
    clusters.fit_predict(matrix)
    return clusters.labels_


def fill_distance_matrix(phrases):
    lev = Levenshtein()
    matrix = numpy.zeros(shape=(len(phrases), len(phrases)))
    total_dist = 0.0
    pairs = 0
    for i in range(0, len(phrases) - 1):
        phrase1 = phrases[i]
        row = []
        for j in range(i + 1, len(phrases)):
            phrase2 = phrases[j]
            #sin = lev.similarity(phrase1, phrase2)
            sem = semantic(phrase1, phrase2)
            valor = 1 - sem
            total_dist += valor
            pairs += 1
            matrix[i][j] = round(valor, 2)
            # print(str(i) + "--" + str(j))

    threshold = round((total_dist / pairs), 2)
    return matrix, threshold


def semantic(phrase1, phrase2):
    total_sem = 0.0
    cant = 0.0
    phr1 = phrase1.split(" ")
    phr2 = phrase2.split(" ")

    for word1 in phr1:
        synsets1 = wordnet.synsets(word1)
        if len(synsets1) > 0:
            syn1 = synsets1[0]
            for word2 in phr2:
                synsets2 = wordnet.synsets(word2)
                if len(synsets2) > 0:
                    syn2 = synsets2[0]
                    if syn1.name().split(".")[1] == syn2.name().split(".")[1]:
                        total_sem += syn1.wup_similarity(syn2)
                        cant += 1

    if cant == 0.0:
        return 0.0
    return total_sem / cant


# A paritr de la lista de etiquetas crer los clusters

def topic_identification(phrases):
    topics = []
    perform_clust = perform_clustering(phrases)
    clusters = perform_clust[0]
    silhouette_score = perform_clust[1]
    dict = {}
    alone = 1
    for i in range(0, len(clusters)):
        if clusters[i] is None:
            key = "alone" + str(alone)
            dict.update({key: [phrases[i]]})
            alone += 1
        else:
            key = clusters[i]
            if key in dict:
                value = dict[key]
                value.append(phrases[i])
                dict.update({key: value})
            else:
                value = [phrases[i]]
                dict.update({key: value})

    for cluster in dict.values():
        topics.append(cluster)
    return topics, silhouette_score

#print(topic_identification(phrases))