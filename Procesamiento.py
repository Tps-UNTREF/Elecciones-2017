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
