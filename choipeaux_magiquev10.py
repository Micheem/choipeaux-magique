# -*- coding: utf-8 -*-
'''
Description du programme
Auteurs: Loys MARIOT, Florian VERNE, MichéèêëesS MANON
Numéro de version 9.0
Date de dernière révision: 00/03/2022
'''

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


eleve_random1 = {'Nom': 'num1', 'Courage': 9, 'Ambition': 2, 'Intelligence': 8, 'Good': 9}
eleve_random2 = {'Nom': 'num2', 'Courage': 6, 'Ambition': 7, 'Intelligence': 9, 'Good': 7}
eleve_random3 = {'Nom': 'num3', 'Courage': 3, 'Ambition': 8, 'Intelligence': 6, 'Good': 3}
eleve_random4 = {'Nom': 'num4', 'Courage': 2, 'Ambition': 3, 'Intelligence': 7, 'Good': 8}
eleve_random5 = {'Nom': 'num5', 'Courage': 3, 'Ambition': 4, 'Intelligence': 8, 'Good': 8}
a = 1

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
    '''
    Fonction qui change les chaînes de caractères des caractéristiques en entier
    :param table: liste de dictionnaire contenant l'ensemble des élèves de poudlard
    :return: c'est la même table que celle en paramètre sauf que ses descripteurs de caractéristiques sont maintenant des entiers
    '''
    for dico in table:
        for keys in ['Courage', 'Ambition', 'Intelligence', 'Good']:
            dico[keys] = int(dico[keys])
    return table


converti(poudlard_characters)


def affichage(table):
    '''
    Fonction d'affichage qui permet une visualisation claire des résultats obtenus
    Entrée : liste de dictionnaire  contenant les élèves qu'on va afficher
    '''

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


# début du programme
def distance(eleve1, eleve2):
    '''
    Fonction calculant la distance entre 2 élèves en fonction de leurs caractéristiques
    On utilise ici la distance euclidienne
    :param eleve1: dictionnaire contenant des caractéristiques
    :param eleve2: pareil que l'élève 1
    :return: (entier) la distance entre 2 élèves
    '''
    return sqrt((eleve1['Courage'] - eleve2['Courage']) ** 2
                + (eleve1['Ambition'] - eleve2['Ambition']) ** 2
                + (eleve1['Intelligence'] - eleve2['Intelligence']) ** 2
                + (eleve1['Good'] - eleve2['Good']) ** 2)


def kkpv(table, eleve, k):
    '''
    Fonction ajoutant un descripteur à chaque eleve(dictionnaire) dans la table poudlard
    :param table: liste de dictionnaire contenant l'entierté des élèves
    :param eleve: un dico contenant élève et ses caractéristiques
    :return: table: liste de dictionnaire contenant désormais un nouveau descripteurs, la distance
    '''
    for eleves in table:
        eleves['Distance'] = round(distance(eleve, eleves), 2)

    voisins = sorted(table, key=lambda x: x['Distance'])
    table = voisins[:k]

    return table


def maison(table, eleve_cible, k):
    '''
    Fonction déterminant quelle maison serait la mieux adapté à un élève en fonction des kppv
    :param table: (liste de dictionnaire)table contenant les élèves de poudlard avec lesquelles on va comparer notre élève selon le nombre de voisin
    :param eleve_cible: (dictionnaire) élève auquel on veut trouver la maison
    :param k: (entier) nombre de voisins
    :return: sa_maison, une chaine de caractère contenant la maison la mieux adapté pour l'élève
    '''

    redondance_g = 0
    redondance_h = 0
    redondance_r = 0
    redondance_s = 0

    for dico in kkpv(table, eleve_cible, k):
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
    return sa_maison


def validation_croisee(table):
    '''
    Fonction déterminant l'efficacité de notre programme grâce à une validation croisée
    :param table: liste de dictionnaire contenant tout les élèves
    '''
    nb_test = 100
    ça_fonctionne = 0
    for _ in range(nb_test):
        train_set = table[:72]
        test_set = table[73:]
        for eleve in test_set:
            if maison(train_set, eleve, k) == eleve['House']:
                ça_fonctionne += 1
    print(f"Le pourcentage de réussite du programme est de {round(ça_fonctionne / len(test_set), 2)}%")


'''-------------------------------------IHM-------------------------------------'''


def affichage_eleve(table, eleve_cible, k):
    '''
    Fonction qui complète l'IHM, elle cherche les k + proches voisins selon l'élève en argument
    elle prend é
    PARAMETRE table: liste de dictionnaire contenant tout les élèves et leurs caractéristiques
    PARAMETRE eleve_cible : (dictionnaire) élève de réference
    PARAMETRE k : variable contenant le nombre de voisins qu'on obtiendra
    '''

    affichage(kkpv(table, eleve_cible, k))
    print(f"La maison attribué à cet élève est {maison(table, eleve_cible, k)}")
    validation_croisee(table)
    print()
    reps = input("Veux tu réessayer? [y] [n]")
    if reps.lower() == 'y':
        print()
        a = 1
    else:
        print('Au revoir')
        a = 2
    return a


print('Bienvenue dans notre algo')
while a == 1:
    k = 5
    if input("Voulez vous choisir une valeur de k ? [y] / [n]: ") == "y":
        k = int(input("rentrer votre valeur de k: "))

    print()
    mode = input('valeur par défaut ou perso? ( défaut = [d] | perso = [p] ): ')
    if mode.lower() not in ['d', 'p']:
        print(f"{bcolors.g}{bcolors.rouge}ERREUR{bcolors.reset}")
        print("Veuillez entrer une valeur valide: [d] ou [p]")
    if mode.lower() == 'd':
        rep = int(input("Vous voulez affichez les k plus proche voisin de qui? [1] / [2] / [3] / [4] / [5] : "))

        if rep not in [1, 2, 3, 4, 5]:
            print(f"{bcolors.g}{bcolors.rouge}ERREUR{bcolors.reset}")
            print("Veuillez entrer une valeur valide: [1] ou [2] ou [3] ou [4] ou [5]")

        if rep in [1, 2, 3, 4, 5]:
            print()
            print("Vous avez choisi d'afficher les k plus proche voisin de l'élève", rep)
            print()
            gang = [eleve_random1, eleve_random2, eleve_random3, eleve_random4, eleve_random5]
            a = affichage_eleve(poudlard_characters, gang[rep - 1], k)

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
