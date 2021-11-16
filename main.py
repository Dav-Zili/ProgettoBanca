import csv
from random import randint
from datetime import date
from itertools import chain
def letturaIntestatarioConto():
    with open("./Anagrafica_conti.csv", encoding="utf-8-sig") as fileCSV:
        lettore = csv.reader(fileCSV,delimiter=";")
        contatoreLinea = 0
        for riga in lettore:
            if contatoreLinea == 0:
                print("I nomi delle colonne sono: ", ", ".join(riga))  
            else:
                print("|Nome: " , riga[0], " Cognome: " , riga[1], " IDConto:", riga[2],"|")
            contatoreLinea += 1
        print("Processate: ", contatoreLinea - 1, " righe")
def letturaSaldoConto(idConto):
    idConto = str(idConto)
    with open("./Saldo_conti.csv", encoding="utf-8-sig") as fileCSV:
        lettore = csv.reader(fileCSV,delimiter=";")
        for riga in lettore:
            if riga[0] == idConto:
                print("|Il saldo è:", riga[1] , "|")  

def letturaMovimentiConto(idConto):
    idConto = str(idConto)
    with open("./SaldoMovimenti_conti.csv", encoding="utf-8-sig") as fileCSV:
        lettore = csv.reader(fileCSV,delimiter=";")
        for riga in lettore:
            if riga[0] == idConto:
                print("|In data ", riga[2] , " è avvenuto una richiesta di ", riga[1] , "|")

def inserisciConto():
    with open('Anagrafica_conti.csv', 'a', encoding="utf-8-sig", newline='') as fileCSV:
        writer = csv.writer(fileCSV, delimiter=';')
        nome = input("Dimmi il nome del correntista\n")
        cognome = input("Dimmi il cognome del correntista\n")
        idConto = randint(100,999)
        l = [nome, cognome, idConto]
        writer.writerow(l)
        with open('Saldo_conti.csv', 'a', encoding="utf-8-sig", newline='') as fileCSV2:
            writer = csv.writer(fileCSV2, delimiter=';')
            saldo = input("Dimmi il saldo iniziale da depositare\n")
            saldo += "$"
            dataOdierna = date.today().strftime("%d/%m/%Y")
            l = [idConto, saldo, dataOdierna]
            writer.writerow(l)
            with open('SaldoMovimenti_conti.csv', 'a', encoding="utf-8-sig", newline='') as fileCSV3:
                writer = csv.writer(fileCSV3, delimiter=';')
                l = [idConto, saldo, dataOdierna]
                writer.writerow(l)
def versaSoldi():
    with open("./Saldo_conti.csv", encoding="utf-8-sig") as fileCSV:
        lettore = csv.reader(fileCSV,delimiter=";")
        lista = list(lettore)
        idConto = input("Inserisci id conto\n")
        if idConto in chain.from_iterable(lista):
            numeroRiga = 0
            for riga in lista:
                if riga[0] == idConto:
                    sommaDepositare = int(input("Quanti soldi vanno depositati? \n"))
                    nuovoSaldo = int(riga[1].replace("$", "")) + sommaDepositare
                    print("Il saldo attuale ora è di:", nuovoSaldo , "$\n")
                    lista[numeroRiga][1] = str(nuovoSaldo) + "$"
                    with open('Saldo_conti.csv', 'w', encoding="utf-8-sig", newline='') as fileCSV2:
                        writer = csv.writer(fileCSV2, delimiter=';')
                        writer.writerows(lista)
                numeroRiga += 1
        else:
            print("Errore, id del conto inesistente")
def prelevaSoldi():
    with open("./Saldo_conti.csv", encoding="utf-8-sig") as fileCSV:
        lettore = csv.reader(fileCSV,delimiter=";")
        lista = list(lettore)
        idConto = input("Inserisci id conto\n")
        if idConto in chain.from_iterable(lista):
            numeroRiga = 0
            for riga in lista:
                if riga[0] == idConto:
                    sommaPrelevare = int(input("Quanti soldi vanno prelevati? \n"))
                    nuovoSaldo = int(riga[1].replace("$", "")) - sommaPrelevare if (sommaPrelevare <= int(riga[1].replace("$", ""))) else riga[1]
                    print("Il saldo attuale ora è di:", nuovoSaldo , "$\n")
                    lista[numeroRiga][1] = str(nuovoSaldo) + "$"
                    with open('Saldo_conti.csv', 'w', encoding="utf-8-sig", newline='') as fileCSV2:
                        writer = csv.writer(fileCSV2, delimiter=';')
                        writer.writerows(lista)
                numeroRiga += 1
        else:
            print("Errore, id del conto inesistente")       
x = int(input("Cosa si desidera fare?\n 1. Leggere informazioni su correntista \n 2. Stampare saldo di un conto a partire dall'id di esso \n 3. Stampare lista movimenti a partire dall'id conto \n 4. Inserire un nuovo conto \n 5. Versa soldi su un conto\n 6. Preleva soldi \n"))     
if(x == 1):
    letturaIntestatarioConto()
elif(x == 2):
        idConto = input("Inserisci id conto\n")
        letturaSaldoConto(idConto)
elif(x == 3):
        idConto = input("Inserisci id conto\n")
        letturaMovimentiConto(idConto)
elif(x == 4):
    inserisciConto()
elif(x == 5):
    versaSoldi()
elif(x == 6):
    prelevaSoldi()
else:
        print("Hai sbagliato a scrivere!")