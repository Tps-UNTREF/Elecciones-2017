import json
import os

from Main import *


class Procesamiento():
    def busqueda(self, almacenamiento):
        lista = ["@CFKArgentina", "@estebanbullrich", "@SergioMassa", "@RandazzoF", "@nestorpitrola",
                 "@JorgeTaiana", "@gladys_gonzalez", "@Stolbizer", "@andreadatri"]

        # Nos identificamos con twitter
        self.tw = Twitter(auth=OAuth(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

        contador_total_aux = 0
        while True:
            try:
                candidatos_OR = str(' OR ').join(lista)
                contador_aux = 0
                print('retardo 15 segundos...(Si tocas ctrl-c frena cuando termina este tiempo)')
                time.sleep(15)
                resultados = self.tw.search.tweets(q=candidatos_OR, result_type='recent', count=100)
                for tweet in resultados['statuses']:
                    id = str(tweet['id'])
                    text = tweet['text']
                    for candidato in lista:
                        if candidato in text:
                            if str(id) not in almacenamiento[candidato]:
                                print(ascii(tweet['id']))
                                print(ascii(tweet['text']))
                                almacenamiento[candidato][id] = {'Hora': resultados['statuses'][0]['created_at'],
                                                                 'Texto': text}
                                contador_aux += 1

                print('se obtuvieron ' + str(contador_aux) + ' tweets')
                contador_total_aux += contador_aux
            except (KeyboardInterrupt, EOFError):
                Persistencia.guardar(almacenamiento)
                print('Se encontraron ' + str(contador_total_aux) + ' Tweets en esta oportunidad.')
                break


    def total_tweets(self, almacenamiento):
        lista_candidatos = []
        contador = 0
        for candidato, tweets in almacenamiento.items():
            contador += len(tweets)
            lista_candidatos.append((len(tweets), candidato))
        return lista_candidatos


    def ranking_candidato_mas_mencionados(self):
        almacenamiento_a_procesar = Persistencia.cargar()
        aux = self.total_tweets(almacenamiento_a_procesar)
        aux.sort()

        file = open('ranking', 'w')
        contador = 0
        for x, y in aux:
            contador += x
            print('Candidato: ' + str(y) + ', Cantidad de tweets:  ' + str(x))
            file.write('Candidato: ' + str(y) + ', Cantidad de tweets:  ' + str(x) + '\n')
        print('Total: ' + str(contador))
        file.write('Total: ' + str(contador))
        file.close()

    def ranking_candidatos_mas_apreciados(self, diccionario_palabras):
        diccionario_afectos_normalizado = Persistencia.generar_diccionario_afectos_normalizados()
        diccionario_puntajes = {}
        for candidato, palabras in diccionario_palabras.items():  # Para cada candidato y cada palabra asociada al mismo
            puntaje_candidato = 0
            for palabra, cantidad in palabras.items():
                if palabra in diccionario_afectos_normalizado.keys():
                    puntaje_candidato += diccionario_afectos_normalizado[palabra] * cantidad
            diccionario_puntajes[candidato] = puntaje_candidato
        return diccionario_puntajes

    def leer_tweets(self):
        STOP_WORDS = Persistencia.cargar_STOP_WORDS()
        apariciones_palabras = {'@CFKArgentina': {}, '@estebanbullrich': {}, '@SergioMassa': {}, '@RandazzoF': {},'@nestorpitrola': {},'@JorgeTaiana': {}, '@gladys_gonzalez': {}, '@Stolbizer': {}, '@andreadatri': {}}
        for candidato in ["@CFKArgentina", "@estebanbullrich", "@SergioMassa", "@RandazzoF", "@nestorpitrola",
                     "@JorgeTaiana", "@gladys_gonzalez", "@Stolbizer", "@andreadatri"]:
            file = open(os.getcwd() + '\\Archivos_guardados\\Normalizados\\' + str(candidato).replace('@', '').lower() + '.j', 'r')
            diccionario_normalizado = json.load(file)
            for id,texto in diccionario_normalizado.items():
                for p in texto.split():
                    if len(p) >= 3 and p not in STOP_WORDS:
                        if p not in apariciones_palabras[candidato].keys():
                            apariciones_palabras[candidato][p] = 1
                        else:
                            apariciones_palabras[candidato][p] += 1
            file.close()

        return apariciones_palabras