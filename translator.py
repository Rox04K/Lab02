import dictionary as d

class Translator:

    def __init__(self):
        self.dizionario = d.Dictionary()

    def printMenu(self):

        print('_'*20)
        print('Translator Alien-Italian')
        print('_'*20)
        print('1. Aggiungi nuova parola')
        print('2. Cerca una traduzione')
        print('3. Cerca con wildcard')
        print('4. Stampa tutto il Dizionario')
        print('5. Exit')
        print('_'*20)
        print()

    def loadDictionary(self, dict):

        with open (dict, 'r') as infile:
            file = infile.readlines()

            for line in file:
                line = line.strip().split(' ')
                self.dizionario.addWord(line[0], [line[1]])

    def handleAdd(self, entry):
        alien = entry[0]
        trad = entry[1].split(" ")

        self.dizionario.addWord(alien, trad)

    def handleTranslate(self, query):
        traduzioni = self.dizionario.translate(query)

        for t in traduzioni:
            print(t, end=" ")
        print()

    def handleWildCard(self,query):

        self.dizionario.translateWordWildCard(query)

    def stampaDizionario(self):
        self.dizionario.stampaDizionario()
