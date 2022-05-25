from difflib import SequenceMatcher as SM


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
    l = refinamiento(requisitos_extraidos)
    listaMayor = []
    indices_guardados = []
    for i in range(len(l)):
        filtro = []
        if i not in indices_guardados:
            for j in range(i+1, len(l)):
                valor = round(SM(None, l[i], l[j]).ratio(), 1)
                if valor >= 0.90 and j not in indices_guardados:
                    filtro.append(l[j])
                    indices_guardados.append(j)
            filtro.append(l[i])
            listaMayor.append(filtro)
    archivo = open('requisitos_agrupados_similares.txt', 'w')
    for linea in listaMayor:
        a = " ".join([str(_) + ", " for _ in linea])
        archivo.write(a + "\n")
    archivo.close()

#similitudes(requisitos_extraidos)