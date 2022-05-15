import spacy
from spacy import displacy
import re
from spacy.matcher import Matcher


def pre_proces(texto):
    #quitar mayusculas
    text_minusculas = texto.lower()

    #quitar aignos de puntuacion
    text_sin_signos = re.sub(r'[?|$|.|!|,|;]',r'',text_minusculas)

    #cargar libreria spaCy
    #nlp = spacy.load(r'C:\Users\Amanda\AppData\Local\Programs\Python\Python39\Lib\site-packages\es_core_news_sm\es_core_news_sm-3.2.0')
    nlp = spacy.load(r'C:\Users\Amanda\AppData\Local\Programs\Python\Python39\Lib\site-packages\es_core_news_lg\es_core_news_lg-3.2.0')
    doc = nlp(text_sin_signos)

    # Tokenizar con Spacy
    tokens = [token for token in doc]

    # Etiquetar y Lematizar
    etiquetado = []
    for token in doc:
        etiquetado.append((token.text, token.tag_, token.lemma_))

    #Chunking
    for token in doc:
        print("{0}/{1} <-- {2} <-- {3}/{4}".format(
            token.text, token.tag_, token.dep_, token.head.text, token.head.tag_
        ))

    displacy.render(doc, style='dep', jupyter=True)


    #--------- PATRONES BASADOS EN REGLAS ---------------

    #Inicializar el matcher con el vocabulario compartido
    matcher = Matcher(nlp.vocab)

    #Annadir patron basado en regla al matcher
    p1 = [{"POS": "VERB"}, {"POS": "NOUN"}]
    p2 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "NOUN"}]
    p3 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}]
    p4 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "DET"}, {"POS": "NOUN"}]
    p5 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "NOUN"}, {"POS": "ADJ"}]
    p6 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "NOUN"}]
    p7 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADP"}, {"POS": "NOUN"}]
    p8 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "DET"}, {"POS": "NOUN"}, {"POS": "ADJ"}]
    p9 = [{"POS": "VERB"}, {"POS": "DET"}, {"POS": "NOUN"}]


    #            ID del patron  nomb del patron
    matcher.add("1", [p1])
    matcher.add("2", [p2])
    matcher.add("3", [p3])
    matcher.add("4", [p4])
    matcher.add("5", [p5])
    matcher.add("6", [p6])
    matcher.add("7", [p7])
    matcher.add("8", [p8])
    matcher.add("9", [p9])



    #llamar al matcher sobre el doc
    matches = matcher(doc)

    #iterar sobre los resultados
    frases = []
    for match_id, start, end in matches:
        #obtener el span resultante
        matched_span = doc[start:end]
        frases.append(matched_span)
        #print(matched_span.text)

    #print(frases)

    requisitos_extraidos = []
    for frase in frases:
        listaTokens = []
        for token in frase:
            if token.tag_ == "VERB":
                token = token.lemma_
            listaTokens.append(token)
        requisitos_extraidos.append(listaTokens)

    return requisitos_extraidos
