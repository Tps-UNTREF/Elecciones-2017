import json
import os




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


