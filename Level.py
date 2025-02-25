# -- coding: utf-8 --

##################
# Projet IPI     #
# S2p 2021       #
# PASCO Florian  #
# LECLERS Simon  #
##################


import random
import sys
import json

import Score

# Le module Level gère le type abstrait de donnée level 

# Création menu départ
def createHome():
    #creation du fond
    bg=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'U', 'B', 'E', ' ', 'C', 'O', 'U', 'R', 'S', 'E', ' ', '2', 'D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', 'N', 'T', 'R', 'E', 'Z', ' ', 'V', 'O', 'T', 'R', 'E', ' ', 'N', 'O', 'M', ':', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '‾', '‾', '‾'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '‾', '‾', '‾', '‾', '‾', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '‾', '‾', '‾', '‾', ' ', ' ', ' ', ' ', '‾', '‾', '‾', '‾', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['‾', '‾', '‾', '‾', ' ', ' ', ' ', '‾', '‾', '‾', '‾', ' ', ' ', ' ', ' ', '‾', '‾', '‾', '‾', '‾', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', 'P', 'P', 'U', 'Y', 'E', 'Z', ' ', 'S', 'U', 'R', ' ', '"', 'E', 'S', 'P', 'A', 'C', 'E', '"', ' ', 'P', 'O', 'U', 'R', ' ', 'C', 'O', 'M', 'M', 'E', 'N', 'C', 'E', 'R', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
   
    #creation Level
    Level=dict()
    Level["bg"]= bg
    
    return Level

# Création menu de fin
def createEnd():
    #creation du fond	
    bg=[
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'U', 'B', 'E', ' ', 'C', 'O', 'U', 'R', 'S', 'E', ' ', '2', 'D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ','#', '1', ' ', '6', '6', ':', '6', '6', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  
    [' ', ' ', ' ', ' ', ' ', ' ','#', '2', ' ', '6', '6', ':', '6', '6', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  
    [' ', ' ', ' ', ' ', ' ', ' ','#', '3', ' ', '6', '6', ':', '6', '6', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  
    [' ', ' ', ' ', ' ', ' ', ' ','#', '4', ' ', '6', '6', ':', '6', '6', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  
    [' ', ' ', ' ', ' ', ' ', ' ','#', '5', ' ', '6', '6', ':', '6', '6', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', 'P', 'P', 'U', 'Y', 'E', 'Z', ' ', 'S', 'U', 'R', ' ', '"', 'E', 'S', 'P', 'A', 'C', 'E', '"', ' ', 'P', 'O', 'U', 'R', ' ', 'R', 'E', 'L', 'A', 'N', 'C', 'E', 'R', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', 'U', ' ', 'E', 'C', 'H', 'A', 'P', ' ', 'P', 'O', 'U', 'R', ' ', 'Q', 'U', 'I', 'T', 'T', 'E', 'R', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    with open('sauvegardes.txt', 'r') as file:
        sauvegarde = json.load(file)

    def get_time(sauvegarde):
        return sauvegarde.get('time')
        sauvegarde.sort(key=get_time, reverse=True)

    for i in range(len(sauvegarde)*2):
        if i%2 == 0 :
            for j in range(len(sauvegarde[int(i/2)]['formattedTime'])) :
                bg[i+3][j+9] = sauvegarde[int(i/2)]['formattedTime'][j]
            for j in range(len(sauvegarde[int(i/2)]['name'])) :
                bg[i+3][j+17] = sauvegarde[int(i/2)]['name'][j]

    #creation Level
    Level=dict()
    Level["bg"]= bg
    return Level

# Création background jeu
def createGame():
    # Création grille nomée "cases"
    bg = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'U', 'B', 'E', ' ', 'C', 'O','U', 'R', 'S', 'E', ' ', '2', 'D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', 'T', 'e', 'm', 'p', 's', ':', ' ', '0', '0', ':', '0', '0', ' ', '|', ' ', 'M', 'e', 'i','l', 'l', 'e', 'u', 'r', ' ', 't', 'e', 'm', 'p', 's', ':', ' ', '0', '4', ':', '5', '8', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

    # Ajout des plateformes au bg
    Plat = generate(300)
    for p in range(len(Plat)):
        ligneT = Plat[p]
        bg.append(ligneT)

    #Creation Level
    Level=dict()
    Level["bg"]= bg
    
    return Level


# Génération des platformes
def generate(longueur):
    # On mets des espaces partout
    pl = []
    for hau in range(9):
        pl.append([])
        for lon in range(longueur + 1):
            pl[hau].append(' ')

    # Plateforme de base
    pl[4][0] = '‾'
    pl[4][1] = '‾'
    pl[4][2] = '‾'
    pl[4][3] = '‾'

    # Fonction random pourcentage
    def ranP(min, max, pM, pP):
        # Valeur rand
        val = 0

        # Négatif / positif
        p = []
        for i in range(pM):
            p.append(0)
        for i in range(pP):
            p.append(1)

        # Random neg / pos
        signe = p[random.randint(0, len(p) - 1)]

        # Valeur
        if signe == 0:
            val = random.randint(min, 0)
        else:
            val = random.randint(1, max)

        return val

    # Valeurs reférence génération
    # Format : [min, max, proba- (%/10), proba+ (%/10)]
    diffH = [[], [], [], [-3, 2, 3, 7], [-2, 2, 5, 5], [-2, 1, 6, 4]]
    tailles = [5, 3, 4, 3, 3, 4, 5, 4, 3, 3]

    # Génération
    hDebut = 4
    hCourant = 4
    xCourant = 3

    # Position : pl[len(pl) - hCourant][xCourant]
    while xCourant < len(pl[0]):
        if xCourant < len(pl[0]) - 6:  # Corps avant la fin
            # Distance plateforme
            distP = random.randint(3, 5)

            # Hauteur plateforme (par rapport à la hauteur actuelle, en fonction de la distance)
            hautP = ranP(diffH[distP][0], diffH[distP][1], diffH[distP][2], diffH[distP][3])

            # Taille plateforme
            longP = tailles[random.randint(0, len(tailles) - 1)]

            # Variable écart réel
            xBase = xCourant
            possible = False

            # Possibilité ajout ennemi 
            ennemi = False # Ennemi à afficher
            etpEnnemi = 0 # Etape affichage ennemi
            if longP >= 3 and abs(hautP) < 3:
                # 1 chance sur 6 de générer un ennemi
                rand = random.randint(0, 12)
                if rand > 10 :
                    ennemi = True


            # Ajout plateforme dans la liste
            for p in range(longP):
                # Variables emplacement
                xAct = xBase + distP + p
                hAct = len(pl) - (hCourant + hautP)

                # Vérifs out of range
                if hAct >= len(pl):
                    hAct = len(pl) - 1
                elif hAct < 0:
                    hAct = 0

                # Si l'affichage est possible
                lPossible = len(pl[0]) - 6 - xAct
                if lPossible > 3 :
                    # Ajout liste
                    if xAct < len(pl[0]) - 6 or xCourant - xBase < 2:
                        pl[hAct][xAct] = '‾'
                        xCourant += 1

                    # Affichage ennemi
                    if ennemi and hAct > 0 :
                        # Longueur affichage supérieure ou = à 3
                        if lPossible >= 3 :
                            # Début affichage
                            if longP == 3 :
                                if p == 0 :
                                    etpEnnemi = 1
                            elif longP == 4 :
                                if p == 1 :
                                    etpEnnemi = 1
                            elif longP == 5 :
                                if p == 2 :
                                    etpEnnemi = 1

                            # Etapes affichage
                            if etpEnnemi == 1 :
                                pl[hAct-1][xAct] = '╔'
                                etpEnnemi += 1
                            elif etpEnnemi == 2 :
                                pl[hAct-1][xAct] = '0'
                                etpEnnemi += 1
                            elif etpEnnemi == 3 :
                                pl[hAct-1][xAct] = '╝'
                                etpEnnemi += 1
                    # Variable affichage possible
                    possible = True

            # Incrémentation
            # xCourant += distP + longP - 1
            xCourant += distP - 1
            if possible:
                hCourant += hautP
                if(hCourant < 0):
                    hCourant = 0
                elif hCourant >= len(pl):
                    hCourant = len(pl) - 1
        else:  # Derniers blocs, adaptation hauteur avec le début
            xCourant = len(pl[0]) - 6
            hActu = len(pl) - hCourant

            if hActu == hDebut:  # Hauteur de fin même que celle de début
                # Ajout plateforme plate à la hauteur
                for p in range(4):
                    # Variables emplacement
                    xAct = xCourant + 2 + p
                    hAct = len(pl) - hCourant

                    # Ajout liste
                    if xAct < len(pl[0]):
                        pl[hAct][xAct] = '‾'
                        # pl[hAct][xAct] = 'N'
                break
            elif hActu > hDebut:  # Hauteur de fin inférieure à celle de début
                hMilieu = int((hCourant+1 + hDebut)/2)

                # Ajout plateforme plate h milieu
                for p in range(4):
                    # Variables emplacement
                    xAct = xCourant + p
                    hAct = len(pl) - hMilieu

                    # Ajout liste
                    if xAct < len(pl[0]):
                        pl[hAct][xAct] = '‾'
                        # pl[hAct][xAct] = 'N'

                break
            else:  # Hauteur de fin supérieure à celle de début
                hMilieu = int((hCourant-1 + hDebut)/2)

                # Ajout plateforme plate h milieu
                for p in range(4):
                    # Variables emplacement
                    xAct = xCourant + 2 + p
                    hAct = len(pl) - hMilieu

                    # Ajout liste
                    if xAct < len(pl[0]):
                        pl[hAct][xAct] = '‾'
                        # pl[hAct][xAct] = 'N'

                break
        # Fin boucle

    # Renvoi
    return pl


# Afficher plateformes
def show(l, type = None, score = None) :  
    bg = getBackground(l)
    
    # On se positionne dans le terminal
    sys.stdout.write("\033[1;1H")
    
    # Couleur fond cyan
    sys.stdout.write("\033[46m")

    # Couleur interface
    txt="\033[30m"
    sys.stdout.write(txt)

    # Affichage
    for i in range (len(bg)):
        for j in range (len(bg[0])):
            sys.stdout.write(bg[i][j])
        sys.stdout.write("\n")

    # Si on affiche l'accueil
    if type == "Home":
        y = str(int(25 - len(Score.getName(score))/2))
        txt="\033[8;" + y + "H"
        sys.stdout.write(txt)
        if len(Score.getName(score)) > 0 and Score.getName(score)[0] == " ":
            Score.setName(score,Score.getName(score)[:0])
        sys.stdout.write(Score.getName(score))
    
    # Si on affiche le jeu
    if type == "Game":
        lignesJeu = bg[4:13]
        for li in range(len(lignesJeu)):
            elementSuppr = lignesJeu[li].pop(0)
            lignesJeu[li].append(elementSuppr)
            for ligne in range(4, len(bg)):
                bg[ligne] = lignesJeu[ligne - 4]
                setBackground(l,bg)


# Accesseurs
def getBackground(l):
    return l['bg']


# Mutateurs
def setBackground(l,bg):
    l['bg']= bg