import copy
from time import time


class Model:
    def __init__(self):
        self.N_soluzioni = 0
        self.N_iterazioni = 0
        self.soluzioni = []  # almeno non devo passare un altro parametro nella funzione _ricorsione

    def risolvi_n_regine(self, N):
        self.N_soluzioni = 0   # devo resettarli altrimenti se faccio due ricorsioni una dopo l'altra
        self.N_iterazioni = 0  # mi tiene traccia di tutto quello che ho fatto prima,
        self.soluzioni = []    # quindi iterazioni precedenti e soluzioni precedenti
        self._ricorsione([], N)  # il valore iniziale sarà una lista vuota perché non c'è niente dentro

    def _ricorsione(self, parziale, N):
        self.N_iterazioni += 1
        # conto ogni volta che entro dentro la funzione ricorsiva nuova, non importa se caso terminale o no

        # condizione terminale
        if len(parziale) == N:
            print(parziale)
            if self._soluzione_nuova(parziale):
                self.N_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))  # non (parziale)

        # caso ricorsivo
        else:
            for row in range(N):
                for col in range(N):  # le devo provare tutte quindi faccio il doppio ciclo
                    parziale.append((row, col))
                    if self._regina_ammissibile(parziale):  # le condizioni sui vincoli conviene metterle in una funzione a parte
                        self._ricorsione(parziale, N)
                    parziale.pop()  # rimuovo l'ultimo elemento, faccio back tracking

    def _regina_ammissibile(self, parziale):
        """
        Prendo l'ultima regina che ho messo e vedo se rispetta i vincoli sulle righe, sulle colonne,
        e sulle diagonali delle regine precedenti
        """
        if len(parziale) == 1:
            return True  # funzione che ritorna un booleano

        ultima_regina = parziale[-1]  # -1 indica l'ultimo elemento della lista, della collection
        for regina in parziale[:len(parziale) - 1]:

            # controllare righe
            if ultima_regina[0] == regina[0]:  # [0] perché ho una tupla, e la riga è il primo elemento della tupla
                return False

            # controllare colonne
            if ultima_regina[1] == regina[1]:
                return False

            # controllare diagonali
                # check row-col
            if (ultima_regina[0] - ultima_regina[1]) == (regina[0] - regina[1]):
                return False
                # check row+col
            if (ultima_regina[0] + ultima_regina[1]) == (regina[0] + regina[1]):
                return False

        return True

    def _soluzione_nuova(self, soluzione_nuova):
        """
        Devo guardare tutte le soluzioni precedenti, prendo una delle soluzioni precedenti, prendo la prima
        soluzione corrente e vado a vedere se tutte le configurazioni delle regine della soluzione corrente
        sono nella soluzione precedente, allora è una cosa che ho già visto
        """
        # controllo tutte le soluzioni precedenti
        for soluzione in self.soluzioni:
            # per ogni regina della nuova soluzione, controllo se è
            # una configurazione vecchia o no
            for regina in soluzione_nuova:
                if regina in soluzione:  # se la regina non è tra quelle precedenti allora so già che è nuova
                    return False

        return True

    def _new_solution(self, parziale):
        # per ogni soluzione
        for s in self.soluzioni:
            answer = False
            for regina in parziale:
                # se almeno una regina di parziale non si trova nella soluzione precedente
                # la soluzione è nuova
                if regina not in s:
                    answer = True
            if not answer:
                return answer
        return True


if __name__ == '__main__':
    model = Model()
    start_time = time()
    model.risolvi_n_regine(5)
    end_time = time()
    print(f"L'algoritmo ha trovato {model.N_soluzioni} soluzioni")
    print(f"L'algoritmo ha chiamato la funzione ricorsiva {model.N_iterazioni} volte")
    print(f"L'algoritmo ha impiegato {end_time - start_time} secondi")
    print("Le soluzioni sono:")
    print(model.soluzioni)
