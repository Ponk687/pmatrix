import random
import time


def randomAscii():
    r = random.randint(32, 126)
    return chr(r)

def ligne(tailleLigne):
    ligne = ""
    for i in range(tailleLigne):
        random.randint(0,200)
        ligne = ligne + randomAscii()
        for i in range (int((random.randint(0,1000))/random.randint(1,1000))):  # on fait une division, de cette manière là, il est plus probable d'obtenir un espace censé
            ligne = ligne + " "
    return ligne


while (True) :
    saut = random.randint(1,10)
    for i in range(int(saut/random.randint(1,5))):   #ici aussi on vient diviser pour garder plus de petits chiffres
        print("\n")
    txt = ligne(225-random.randint(0,225))
    print(f"\033[92m{txt})\033[0m")