import random

from domanda import Domanda
from giocatore import Giocatore

#read legge tutto il file e lo trasforma in una grande stringa
f = open("domande.txt", "r").read().splitlines()  #crea una lista di stringhe in cui ogni stringa è una riga del file senza il carattere /n di a capo
d=[]
for ii in range(0, len(f), 7):  #scorre la lista da 0 a len(f) di 7 in 7, ogni 7 righe contenuta un intera domanda con le sue opzioni
    d.append(Domanda(testo=f[ii], diff=f[ii+1], corretta=f[ii+2], opzioni=f[ii+2:ii+6]))  #lista in cui a ogni indice trovo una domanda intera con tutte le sue caratteristiche
    #ii prende il testo della domanda perchè è il primo, poi gli altri sono successivi
    #opzioni=f[ii+2:ii+6]  da ii+2 escluso a ii+6 incluso

#imposta i valori iniziali
flag=True
current_diff = 0
max_diff = max(d, key=lambda x: x.difficoltà).difficoltà  #cerca la difficolta massima, non ordina
punti=0


while(flag):
    current_d=[]
    current_d = [x for x in d if int(x.difficoltà)==current_diff]  #se la domanda ha la difficolta uguale a quella corrente aggiungila alla lista current_d
    ii = random.randint(0,len(current_d)-1)  #genero un indice casuale per scegliere una domanda casuale da current_d
    current_opzioni = current_d[ii].opzioni_random()
    print("Livello "+ current_d[ii].difficoltà + ") "+ current_d[ii].testo)   #faccio la domanda
    for jj in range(len(current_opzioni)):    #scorro le opzioni per stamparle
        print(str(jj+1) + '. ' + current_opzioni[jj]) #le printo con il numero.
    n_risposta = input("Inserisci risposta: ")   #con input("") ti permette di scrivere qualcosa sul terminale
    risposta = current_opzioni[int(n_risposta)-1] #dato il numero della risposta, ricava la risposta data in parola

    if risposta != current_d[ii].corretta:
        flag=False
        print("Risposta sbagliata! La risposta era: " + str(current_opzioni.index(current_d[ii].corretta) +1))   #dice il numero della risposta
        print("Punteggio: ", punti)   #il punteggio rimane 0
        nick = input("Inserisci nickname: ")
    else:
        print("Risposta corretta!")
        current_diff = current_diff+1   #se la risposta è corretta si sale di difficolta
        punti=punti+1   #se la risposta è corretta sali di un punto
        if current_diff > int(max_diff):
            print("Hai vinto! Punteggio: ", punti)   #se raggiungi la massima difficolta, hai finito il gioco e hai vinto
            flag=False    #finito il gioco, metti false così non entri più nel ciclo
            nick = input("Inserisci nickname: ")

f = open("punti.txt", "r").read().splitlines()   #leggi file dei punti
g=[]
for ii in range(len(f)):
    g.append(Giocatore(giocatore=f[ii].split(' ')[0], punti=f[ii].split(' ')[1]))#creo un giocatore(che ha nome e punti) per ogni riga del file e li memotizzo in g
g.append(Giocatore(giocatore=nick, punti=punti))  #aggiungo anche il giocatore che ha appena giocato, al fondo dopo i giocatori passati

g.sort(key=lambda x: int(x.punti), reverse=True) #ordino in base ai punteggi

with open('punti.txt', 'w') as f:   #ora apro il file punti in scrittura
    for jj in g:
        nick = jj.giocatore
        punti = jj.punti
        f.write(nick+ ' ' + str(punti) + '\n')   #scrive nel file

