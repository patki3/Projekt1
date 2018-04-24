def NWD(a, b):
    if (a == b):
        return a
    if (a > b):
        a, b = b, a
    while (a != 0):
        a, b = b % a, a
    return b

n=int(input())
for i in range(0,n):
    liczby=list(map(int,input().split()))
    print(str(NWD(liczby[0],liczby[1])))
