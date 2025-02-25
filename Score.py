# -- coding: utf-8 --


##################
# Projet IPI     #
# S2p 2021       #
# PASCO Florian  #
# LECLERS Simon  #
##################

import json

# Le module score gere le type abstrait de donnée score 

# Créer un score
def create():
	# Création Score
	Score = dict()
	Score["name"] = ""
	Score["time"] = 0
	Score["formattedTime"] = ""
	
	return Score

# Obtenir le meilleur temps
def getBestTime():
	with open('sauvegardes.txt', 'r') as file:
		sauvegarde = json.load(file)
	# Trier les scores de façon croissante
	sauvegarde.sort(key = get_time, reverse = True)
	return sauvegarde[0]["formattedTime"]

# Obtenir le temps d'une sauvegarde
def get_time(sauvegarde):
	return sauvegarde.get('time')

# Ajouter un score à la sauvegarde
def addToSauvegarde(score):
	with open('sauvegardes.txt', 'r') as file:
		sauvegarde = json.load(file)
	sauvegarde.append(score)
	#trier les scores de façon croissante
	sauvegarde.sort(key = get_time, reverse = True)
	sauvegarde = sauvegarde[:5]
	#Pour enregistrer le dictionnaire dans un fichier :
	with open('sauvegardes.txt', 'w') as file:
	   json.dump(sauvegarde, file)


# Accesseurs
def getName(s):
    return s['name']

def getTime(s):
    return s['time']

def getformattedTime(s):
    return s['formattedTime']


# Mutateurs
def setName(s, n):
    s['name']= n

def setTime(s, t):
    s['time']= t

def setFormattedTime(s, ft):
    s['formattedTime']=ft