import translator as tr
import re

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    while not txtIn.isdigit():
        txtIn = input("Valore non valido, reinserire valore: ")

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?\n")
        txtIn = input()
        while not bool(re.fullmatch(r'[a-zA-Z\s]*', txtIn)):
            txtIn = input("Valore non valido, reinserire valore: ")
        tupla = txtIn.lower().split(" ", 1  )
        t.handleAdd(tupla)
        print("Aggiunta!\n")
        continue

    if int(txtIn) == 2:
        print("Ok, quale parola devo cercare?\n")
        txtIn = input()
        while not bool(re.fullmatch(r'[a-zA-Z]*', txtIn)):
            txtIn = input("Valore non valido, reinserire valore: ")
        parola = txtIn.lower()
        t.handleTranslate(parola)
        continue

    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare?\n")
        txtIn = input()
        while not bool(re.fullmatch(r'[a-zA-Z?]*', txtIn)) or txtIn.count("?") != 1:
            txtIn = input("Valore non valido, reinserire valore: ")
        parola = txtIn.lower()
        t.handleWildCard(parola)
        continue

    if int(txtIn) == 4:
        t.stampaDizionario()

    if int(txtIn) == 5:
        break


