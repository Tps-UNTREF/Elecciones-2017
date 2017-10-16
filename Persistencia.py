import json
import os
import re


def cargar():
    almacenamiento = {'@CFKArgentina': {}, '@estebanbullrich': {}, '@SergioMassa': {}, '@RandazzoF': {},'@nestorpitrola': {},'@JorgeTaiana': {}, '@gladys_gonzalez': {}, '@Stolbizer': {}, '@andreadatri': {}}
    for candidato in ["@CFKArgentina", "@estebanbullrich" , "@SergioMassa" , "@RandazzoF" , "@nestorpitrola", "@JorgeTaiana" , "@gladys_gonzalez" , "@Stolbizer" , "@andreadatri"] :
        file = open(os.getcwd() + '\\Archivos_guardados\\' + str(candidato).replace('@', '').lower() + '.j', 'r')
        lista = json.load(file)
        for id,fecha_texto in lista.items():
                almacenamiento[candidato][id] = fecha_texto
        file.close()
    return almacenamiento

def guardar(almacenamiento):
    for candidato, dic_ids in almacenamiento.items():
        diccionario = dic_ids
        file = open(os.getcwd() + '\\Archivos_guardados\\' + str(candidato).replace('@', '').lower() + '.j', 'w')
        json.dump(diccionario, file)
        file.close()

def normalizar_tweets():

    for candidato in ["@CFKArgentina", "@estebanbullrich", "@SergioMassa", "@RandazzoF", "@nestorpitrola",
                      "@JorgeTaiana", "@gladys_gonzalez", "@Stolbizer", "@andreadatri"]:

        file = open(os.getcwd() + '\\Archivos_guardados\\' + str(candidato).replace('@', '').lower() + '.j', 'r')
        diccionario = json.load(file)
        print(diccionario)

        for id,valor  in diccionario.items():
            # Normalizamos texto
            texto=re.sub(r'[á]', 'a', valor['Texto'].lower())
            texto1=re.sub(r'[é]', 'e', texto)
            texto2=re.sub(r'[í]', 'i', texto1)
            texto3=re.sub(r'[ó]', 'o', texto2)
            texto4=re.sub(r'[ú]', 'u', texto3)
            texto5=re.sub(r'[\S]+(.com|.org|.es|.net)[\S]*', 'URL', texto4)
            texto6=re.sub(r'\B@[\S]+', 'USER', texto5)
            texto7=re.sub(r'[\S]?(http:|https:).[\S]*', 'URL', texto6)
            diccionario['Texto'] = texto7

def normalizar_stop_words():
    file = open(os.getcwd() + '\\diccionarios\\STOP_WORDS.txt', 'r')
    file_normalizado = open(os.getcwd() + '\\diccionarios\\STOP_WORDS_NORMALIZADO', 'w')

    for linea in file:
        texto = re.sub(r'[á]', 'a', linea)
        texto1 = re.sub(r'[é]', 'e', texto)
        texto2 = re.sub(r'[í]', 'i', texto1)
        texto3 = re.sub(r'[ó]', 'o', texto2)
        texto4 = re.sub(r'[ú]', 'u', texto3)
        file_normalizado.writelines(texto4)

    file.close()
    file_normalizado.close()

almacen=cargar()
normalizar_stop_words()
