import random
class Domanda(object):
    def __init__(self, testo="", diff=None, corretta="", opzioni=[]):   #quando fai costruttore specifica il tipo
        self.testo=testo
        self.difficoltà=diff    #perchè diff none, indica che quel valore potrebbe anche non esserci da subito e non bisogna usare valori di default
        self.corretta=corretta
        self.opzioni=opzioni


    def opzioni_random(self):       #random.shuffle per mischiare randomicamente
        random.shuffle(self.opzioni)
        return self.opzioni