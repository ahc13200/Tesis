import spacy
import re
import json
import spacy
from spacy.matcher import Matcher


'''texto = "La Empresa RentaCar se dedica a la renta de autos a personas naturales que desean alquilar un automóvil. "
                   "Los clientes deben suministrar sus datos personales a la empresa y los servicios extra que necesita le proporcionen."
                   "A su vez deben informarles sobre los modelos y precios de los vehículos que tienen para la renta. Las universidades consideradas cobran tarifas elevadas.'''

def cargar_spacy(texto):
    nlp = spacy.load(r'C:\Users\Amanda\AppData\Local\Programs\Python\Python39\Lib\site-packages\es_core_news_lg\es_core_news_lg-3.2.0')
    #nlp = spacy.load("es_core_news_lg")
    doc = nlp(texto)

    return doc, nlp



# -------------------------------- PATRONES LEXICOS - SINTACTICOS ------------------------

# convertir las listas de palabras en listas de frases
def convertir(requisitos_extraidos):
    listas = []
    for requi in requisitos_extraidos:
        r = " ".join([str(_) for _ in requi])
        listas.append(r)
    return listas

def patrones_lexicos_sintacticos(texto):

    doc, nlp = cargar_spacy(texto)

    # Inicializar el matcher con el vocabulario compartido
    matcher = Matcher(nlp.vocab)

    # Annadir patron basado en regla al matcher
    '''p1 = [{"POS": "VERB"}, {"POS": "NOUN"}]
    p2 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}]
    p3 = [{"POS": "VERB"}, {"POS": "DET"}, {"POS": "NOUN"}]
    p4 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "NOUN"}]
    p5 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "DET"}, {"POS": "NOUN"}]
    p6 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "NOUN"}, {"POS": "ADJ"}]
    p7 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "NOUN"}]
    p8 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADP"}, {"POS": "NOUN"}]
    p9 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "DET"}, {"POS": "NOUN"}, {"POS": "ADJ"}]
    p10 = [{"POS": "VERB"}, {"POS": "ADJ"}, {"POS": "PRON"}, {"POS": "VERB"}, {"POS": "ADJ"}, {"POS": "DET"}, {"POS": "NOUN"}, {"POS": "ADJ"}]
    p11 = [{"POS": "VERB"}, {"POS": "ADJ"}, {"POS": "PRON"}, {"POS": "VERB"}, {"POS": "DET"}, {"POS": "NOUN"}, {"POS": "AUX"}]
    p12 = [{"POS": "VERB"}, {"POS": "CCONJ"}, {"POS": "VERB"}, {"POS": "DET"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "NOUN"}]
    p13 = [{"POS": "VERB"}, {"POS": "ADV"}, {"POS": "ADP"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "DET"}, {"POS": "NOUN"}, {"POS": "ADJ"}]
    p14 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "CCONJ"}, {"POS": "NOUN"}]
    p15 = [{"POS": "VERB"}, {"POS": "DET"}, {"POS": "NOUN"}, {"POS": "ADJ"}]
    p16 = [{"POS": "VERB"}, {"POS": "DET"}, {"POS": "NOUN"}, {"POS": "CCONJ"}, {"POS": "DET"}, {"POS": "NOUN"}]
    p17 = [{"POS": "VERB"}, {"POS": "ADP"}, {"POS": "NOUN"}]
    p18 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADP"}, {"POS": "NOUN"}, {"POS": "ADJ"}]
    p19 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADJ"}, {"POS": "ADP"}, {"POS": "DET"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "NOUN"}]
    p20 = [{"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "NOUN"}]


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
    matcher.add("10", [p10])
    matcher.add("11", [p11])
    matcher.add("12", [p12])
    matcher.add("13", [p13])
    matcher.add("14", [p14])
    matcher.add("15", [p15])
    matcher.add("15", [p16])
    matcher.add("15", [p17])
    matcher.add("15", [p18])
    matcher.add("15", [p19])
    matcher.add("15", [p20])'''

    # Annadir patrones desde un archivo externo
    patterns = open("patterns\\es_patterns.txt", 'r').read().split("\n")
    for i in range(len(patterns)):
        poss = patterns[i].split(" ")
        p = []
        for pos in poss:
            p.append({"POS": pos})
        matcher.add(str(i + 1), [p])

    # llamar al matcher sobre el doc
    matches = matcher(doc)

    # iterar sobre los resultados
    frases = []
    for match_id, start, end in matches:
        # obtener el span resultante
        matched_span = doc[start:end]
        frases.append(matched_span)
        # print(matched_span.text)

    # print(frases)

    requisitos = []
    for frase in frases:
        listaTokens = []
        for token in frase:
            if token.tag_ == "VERB":
                token = token.lemma_
            listaTokens.append(token)
        requisitos.append(listaTokens)

    requisitos_extraidos = convertir(requisitos)

    return requisitos_extraidos


# -------------------------------- ANALISIS DE DEPENDENCIAS ------------------------

#convertir las listas de palabras en listas de frases
def convertir(requisitos_extraidos):
    listas = []
    for requi in requisitos_extraidos:
        l = []
        if type(requi) == list:
            for i in requi:
                if type(i) == list:
                    r = " ".join([str(_) for _ in i])
                    l.append(r)
                else:
                    l.append(i)
        else:
            l.append(r)
        listas.append(l)
    return listas



def analisis_dependencias(texto):

    doc, nlp = cargar_spacy(texto)

    #separar las oraciones
    '''sentences = list(doc.sents)
    for sentence in sentences:
        print(sentence)
    
    #sacar la raiz de cada oracion, moyormente es el verbo
    for sentence in sentences:
        #print(sentence.root)'''

    #root_token = sentences[0].root
    frases = []
    sentences = list(doc.sents)
    for sentence in sentences:
        lista = []
        lista.append(sentence.root.text)
        for child in sentence.root.children:
            if child.dep_ == 'nsubj':
                subj = child
                subtree_subj = [t.text for t in subj.subtree]
                lista.append(subtree_subj)
            elif child.dep_ == 'obj':
                    obj = child
                    #subtree_obj = [t.text for t in obj.subtree]
                    lista.append(obj.text)
        frases.append(lista)

    requisitos_extraidos = convertir(frases)

    return requisitos_extraidos


#print(patrones_lexicos_sintacticos())


