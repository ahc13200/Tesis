import docx2txt
from tkinter import Tk
# from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import os
from PyPDF2 import PdfFileReader


#cargar documento
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

#texto = cargar_contenido()

#print(texto)
