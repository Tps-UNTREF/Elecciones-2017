from Main import *


class Procesamiento():
    @staticmethod
    def ranking_candidato_mas_mencionados():
        almacenamiento_a_procesar = Persistencia.cargar()
        aux = Main.total_tweets(almacenamiento_a_procesar)
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



