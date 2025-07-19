# Zorluk : Basit
liste = [4, 8, 6, 2]

liste.sort()
s = liste[1] - liste[0]  # Aritmetik fark

for i in range(len(liste) - 1):

    if s != liste[i + 1] - liste[i]:

        print("Bu liste aritmatik değil")
        break

else:
    print("Bu liste aritmatik")
