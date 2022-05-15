import spacy
import re
import docx2txt
from spacy.matcher import Matcher
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
from PyPDF2 import PdfFileReader


def cargar_contenido():
    Tk().withdraw()
    ruta = askopenfilename() # aqui muestras un dialogo para seleccionar el archivo y retorna la ruta
    #print(ruta)

    raiz, extension = os.path.splitext(ruta)

    if extension == ".docx":
        contenido = docx2txt.process(ruta)
        #print(contenido)

    else:
        if extension == ".pdf":
            temp = open(ruta, 'rb')
            pdf = PdfFileReader(temp)
            number_of_pages = pdf.getNumPages()
            page = pdf.getPage(0)
            contenido = page.extractText()
            #print(contenido)

        else:
            if extension == ".txt":
                with open(ruta, 'r') as archivo:
                    contenido = archivo.read()
                #print(contenido)


    return contenido

texto = cargar_contenido()


#quitar mayusculas
text_minusculas = texto.lower()

#quitar aignos de puntuacion
text_sin_signos = re.sub(r'[?|$|.|!|,|;]',r'',text_minusculas)

nlp = spacy.load(r'C:\Users\Amanda\AppData\Local\Programs\Python\Python39\Lib\site-packages\es_core_news_lg\es_core_news_lg-3.2.0')
doc = nlp(text_sin_signos)


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

agrupados = []
for x in requisitos_extraidos:
    a = " ".join([str(_) for _ in x])
    #print(a)
    agrupados.append(a)

def refinamiento(agrupados):
    lista = []

    for i in range(len(agrupados)):
        repetido = False
        for j in range(i + 1, len(agrupados)):
            if agrupados[i] in agrupados[j]:
                lista.append(agrupados[j])
                repetido = True
        if repetido == False and agrupados[i] not in lista:
            lista.append(agrupados[i])

    print(lista)

refinamiento(agrupados)




