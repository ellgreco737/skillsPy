import time
import os

ClearConsole = lambda: os.system('cls')

A = []
B = []
C = []
a = []
b = []
c = []

def choice(n):
    if n == 'A' or n=='a':
        A.append('A'+str(int(len(a)+1)))
        a.append(1)
        return 'Twój numer to ' +(A[-1])
    elif n == 'B' or n == 'b' :
        B.append('B' + str(int(len(b) + 1)))
        b.append(1)
        return 'Twój numer to ' + (B[-1])
    elif n == 'C' or n == 'c':
        C.append('C' + str(len(c) + 1))
        c.append(1)
        return 'Twój numer to '+ (C[-1])
    elif n == 'dupa1':
        x = input('Z której kolejki będziesz obsługiwał klienta? ')
        if x == 'A' or x == 'a':
            if A == []:
                return 'Tu nikogo nie ma'
            else:
                z = (A[0])
                A.pop(0)
                return z
        elif x == 'B' or x == 'b':
            if B == []:
                return 'Tu nikogo nie ma'
            else:
                z = (B[0])
                B.pop(0)
                return z
        elif x == 'C' or x == 'c':
            if C == []:
                return 'Tu nikogo nie ma'
            else:
                z = (C[0])
                C.pop(0)
                return z
    else:
        return 'Podaj włąściwą literę'


if __name__ == "__main__":

    while 1 == 1:
        print('Witamy w urzędzie: A - rejestracja pojazdów, '+str(A)+' B - odbiór prawo jazdy'+str(B)+', C - odbiór dowodu osobistego'+str(C))
        n = input('podaj litrę: ')
        print(choice(n))
        time.sleep(3) # czas ustawiam na 3 żeby było szybciej
        ClearConsole() # nie działa, dlaczego?
