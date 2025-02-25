# -- coding: utf-8 --


##################
# Projet IPI     #
# S2p 2021       #
# PASCO Florian  #
# LECLERS Simon  #
##################

import sys

import Score

# Le module timer gere le type abstrait de donnée timer
# Un timer est un objet qui affiche le temps depuis le début de la partie


# Créer le timer
def create():
    # creation Timer
    Timer = dict()
    Timer["positiontime"] = [13, 1]
    Timer["positionbesttime"] = [37, 1]
    Timer["time"] = 0

    return Timer


# Afficher le timer
def show(t):
    # On se place a la position du timer dans le terminal
    x = str(int(t["positiontime"][0]) + 1)
    y = str(int(t["positiontime"][1]) + 1)
    txt = "\033["+y+";"+x+"H"
    sys.stdout.write(txt)

    # Affichage du Temps
    time = timeFormatting(t["time"])  # Retourne un texte au format 00:00
    sys.stdout.write("" + time + "\n")

    # On se place a la position du timer dans le terminal
    x = str(int(t["positionbesttime"][0]) + 1)
    y = str(int(t["positionbesttime"][1]) + 1)
    txt = "\033["+y+";"+x+"H"
    sys.stdout.write(txt)

    # Affichage du Meilleure Temps
    time = Score.getBestTime()  # Retourne un texte au format 00:00
    sys.stdout.write("" + time + "\n")


# Incrémenter le timer
def newTurn(t, timeStep):
    t["time"] = t["time"] + timeStep


# Formater le temps initialement en seconde en un texte prêt à être affiché
def timeFormatting(time):
    time = int(time)
    if time < 10:  # Moins de 10 secondes
        formattedSecond = "0" + str(time)
        formattedMinutes = "00"

    elif time < 60:  # Moins de 1minutes
        formattedSecond = str(time)
        formattedMinutes = "00"

    elif time >= 60:  # Plus de 1minutes
        # On gère d'abord les secondes
        second = time % 60  # Nombre de seconde non incoporée dans des minutes
        if second < 10:  # Moins de 10 secondes non incoporé
            formattedSecond = "0" + str(second)

        elif second >= 10:  # Plus de 10 secondes non incoporé
            formattedSecond = str(second)

        # On gère ensuite les minutes
        if time < 600:  # Moins de 10 minutes
            # Nombre de minutes (forcément inférieur à 10 ici)
            minutes = time//60
            formattedMinutes = "0" + str(minutes)

        elif time >= 600:  # Plus de 10minutes
            # Nombre de minutes (forcément supérieur à 10 ici)
            minutes = time//60
            formattedMinutes = str(minutes)

    formattedTime = formattedMinutes + ":" + formattedSecond
    return formattedTime


# Obtenir le temps dans une string
def getTime(t):
    return t["time"]
