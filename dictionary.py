class Dictionary:
    def __init__(self):
        self.dizionario = {}

    def addWord(self, alien, traduzioni:[]):

        if alien not in self.dizionario.keys():
            self.dizionario[alien] = []

        for t in traduzioni:
            if t not in self.dizionario[alien]:
                self.dizionario[alien].append(t)


    def translate(self, alien):
        return self.dizionario[alien]

    def translateWordWildCard(self, parola):

        match = []

        for d in self.dizionario.keys():
            if len(parola) == len(d):

                ricerca = list(parola)
                alieno = list(d)

                wildcard = ricerca.index('?')

                ricerca[wildcard] = alieno[wildcard]

                if "".join(ricerca) == d:
                    match.append(d)

        if len(match) == 1:
            traduzioni = self.dizionario[match[0]]

            for t in traduzioni:
                print(t, end=" ")
                print()

        elif len(match) == 0:
            print ("No match found")

        else:

            for m in match:
                traduzione = self.dizionario[m]
                print(f'Parola: {m}\nTraduzioni:', end=" ")

                for t in traduzione:
                    print(t, end=" ")
                    print()
                    print()

    def stampaDizionario(self):
        print('<<<Dizionario>>>\n')

        for d,t in self.dizionario.items():

            print(f'\nParola aliena: {d}')
            print(f'Traduzioni:', end=" ")
            for tr in t:
                print(tr, end=" ")
                print()

