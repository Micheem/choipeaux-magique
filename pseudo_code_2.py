VARIABLE:
    eleve1: dictionnaire contenant les caractéristiques d_un élève
    eleve2: dictionnaire contenant les caractéristiques d_un élève



DEBUT_FONCTION distance(eleve1, eleve2):
    
    RETOURNER racine carré de (eleve1['Courage'] - eleve2['Courage']) ** 2
                            + (eleve1['Ambition'] - eleve2['Ambition']) ** 2
                            + (eleve1['Intelligence'] - eleve2['Intelligence']) ** 2
                            + (eleve1['Good'] - eleve2['Good']) ** 2)
FIN_FONCTION distance

_______________________________________________________________________________________
VARIABLE:
    table (en entrée): liste de dictionnaire contenant l_entierté des élèves
    eleve: dictionnaire contenant un élève et ses caractéristiques
    k : entier, nombre de voisins
    voisins : liste de dictionnaire contenant l_entierté des élèves trier selon leur distance
    table (en sortie): liste de dictionnaire contenant les k plus proche voisins
    
DEBUT_FONCTION kkpv(table, distance, k):
    
    POUR eleves DANS table:
        eleves['Distance'] = arrondir(distance(eleve, eleves), 2)
    FIN_POUR

    voisins <- trier(table, key=lambda x: x['Distance'])
    table <- voisins[:k]

    RETOURNER table

FIN_FONCTION kkpv

