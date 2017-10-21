import codecs
import csv
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
        writer = open(os.getcwd() + '\\Archivos_guardados\\Normalizados\\' + str(candidato).replace('@', '').lower() + '.j', 'w')
        diccionario = json.load(file)
        diccionario_normalizado = {}
        print(diccionario)

        for id,valor in diccionario.items():
            # Normalizamos texto
            texto=re.sub(r'[á]', 'a', valor['Texto'].lower())
            texto1=re.sub(r'[é]', 'e', texto)
            texto2=re.sub(r'[í]', 'i', texto1)
            texto3=re.sub(r'[ó]', 'o', texto2)
            texto4=re.sub(r'[ú]', 'u', texto3)
            texto5=re.sub(r'[\S]+(.com|.org|.es|.net)[\S]*', 'URL', texto4)
            texto6=re.sub(r'\B@[\S]+', 'USER', texto5)
            texto7=re.sub(r'[\S]?(http:|https:).[\S]*', 'URL', texto6)
            diccionario_normalizado[id] = texto7

        json.dump(diccionario_normalizado,writer)



def normalizar_stop_words():
    file = codecs.open(os.getcwd() + '\\diccionarios\\STOP_WORDS', 'r', 'utf8')
    file_normalizado = open(os.getcwd() + '\\diccionarios\\STOP_WORDS_NORMALIZADO', 'w')

    for linea in file:
        print(linea)
        texto = re.sub(r'[á]', 'a', linea)
        texto1 = re.sub(r'[é]', 'e', texto)
        texto2 = re.sub(r'[í]', 'i', texto1)
        texto3 = re.sub(r'[ó]', 'o', texto2)
        texto4 = re.sub(r'[ú]', 'u', texto3)
        file_normalizado.writelines(texto4)

    file.close()
    file_normalizado.close()

def normalizar_diccionario_de_afecto():
    reader = csv.reader(codecs.open(os.getcwd() + '\\diccionarios\\SpanishDAL-v1.2\\meanAndStdev.csv', 'r', 'utf8'), delimiter = ';')
    writer = csv.writer(open(os.getcwd() + '\\diccionarios\\SpanishDAL-v1.2\\meanAndStdev_normalizado.csv', 'w', newline=''), delimiter = ';')
    for row in reader:
        texto = re.sub(r'[á]', 'a', row[0])
        texto1 = re.sub(r'[é]', 'e', texto)
        texto2 = re.sub(r'[í]', 'i', texto1)
        texto3 = re.sub(r'[ó]', 'o', texto2)
        texto4 = re.sub(r'[ú]', 'u', texto3)
        texto5 = re.sub(r'_[A-Z]', '', texto4)
        row[0] = texto5
        writer.writerow(row)


