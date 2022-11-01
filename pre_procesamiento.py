import re
import extraccion_requisitos_candidatos

def pre_proces(texto):
    #quitar mayusculas
    text_minusculas = texto.lower()

    #quitar signos de puntuacion
    text_sin_signos = re.sub(r'[?|$|:|!|¿]',r'',text_minusculas)

    doc, nlp = extraccion_requisitos_candidatos.cargar_spacy(text_sin_signos)

    # fragmentar el texto en oraciones
    lista = []
    for sentence in doc.sents:
        lista.append(sentence)
    #print(len(lista))

    texto_procesado = " ".join([str(_) for _ in lista])

    return texto_procesado
