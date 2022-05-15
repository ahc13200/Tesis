from difflib import SequenceMatcher as SM


######################## Buscar similitudes ###############################

def convertir(requisitos_extraidos):
    listas = []
    for requi in requisitos_extraidos:
        r = " ".join([str(_) for _ in requi])
        listas.append(r)
    return listas


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
    return lista


def similitudes(requisitos_extraidos):
    requisitos = convertir(requisitos_extraidos)
    l = refinamiento(requisitos)
    listaMayor = []
    indices_guardados = []
    for i in range(len(l)):
        filtro = []
        if i not in indices_guardados:
            for j in range(i+1, len(l)):
                valor = round(SM(None, l[i], l[j]).ratio(), 1)
                if valor >= 0.75 and j not in indices_guardados:
                    filtro.append(l[j])
                    indices_guardados.append(j)
            filtro.append(l[i])
            listaMayor.append(filtro)
    archivo = open('requisitos_agrupados_similares.txt', 'w')
    for linea in listaMayor:
        a = " ".join([str(_) + ", " for _ in linea])
        archivo.write(a + "\n")
    archivo.close()

#similitudes()