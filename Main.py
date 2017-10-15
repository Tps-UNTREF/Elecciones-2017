import time

from twitter import *

import Persistencia
from config import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_SECRET, CONSUMER_KEY


class Main():

    def __init__(self):
        # Nos identificamos con twitter
        self.tw = Twitter(auth=OAuth(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
        self.candidatos = ["@CFKArgentina", "@estebanbullrich", "@SergioMassa", "@RandazzoF", "@nestorpitrola",
                           "@JorgeTaiana", "@gladys_gonzalez", "@Stolbizer", "@andreadatri"]
        almacenamiento = Persistencia.cargar()
        self.busqueda(self.candidatos, almacenamiento)

    def busqueda(self, lista, almacenamiento):
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
            except (KeyboardInterrupt, EOFError):
                Persistencia.guardar(almacenamiento)
                self.total_tweets(almacenamiento)
                break
    @staticmethod
    def total_tweets(almacenamiento):
        lista_candidatos=[]
        contador = 0
        for candidato, tweets in almacenamiento.items():
            print(candidato, ': ', len(tweets))
            contador += len(tweets)
            lista_candidatos.append((len(tweets),candidato))
        print('Total: ', contador)
        return lista_candidatos





if __name__ == '__main__':
    Main()