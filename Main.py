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
        self.procesamiento = Procesamiento()

        try:
            while True:
                numero_menu = self.leer_entero('Ingrese una opción: \n' '1- Obtener tweets \n' '2- Ranking de candidatos más twitteados \n' '3- Ranking de candidatos más apreciado \n' '4- Terminar \n')

                if numero_menu == 1:
                    # Obtener tweets
                    almacenamiento = Persistencia.cargar()
                    self.procesamiento.busqueda(almacenamiento)

                elif numero_menu == 2:
                    # Ranking de candidatos más twitteados
                    self.procesamiento.ranking_candidato_mas_mencionados()

                elif numero_menu == 3:
                    # Ranking de candidatos más apreciado
                    print('Espere...')

                    Persistencia.normalizar_tweets()
                    Persistencia.normalizar_diccionario_de_afecto()
                    Persistencia.normalizar_stop_words()

                    diccionario = self.procesamiento.leer_tweets()
                    diccionario_puntajes = self.procesamiento.ranking_candidatos_mas_apreciados(diccionario)
                    print()
                    print('Estadísticas:')
                    for candidato, puntaje in diccionario_puntajes.items():
                        acumulador = 0
                        for palabra,cantidad_total in diccionario[candidato].items():
                            acumulador += cantidad_total
                        print(candidato, ': ' + str((puntaje/acumulador)*100))

                    print()
                    print()

                elif numero_menu == 4:
                    #TERMINAR
                    break

                else:
                    raise NumeroNoEstaEnMenu
        except NumeroNoEstaEnMenu:
            print('Por favor, ingrese un numero del 1 al 4.')



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