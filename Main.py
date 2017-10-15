import time

from twitter import *

import Persistencia
from Procesamiento import *
from Excepciones.NumeroNoEstaEnMenu import NumeroNoEstaEnMenu
from config import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_SECRET, CONSUMER_KEY


class Main():

    def __init__(self):
        # Nos identificamos con twitter
        self.tw = Twitter(auth=OAuth(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

        try:
            while True:
                numero_menu = self.leer_entero('Ingrese una opción: \n' '1- Obtener tweets \n' '2- Obtener ranking(Mas tweeteados) \n' '3- Obtener Estadisticas \n' '4- Terminar \n')

                if numero_menu == 1:
                    # OBTENER TWEETS
                    self.candidatos = ["@CFKArgentina", "@estebanbullrich", "@SergioMassa", "@RandazzoF", "@nestorpitrola", "@JorgeTaiana", "@gladys_gonzalez", "@Stolbizer", "@andreadatri"]
                    almacenamiento = Persistencia.cargar()
                    self.busqueda(self.candidatos, almacenamiento)

                elif numero_menu == 2:
                    # OBTENER RANKING
                    Procesamiento.ranking_candidato_mas_mencionados()

                elif numero_menu == 3:
                    # OBTENER ESTADISTICAS
                    pass

                elif numero_menu == 4:
                    #TERMINAR
                    break

                else:
                    raise NumeroNoEstaEnMenu
        except NumeroNoEstaEnMenu:
            print('Por favor, ingrese un numero del 1 al 4.')


    def busqueda(self, lista, almacenamiento):
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

    @staticmethod
    def total_tweets(almacenamiento):
        lista_candidatos=[]
        contador = 0
        for candidato, tweets in almacenamiento.items():
            contador += len(tweets)
            lista_candidatos.append((len(tweets),candidato))
        return lista_candidatos


    def leer_entero(self, texto):
        while True:
            try:
                ingresado = eval(input(texto))
                if type(ingresado) == int:
                    return ingresado
                else:
                    raise Exception
            except (Exception, ValueError):
                print('Por favor ingrese un numero entero')
            except (EOFError, KeyboardInterrupt):
                print('Error atrapado de Ctrl-C')


if __name__ == '__main__':
    Main()