import spacy

#cargar libreria spaCy
nlp = spacy.load(r'C:\Users\Amanda\AppData\Local\Programs\Python\Python39\Lib\site-packages\es_core_news_sm\es_core_news_sm-3.2.0')
doc = nlp("Las universidades consideradas cobran tarifas elevadas")


dependencias = [{}]

def obtener_dependencias():
    dependencias = [{}]
    for tokens in doc:
        if tokens.tag_ == "VERB":
            for child in tokens.children:
                dependencias.append({child.text: child.tag_})
    print(dependencias)

obtener_dependencias()
