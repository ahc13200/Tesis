import spacy
import re
import json



#extraccion de requisitos por analisis de dependencias
def analisis_depend(texto):

    #cargar libreria spaCy
    #nlp = spacy.load(r'C:\Users\Amanda\AppData\Local\Programs\Python\Python39\Lib\site-packages\es_core_news_sm\es_core_news_sm-3.2.0')
    nlp = spacy.load(r'C:\Users\Amanda\AppData\Local\Programs\Python\Python39\Lib\site-packages\es_core_news_lg\es_core_news_lg-3.2.0')

    '''doc = nlp("La Empresa RentaCar se dedica a la renta de autos a personas naturales que desean alquilar un automóvil. "
                  "Los clientes deben suministrar sus datos personales a la empresa y los servicios extra que necesita le proporcionen."
                  "A su vez deben informarles sobre los modelos y precios de los vehículos que tienen para la renta. Las universidades consideradas cobran tarifas elevadas.")'''
    doc = nlp(texto)


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
    return frases


#convertir las listas de palabras en listas de frases
def convertir(texto):
    requisitos_extraidos = analisis_depend(texto)
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


#print(convertir())


