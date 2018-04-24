class kolekcjoner:
    def __init__(self,imie,nazwisko):
        self.imie=imie
        self.nazwisko=nazwisko
        self.kolekcja=[]

    def __str__(self):
        return (self.imie + " " + self.nazwisko + " " + str(list(map(str,self.kolekcja))))
