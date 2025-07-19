# Zorluk : Orta

def fonk(liste): # Listedeki sayıları int yapıyor
    x = 1
    t = 0

    for i in range(len(liste)):
        y = liste[i] * x
        x = x * 10
        t = y + t

    return t

def fonk1(x): # İnt değeri listeye geri çeviriyor

    liste3 = []
    while x > 0:
        y = x % 10
        liste3.append(y)
        x = x // 10

    return liste3

liste1 = [9,9,9,9,9,9,9]
liste2 = [9,9,9,9]

ç = fonk(liste2)
ç1 =  fonk(liste1)

ç2 = ç1 + ç

ç3 = fonk1(ç2)

print(ç3)
