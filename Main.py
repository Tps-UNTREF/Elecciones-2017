import time

from twitter import *

import Persistencia
from config import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_SECRET, CONSUMER_KEY

class Main():



    def __init__(self):
        # Nos identificamos con twitter
        self.tw = Twitter(auth = OAuth(ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET))
        self.candidatos=["@CFKArgentina", "@estebanbullrich" , "@SergioMassa" , "@RandazzoF" , "@nestorpitrola", "@JorgeTaiana" , "@gladys_gonzalez" , "@Stolbizer" , "@andreadatri"]
        almacenamiento = almacenamiento = {'@CFKArgentina': {}, '@estebanbullrich': {}, '@SergioMassa': {}, '@RandazzoF': {},'@nestorpitrola': {},'@JorgeTaiana': {}, '@gladys_gonzalez': {}, '@Stolbizer': {}, '@andreadatri': {}}
        self.busqueda(self.candidatos,almacenamiento)



    #RECOMPILO TWEETS Y LOS ALMACENO
    def busqueda(self,lista,almacenamiento):

        candidatos_OR = str(' OR ').join(lista)

        contador = 0

        resultados = self.tw.search.tweets(q=candidatos_OR, result_type='recent', count=100)
        ultimo_id = resultados['statuses'][0]['id']
        for tweet in resultados['statuses']:
            print(ascii(tweet['id']))
            id = tweet['id']
            print(ascii(tweet['text']))
            text = tweet['text']
            for candidato in lista:
                if candidato in text:
                    if id not in almacenamiento[candidato]:
                        almacenamiento[candidato][id] = {'Hora': resultados['statuses'][0]['created_at'], 'Texto': text}
                        contador += 1



        for x in range(0,3):
            time.sleep(15)
            resultados = self.tw.search.tweets(q=candidatos_OR,result_type='recent',count=1, since_id= ultimo_id)
            if resultados['statuses'] !=[]:
                ultimo_id = resultados['statuses'][0]['id']
                for tweet in resultados['statuses']:
                    print(ascii(tweet['id']))
                    id = tweet['id']
                    print(ascii(tweet['text']))
                    text = tweet['text']
                    for candidato in lista:
                        if candidato in text:
                            if id not in almacenamiento[candidato]:
                                almacenamiento[candidato][id] = {'Hora': resultados['statuses'][0]['created_at'],
                                                                 'Texto': text}

        Persistencia.guardar(almacenamiento)
        Persistencia.guarda_estadistica(contador)








if __name__ == '__main__':
    Main()