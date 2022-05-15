

################## FORMULAS DE LAS METRICAS ######################



def medidaf(requisitos_extraidos):
    with open('requisitos.txt', 'r') as archivo:
        requisitos_correctos = [linea.strip() for linea in archivo]
    requisitos_extraidos_correctos = []
    for r in requisitos_correctos:
        for requi in requisitos_extraidos:
            a = " ".join([str(_) for _ in requi])
            if r == a:
                requisitos_extraidos_correctos.append(a)

    presicion = (len(requisitos_extraidos_correctos) / len(requisitos_extraidos))*100
    cobertura = (len(requisitos_extraidos_correctos) / len(requisitos_correctos))*100
    medida = 2 * ((presicion * cobertura) / (presicion + cobertura))

    archivo = open('medidaF.txt', 'w')
    archivo.write('La medida-F es : ' + str(medida))
    archivo.close()


#medidaf(requisitos_extraidos, requisitos_correctos)