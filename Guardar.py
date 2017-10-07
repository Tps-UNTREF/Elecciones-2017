import json
import os
from Main import Main
def cargar():
    diccionario = {}
    for candidato in ["@CFKArgentina", "@estebanbullrich" , "@SergioMassa" , "@RandazzoF" , "@nestorpitrola", "@JorgeTaiana" , "@gladys_gonzalez" , "@Stolbizer" , "@andreadatri"] :
        diccionario[candidato] = {}
        file = open(os.getcwd() + '\\' + str(candidato).replace('@', '').lower() + '.j', 'r')
        lista = json.load(file)
        for id in lista:
            for hora_texto in id:

                diccionario[candidato][id] = tweet
        file.close()
    return diccionario
def guardar(dicc):
    for candidato, tweets in dicc.items():
        file = open(os.getcwd() + '\\' + str(candidato).replace('@', '').lower() + '.j', 'w')
        lista = []
        for tweet in tweets.values():
            lista.append(tweet)
        json.dump(lista, file)
        file.close()