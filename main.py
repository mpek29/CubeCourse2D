# -- coding: utf-8 --

##################
# Projet IPI     #
# S2p 2021       #
# PASCO Florian  #
# LECLERS Simon  #
##################

import termios
import sys
import tty
import time
import select

import Level
import Score
import Player
import Timer

# Interactions clavier
old_settings = termios.tcgetattr(sys.stdin)

# Données du jeu
scene = 0
homelevel = None
gamelevel = None
endbackground = None
timeStep = None
score = None
player = None
timer = None

end = None

### Général ###
def init():
    global homelevel, gamelevel, timeStep, score, scene, player, timer, end

    # enlève le curseur
    sys.stdout.write("\033[?25l")

    # initialisation de la partie
    timeStep = 0.2
    end = False

    # creation des elements du jeu
    homelevel = Level.createHome()
    gamelevel = Level.createGame()
    score = Score.create()
    player = Player.create()
    timer = Timer.create()

    # interaction clavier
    tty.setcbreak(sys.stdin.fileno())

# Affichage
def show():
    global homelevel, score, scene, gamelevel, endlevel, timer, player, end

    # rafraichissement de l'affichage

    # effacer la console
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[2J")

    # affichage des differents elements du Home
    if scene == 0:
        Level.show(homelevel, "Home", score)

    # affichage des differents elements du Jeu
    if scene == 1:
        Level.show(gamelevel, "Game")
        Timer.show(timer)  # On affiche le timer
        # Si le player tombe dans le vide
        if Player.show(player, Level.getBackground(gamelevel)) == False:
            # On enregistre son temps
            Score.setTime(score, int(Score.getTime(timer)))
            Score.setFormattedTime(score, Timer.timeFormatting(
                Score.getTime(timer)))  # On enregistre son temps formaté
            Score.addToSauvegarde(score)
            scene = 2

    # affichage des differents elements de la fin du jeu
    if scene == 2 and end:
        Level.show(endlevel)

    # restoration couleur
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")

    # deplacement curseur
    sys.stdout.write("\033[0;0H\n")

# Boucle de simu
def run():
    global timeStep, scene, end

    # Boucle de simulation
    while scene == 0 or scene == 1:
        if scene == 0:
            t0 = time.time()
            interactHome()
            show()
            time.sleep(timeStep - (time.time() - t0))
        if scene == 1:
            t0 = time.time()
            interactGame()
            show()
            time.sleep(timeStep - (time.time() - t0))
    while scene == 2 and end == True:
        if scene == 2:
            t0 = time.time()
            interactEnd()
            show()
            time.sleep(timeStep - (time.time() - t0))

# Récuperation évènements clavier
def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

# Quitter le programme
def quit():
    # Remet le curseur
    sys.stdout.write("\033[?25h")

    # Restoration parametres terminal
    global old_settings

    # Couleur white
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    sys.exit()

### Scene 1 : Home ###
def interactHome():
    global score, scene

    # gestion des evenement clavier
    # si une touche est appuyee
    if isData():
        c = sys.stdin.read(1)
        if c == '\x20' and Score.getName(score) != "":  # x20 is SPACE
            scene = 1
        elif c == '\x1b':  # x1b is ESC
            quit()
        # x7f is Delete character
        elif c == '\x7f' and len(Score.getName(score)) < 24:
            # On retire le dernier élement du nom
            Score.setName(score, Score.getName(score)[:-1])
        else:
            Score.setName(score, Score.getName(score) + c)

### Scene 2 : Game ###
def interactGame():
    global gamelevel, player, timer, timeStep
    # gestion des evenement clavier
    # si une touche est appuyee
    # On ajoute le temps suplémentaire au compteur
    Timer.newTurn(timer, timeStep)
    if isData():
        c = sys.stdin.read(1)
        if c == '\x1b':         # x1b is ESC
            quit()
        if c == '\x20':
            Player.jump(player, Level.getBackground(gamelevel))
            Player.changeShape(player)

### Scene 3 : End ###
def initEnd():
    global endlevel, end, t0

    # creation des elements du jeu
    endlevel = Level.createEnd()

    end = True
    t0 = time.time()

# Interactions écran de fin
def interactEnd():
    global scene, end, t0
	# Gestion des evenement clavier
	# Si une touche est appuyee
    if isData() :
        c = sys.stdin.read(1)
        if c == '\x1b':         # x1b is ESC
            quit()
        elif c == '\x20':
            end = False
            scene = 1


######################################
while 1:
    init()
    run()
    time.sleep(0.8)
    initEnd()
    run()
