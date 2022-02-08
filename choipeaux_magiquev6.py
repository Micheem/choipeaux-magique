# -*- coding: utf-8 -*-
from math import sqrt
import csv


class bcolors:
    vert = '\33[92m'
    jaune = '\33[93m'
    rouge = '\33[91m'
    bleu = '\33[94m'
    rose = '\33[95m'
    noir = '\33[30m'
    bleubizarre = '\33[36m'

    reset = '\033[0m'  # réinitialise la couleur
    g = '\033[1m'  # gras
    s = '\033[4m'  # surligner
    i = '\033[3m'  # italique


'''
DEFAUT
• Courage : 9 Ambition : 2 Intelligence : 8 Good : 9
• Courage : 6 Ambition : 7 Intelligence : 9 Good : 7
• Courage : 3 Ambition : 8 Intelligence : 6 Good : 3
• Courage : 2 Ambition : 3 Intelligence : 7 Good : 8
• Courage : 3 Ambition : 4 Intelligence : 8 Good : 8
'''
a = 1


def maison(table):
    redondance_g = 0
    redondance_h = 0
    redondance_r = 0
    redondance_s = 0

    for dico in table:
        house = dico['House']

        if house == 'Gryffindor':
            redondance_g += 1

        elif house == 'Hufflepuff':
            redondance_h += 1

        elif house == 'Slytherin':
            redondance_s += 1

        else:
            redondance_r += 1

    liste_redondance = [redondance_s, redondance_g, redondance_h, redondance_r]
    liste_redondance.sort(reverse=True)

    if liste_redondance[0] == redondance_g:
        sa_maison = 'Gryffindor'

    elif liste_redondance[0] == redondance_h:
        sa_maison = 'Hufflepuff'

    elif liste_redondance[0] == redondance_s:
        sa_maison = 'Slytherin'

    elif liste_redondance[0] == redondance_r:
        sa_maison = 'Ravenclaw'

    print(f"{bcolors.g}la maison attribué à cette élève est {sa_maison}{bcolors.reset}")


def affichage(table):
    for dico in table:
        nom = dico['Name']
        distance = dico['Distance']
        courage = dico['Courage']
        ambition = dico['Ambition']
        intelligence = dico['Intelligence']
        good = dico['Good']
        house = dico['House']

        print(
            f"{bcolors.g + bcolors.s + bcolors.i}Nom{bcolors.reset} : {nom}|{bcolors.g + bcolors.rouge} Courage{bcolors.reset} : {courage}|"
            f"{bcolors.g + bcolors.jaune} Ambition{bcolors.reset} : {ambition}|"
            f"{bcolors.g + bcolors.bleu} Intelligence{bcolors.reset} : {intelligence}|{bcolors.g + bcolors.vert} Good{bcolors.reset} : {good}|"
            f"{bcolors.g + bcolors.rose} Distance{bcolors.reset} : {distance}|{bcolors.g + bcolors.bleubizarre} Maison{bcolors.reset} : {house}")


eleve_random1 = {'Nom': 'num1', 'Courage': 9, 'Ambition': 2, 'Intelligence': 8, 'Good': 9}
eleve_random2 = {'Nom': 'num2', 'Courage': 6, 'Ambition': 7, 'Intelligence': 9, 'Good': 7}
eleve_random3 = {'Nom': 'num3', 'Courage': 3, 'Ambition': 8, 'Intelligence': 6, 'Good': 3}
eleve_random4 = {'Nom': 'num4', 'Courage': 2, 'Ambition': 3, 'Intelligence': 7, 'Good': 8}
eleve_random5 = {'Nom': 'num5', 'Courage': 3, 'Ambition': 4, 'Intelligence': 8, 'Good': 8}

with open("Characters.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    characters = [{key: value for key, value in element.items()} for element in reader]

with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    caracteristiques = [{key: value for key, value in element.items()} for element in reader]

poudlard_characters = []

for poudlard_character in caracteristiques:
    for i in characters:
        if poudlard_character['Name'] == i['Name']:
            poudlard_character.update(i)
            poudlard_characters.append(poudlard_character)


def converti(table):
    for dico in table:
        for keys in ['Courage', 'Ambition', 'Intelligence', 'Good']:
            dico[keys] = int(dico[keys])
    return table


converti(poudlard_characters)


def distance(eleve1, eleve2):
    return sqrt((eleve1['Courage'] - eleve2['Courage']) ** 2
                + (eleve1['Ambition'] - eleve2['Ambition']) ** 2
                + (eleve1['Intelligence'] - eleve2['Intelligence']) ** 2
                + (eleve1['Good'] - eleve2['Good']) ** 2)


def ajout_distances(poudlard_characters, eleve1):
    for eleves in poudlard_characters:
        eleves['Distance'] = distance(eleve1, eleves)
    return poudlard_characters


'''----------------------------------------------IHM--------------------------------------------------(pas fini)'''
print('Bienvenue dans notre algo')
while a == 1:
    k = 5
    if input("Voulez vous choisir une valeur de k ? [y] / [n]: ") == "y":
        k = int(input("rentrer votre valeur de k: "))

    print()
    mode = input('valeur par défaut ou perso? ( défaut = [d] | perso = [p] ): ')
    while mode.lower() not in ['d', 'p']:
        print(f"{bcolors.g}{bcolors.rouge}ERREUR{bcolors.reset}")
        print("Veuillez entrer une valeur valide: [d] ou [p]")
    if mode.lower() == 'd':
        rep = input("Vous voulez affichez les k plus proche voisin de qui? [a] / [b] / [c] / [d] / [e] :")

        if rep.lower() not in ['a', 'b', 'c', "d", "e"]:
            print(f"{bcolors.g}{bcolors.rouge}ERREUR{bcolors.reset}")
            print("Veuillez entrer une valeur valide: [a] ou [b] ou [c] ou [d] ou [e]")

        if rep.lower() == 'a':
            print()
            print("Vous avez choisi d'afficher les k plus proche voisin de l'élève random 1 ")
            print()
            eleve_1 = ajout_distances(poudlard_characters, eleve_random1)
            voisins1 = sorted(eleve_1, key=lambda x: x['Distance'])
            copie1 = voisins1[:k]
            affichage(copie1)
            maison(copie1)
            print()
            reps = input("Veux tu réessayer? [y] [n]")
            if reps.lower() == 'y':
                print()
                pass
            else:
                print('Au revoir')
                a = 2

        if rep.lower() == 'b':
            print()
            print("Vous avez choisi d'afficher les k plus proche voisin de l'élève random 2 ")
            print()
            eleve_2 = ajout_distances(poudlard_characters, eleve_random2)
            voisins2 = sorted(eleve_2, key=lambda x: x['Distance'])
            copie2 = voisins2[:k]
            affichage(copie2)
            maison(copie2)
            print()
            reps = input("Veux tu réessayer? [y] [n]")
            if reps.lower() == 'y':
                print()
                pass
            else:
                print('Au revoir')
                a = 2

        if rep.lower() == 'c':
            print()
            print("Vous avez choisi d'afficher les k plus proche voisin de l'élève random 3 ")
            print()
            eleve_3 = ajout_distances(poudlard_characters, eleve_random3)
            voisins3 = sorted(eleve_3, key=lambda x: x['Distance'])
            copie3 = voisins3[:k]
            affichage(copie3)
            maison(copie3)
            print()
            reps = input("Veux tu réessayer? [y] [n]: ")
            if reps.lower() == 'y':
                print()
                pass
            else:
                print('Au revoir!')
                a = 2

        if rep.lower() == 'd':
            print()
            print("Vous avez choisi d'afficher les k plus proche voisin de l'élève random 4 ")
            print()
            eleve_4 = ajout_distances(poudlard_characters, eleve_random4)
            voisins4 = sorted(eleve_4, key=lambda x: x['Distance'])
            copie4 = voisins4[:k]
            affichage(copie4)
            maison(copie4)
            print()
            reps = input("Veux tu réessayer? [y] [n]: ")
            if reps.lower() == 'y':
                print()
                pass
            else:
                print('Au revoir')
                a = 2

        if rep.lower() == 'e':
            print()
            print("Vous avez choisi d'afficher les k plus proche voisin de l'élève random 5 ")
            print()
            eleve_5 = ajout_distances(poudlard_characters, eleve_random5)
            voisins5 = sorted(eleve_5, key=lambda x: x['Distance'])
            copie5 = voisins5[:k]
            affichage(copie5)
            maison(copie5)
            print()
            reps = input("Veux tu réessayer? [y] [n]: ")
            if reps.lower() == 'y':
                print()
                pass
            else:
                print('Au revoir')
                a = 2

    if mode.lower() == 'p':
        print()
        eleve_perso = {}
        print(f"Entrez le Nom de votre élève: ")
        eleve_perso['Name'] = input()
        print(f"Entrez la valeur du courage de votre élève: ")
        eleve_perso['Courage'] = int(input())
        print(f"Entrez la valeur de l'ambition de votre élève: ")
        eleve_perso['Ambition'] = int(input())
        print(f"Entrez la valeur de l'intelligence de votre élève: ")
        eleve_perso['Intelligence'] = int(input())
        print(f"Entrez la valeur de la bontée de votre élève: ")
        eleve_perso['Good'] = int(input())

        votre_eleve = ajout_distances(poudlard_characters, eleve_perso)
        voisin_votre_eleve = sorted(votre_eleve, key=lambda x: x['Distance'])
        copie_perso = voisin_votre_eleve[:k]
        affichage(copie_perso)
        maison(copie_perso)
        print()
        reps = input("Veux tu réessayer? [y] [n]: ")
        if reps.lower() == 'y':
            print()
            pass
        else:
            print('Au revoir')
            a = 2
