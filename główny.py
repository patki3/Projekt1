from klasa import *
from funkcja import *
from nowaklasa import *

u1 = Ulamek(1, 4)
print("U1 = " + (str(u1)))
u2 = Ulamek(1, 0)

print("U2 = " + (str(u2)))


print("u1 + u2 = ", end=" ")
print(u1 + u2)
print("u1 - u2 = ", end=" ")
print(u1 - u2)


tablica=[u1,u2,Ulamek(3,4)]
print(str(list(map(str,tablica))))
tablica.sort()
print(str(list(map(str,tablica))))

print("NWD = " + str(NWD(u1.mianownik, u2.mianownik)))


print("")
print("K O L E K C J O N E R")
print("")

osoba=kolekcjoner("A","B")


osoba.kolekcja+=[Ulamek(1,2),Ulamek(3,4),u1,u2]
print(osoba)
