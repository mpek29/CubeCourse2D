# -- coding: utf-8 --


##################
# Projet IPI     #
# S2p 2021       #
# PASCO Florian  #
# LECLERS Simon  #
##################

import sys

# Le module player gere le type abstrait de donnée player
# Un player est un objet qui se déplace dans le terminal 

doubleJump = False

# Créer le player
def create():
	# Creation Player
	Player=dict()
	Player["position"]= [1,7]
	Player["color"]= 7
	Player["shape"]= True
	
	return Player
 
# Afficher le player
def show(p, bg) : 
	# On se place a la position du player dans le terminal
	x=str(int(p["position"][0]) + 1 )
	y=str(int(p["position"][1]) + 1 )
	txt="\033["+y+";"+x+"H"
	sys.stdout.write(txt)
	
	# Couleur animat
	c=p["color"]
	txt="\033[3"+str(c)+"m"
	sys.stdout.write(txt)

	# Affichage de l animat
	if p["shape"] :
		sys.stdout.write("╔0╝\n")
	else :
		sys.stdout.write( "╚0╗\n")
	return gravity(p, bg)

# Gérer la gravité
def gravity(p, bg):
	PlayerPosition = getPosition(p)

	if PlayerPosition[1] == len(bg) - 1 or bg[PlayerPosition[1]][PlayerPosition[0]+1] == "╔" :
		return False
	elif bg[PlayerPosition[1]+1][PlayerPosition[0]] == ' ' and bg[PlayerPosition[1]+1][PlayerPosition[0]+1] == ' ' and bg[PlayerPosition[1]+1][PlayerPosition[0]-1] == ' ':
		setPosition(p,PlayerPosition[0],PlayerPosition[1] + 1)
		return True

# Obtenir la position du player
def getPosition(p) :
	return p["position"]

# Définir la position
def setPosition(p,x,y) :
	 p["position"]= [x,y]

# Sauter
def jump(p, bg):
	global doubleJump
	PlayerPosition = getPosition(p)
	if PlayerPosition[1] != len(bg) - 1 :
		spElement = ['╔', '╝', '0', '‾'] # Elements 'durs'
		isGrounded = bg[PlayerPosition[1]+1][PlayerPosition[0]] in spElement or bg[PlayerPosition[1]][PlayerPosition[0]+1] in spElement or bg[PlayerPosition[1]+1][PlayerPosition[0]-1] in spElement
		if  isGrounded: # Si on touche le sol
			doubleJump = True
		if  isGrounded or doubleJump: # Si on touche le sol ou que le saut est autorisé
			if (not isGrounded): # Si on ne touche pas le sol
				doubleJump = False
			setPosition(p,PlayerPosition[0],PlayerPosition[1]-2) # Alors on saute


# Modifier la forme
def changeShape(p) :
	p["shape"] = not p["shape"]