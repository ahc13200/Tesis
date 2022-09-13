import spacy
import re

def analisis_depend(texto):
    ''' quitar mayusculas
    text_minusculas = texto.lower()

    #quitar aignos de puntuacion
    text_sin_signos = re.sub(r'[?|$|.|!|,|;]',r'',text_minusculas)'''

    #cargar libreria spaCy
    #nlp = spacy.load(r'C:\Users\Amanda\AppData\Local\Programs\Python\Python39\Lib\site-packages\es_core_news_sm\es_core_news_sm-3.2.0')
    nlp = spacy.load(r'C:\Users\Amanda\AppData\Local\Programs\Python\Python39\Lib\site-packages\es_core_news_lg\es_core_news_lg-3.2.0')
    doc = nlp(texto)

    oraciones = list(doc.sents)



    return oraciones
