# -*- coding: utf-8 -*-
from math import sqrt
import csv


k = 5
def affichage(table):
    for dico in table:
        nom = dico['Name']
        distance = dico['Distance']
        courage = dico['Courage']
        ambition = dico['Ambition']
        intelligence = dico['Intelligence']
        good = dico['Good']

        print(f"Nom : {nom}, courage : {courage}, ambition : {ambition}, intelligence : {intelligence}, good : {good}, distance : {distance}")



eleve_random = {'Nom' :'ddfi','Courage' : 9, 'Ambition' : 2, 'Intelligence' : 8, 'Good' : 9 }


with open("Characters.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    characters = [{key : value for key, value in element.items()} for element in reader]


with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    caracteristiques = [{key : value for key, value in element.items()} for element in reader]

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

    return sqrt((eleve1['Courage'] - eleve2['Courage'])**2
    + (eleve1['Ambition']- eleve2['Ambition'])**2
    + (eleve1['Intelligence'] - eleve2['Intelligence'])**2
    + (eleve1['Good'] - eleve2['Good'])**2)

def ajout_distances(poudlard_characters, eleve1):
    for eleves in poudlard_characters:
        eleves['Distance'] = distance(eleve1, eleves)
    return poudlard_characters

for eleves in poudlard_characters:
    eleve = ajout_distances(poudlard_characters, eleve_random)
voisins = sorted(eleve, key=lambda x: x['Distance'])

copie = voisins[:k]
affichage(copie)






'''DEFAULT
• Courage : 9 Ambition : 2 Intelligence : 8 Good : 9
• Courage : 6 Ambition : 7 Intelligence : 9 Good : 7
• Courage : 3 Ambition : 8 Intelligence : 6 Good : 3
• Courage : 2 Ambition : 3 Intelligence : 7 Good : 8
• Courage : 3 Ambition : 4 Intelligence : 8 Good : 8
'''