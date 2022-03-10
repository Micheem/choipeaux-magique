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
    table: liste de dictionnaire contenant l_entierté des élèves
    eleve: dictionnaire contenant un élève et ses caractéristiques
    
    
    
DEBUT_FONCTION ajout_distance(table, distance):
    
    POUR eleves DANS table:
        eleves['Distance'] = round(distance(eleve, eleves), 2)
    FIN_POUR
    RETOURNER poudlard_characters

_______________________________________________________________________________________
VARIABLE:
    table : liste de dictionnaire contenant l_entierté des élèves.
    
    eleve_cible : dictionnaire contenant l_élève font on veut trouver la maison.
    
    k : entier, nombre de voisin(s).
    
    eleve_cible_distance : liste de dictionnaire contenant l_entierté des élèves
                           avec leur descripteur 'distance' selon l_eleve cible.
                           
    voisins : liste de dictionnaire contenant l_entierté des élèves
              trier avec leur descripteur 'distance' selon l_eleve cible.
    
    copie : liste de dictionnaire contenant les 'k' premiers dictionnaire de
            la table voisins.
    
    redondance_g : entier, nombre de fois où apparaît la maison Gryffindor.
    redondance_h : entier, nombre de fois où apparaît la maison Hufflepuff.
    redondance_s : entier, nombre de fois où apparaît la maison Slytherin.
    redondance_r : entier, nombre de fois où apparaît la maison Ravenclaw.
    
    liste_redondance : liste contenant tout les redondances par maison.
    
    house : chaîne de caractère contenant la maison d_un des élèves de
            notre table 'copie'.
    
    sa_maison : chaine de caractère, ce sera la maison de l_eleve cible.
    
    
    
DEBUT_FONCTION maison(table, eleve_cible, k):
    
    eleve_cible_distance <- ajout_distances(table, eleve_cible)
    voisins <- sorted(eleve_cible_distance, key=lambda x: x['Distance'])
    copie <- voisins[:k]
    redondance_g <- 0
    redondance_h <- 0
    redondance_r <- 0
    redondance_s <- 0
    
    POUR dico DANS copie:
         house <- dico['House']

        SI house = 'Gryffindor':
            redondance_g <- redondance_g + 1

        SINON_SI house = 'Hufflepuff':
            redondance_h <- redondance_h + 1

        SINON_SI house = 'Slytherin':
            redondance_s <- redondance_s + 1

        SINON:
            redondance_r <- redondance_r + 1
    FIN_POUR
    
    
    liste_redondance <- [redondance_s, redondance_g, redondance_h, redondance_r]
    
    liste_redondance.sort(reverse=True)
    
    
    SI liste_redondance[0] = redondance_g:
        sa_maison <- 'Gryffindor'

    SINON_SI liste_redondance[0] = redondance_h:
        sa_maison <- 'Hufflepuff'

    SINON_SI liste_redondance[0] = redondance_s:
        sa_maison <- 'Slytherin'

    SINON liste_redondance[0] = redondance_r:
        sa_maison <- 'Ravenclaw'
        
    RETOURNER sa_maison


