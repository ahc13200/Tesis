

################## FORMULAS DE LAS METRICAS ######################

def requi_correctos():
    with open('requisitos.txt', 'r', encoding="utf8") as archivo:
        requisitos_correctos = [linea.strip() for linea in archivo]
    return requisitos_correctos

print(requi_correctos())


def requi_extraidos (requisitos_extraidos):
    requisitos_correctos = requi_correctos()
    requisitos_extraidos_correctos = []
    for r in requisitos_correctos:
        for requi in requisitos_extraidos:
            a = " ".join([str(_) for _ in requi])
            if r == a:
                requisitos_extraidos_correctos.append(a)

    return requisitos_extraidos_correctos


def medidaf(requisitos_extraidos):
    requisitos_extraidos_correctos = requi_extraidos(requisitos_extraidos)
    requisitos_correctos = requi_correctos()

    presicion = (len(requisitos_extraidos_correctos) / len(requisitos_extraidos))*100
    cobertura = (len(requisitos_extraidos_correctos) / len(requisitos_correctos))*100
    medida = 2 * ((presicion * cobertura) / (presicion + cobertura))

    archivo = open('medidaF.txt', 'w')
    archivo.write('La medida-F es : ' + str(medida))
    archivo.close()


#medidaf(requisitos_extraidos, requisitos_correctos)