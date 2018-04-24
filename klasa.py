from funkcja import *


class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
        self.skróæ()

    def skróæ(self):
        x = int(1)
        if (self.licznik<0):
            x =-1
        self.licznik*= x
        a = NWD(self.licznik, self.mianownik)
        self.licznik /= a
        self.mianownik /= a
        if(x == -1):
            self.licznik*=-1

    def __str__(self):
        return ((str(self.licznik) + '/' + str(self.mianownik)))

    def wyswietl(self):  # to ju¿ nie jest konicznie jel jest __str__
        print(str(self.licznik) + '/' + str(self.mianownik))

    def __add__(self, u2):
        return Ulamek(self.licznik * u2.mianownik + u2.licznik * self.mianownik, self.mianownik * u2.mianownik)

    def __sub__(self, u2):
        return Ulamek(self.licznik * u2.mianownik - u2.licznik * self.mianownik, self.mianownik * u2.mianownik)

    def __lt__(self,u2):
        if ((self.licznik*u2.mianownik)<(self.mianownik*u2.licznik)):
            return (True)
        else:
            return (False)

    def __eq__(self,u2):
        if ((self.licznik*u2.mianownik)==(self.mianownik*u2.licznik)):
            return (True)
        else:
            return (False)

    def __ne__(self,u2):
        if ((self.licznik*u2.mianownik)==(self.mianownik*u2.licznik)):
            return (False)
        else:
            return (True)
