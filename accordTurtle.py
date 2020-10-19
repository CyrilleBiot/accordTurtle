#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__copyright__ = "Copyleft"
__credits__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__license__ = "GPL"
__version__ = "0.1"
__date__ = "2020/10/19"
__maintainer__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__email__ = "cyrille@cbiot.fr"
__status__ = "Devel"
"""

import turtle

# Tuple contenant : position x, position y et la largeur d'une case de manche
largeur = 25
position = (-100, 100, largeur)
varLargeur = largeur / 25
colorLine = "red"
colorBack = "yellow"
colorDote0 = 'red'
colorDoteX = "blue"
fontSizeName = 12 * varLargeur
fontSizeDot = 8 * varLargeur

# Vitesse de la tortue
speed = 0

# Les accords majeurs
dictAccord = {
    "A" : ("X",0,(2,1),(2,2),(2,3),0, "A", "LA"),
    "B" : ("X", (2,1),(4,2),(4,3),(4,4),(2,1), "B", "SI"),
    "C" : ("X",(3,3),(2,2),0,(1,1),0,"C", "DO"),
    "D" : ("X","X",0,(2,1),(3,2),(2,3), "D", "RE"),
    "E" : (0,(2,3),(2,2),(1,1),0,0, "E", "MI"),
    "F" : ("X", "X", (3,3),(2,2),(1,1),(1,1), "F", "FA"),
    "G" : ((3,1),(2,2),0,0,0,(1,3), "G", "SOL")
    }


# Les fonctions
def dessine_moi_un_manche(position):
    """
    Fonction dessinant le manche de la guitare
    :param position: Tuple contenant : position x, position y et la largeur d'une case de manche
    :return:
    """
    # Extrait les données du tuple
    x,y,largeur = position

    # Positionnement et dessin de la fret
    turtle.penup()
    turtle.goto(x,y)
    turtle.color(colorLine, colorBack)
    turtle.pensize(3)
    turtle.pendown()
    turtle.forward(largeur*5)
    turtle.penup()
    turtle.goto(x, y)

    # Dessin des 4 premières cases
    turtle.pensize(1)

    # Mise en mémoire de la valeur par défaut de X
    xbase = x
    for i in range(4):
        turtle.goto(x,y)
        for i in range(5):
            turtle.goto(x,y)
            turtle.begin_fill()
            for i in range(4):
                turtle.pendown()
                turtle.forward(largeur)
                turtle.left(-90)
                turtle.penup()
            turtle.end_fill()
            x = x + largeur
        y = y - largeur
        x = xbase


def dessine_moi_un_accord(accord, position):
    """
    Fonction représentant la tablature de l'accord
    :param accord: Tuple Accord de tablature encodé + Notation Américaine + Notation Française
    :param position: Tuple contenant : position x, position y et la largeur d'une case de manche
    :return:
    """
    # Extrait les données du tuple
    x, y, largeur = position
    # Recupere les valeurs par défaut de X et de Y
    ybase = y
    xbase = x

    # On parcourt l'entrée du dictionnaire correspondant à l'accord
    for i in range(len(accord)-2) :

        # Le tuple contient un string, c'est une corde à vide
        if isinstance(accord[i], str):
            y = ybase + (largeur/2)
            turtle.goto(x, y)
            #turtle.dot(largeur - 10, colorDote0)
            #turtle.dot(largeur - 15,'white')
            turtle.goto(x - (0.5 * fontSizeDot), y - fontSizeDot)
            turtle.write("X", font=("Arial", int(fontSizeName), "bold"))

        # L'entrée du tuple contient soit un integer, soit un tuple, c'est une corde à jouer
        else:

            # l'entrée est un 0 (integer):
            # Corde à vide, on fait un cercle
            if accord[i] == 0:
                y = ybase - (accord[i] * largeur) + (largeur / 2)
                turtle.goto(x, y)
                turtle.dot(largeur - 10, colorDoteX)
                turtle.dot(largeur - 15, 'white')

            # L'intrée est un tuple de 2 integers ->
            # -------> premier chiffre :  n° case à pincer
            # -------> premier chiffre :  n° du doigt à utiliser
            # Corde pincée,
            else:
                y = ybase - (accord[i][0] * largeur) + (largeur / 2)
                turtle.goto(x, y)
                turtle.dot(largeur - 5, colorDoteX)
                posX = turtle.xcor()
                posY = turtle.ycor()
                turtle.goto(x - (0.2 * fontSizeDot), y - (0.75 * fontSizeDot))
                #turtle.goto(x-(largeur/8), y-(largeur/4))
                turtle.color('white', 'yellow')
                turtle.write(accord[i][1], font=("Arial", int(fontSizeDot), "bold"))
                turtle.color('red', 'yellow')
        x = x + largeur
        turtle.goto(x, y)
    # Ligne à revoir
    turtle.goto(xbase + largeur,(ybase - (5 * largeur)))
    turtle.write(accord[len(accord)-2] + ' --- ' + accord[len(accord)-1], font=("Arial", int(fontSizeName), "bold"))

# ===================================================================================================================
# LANCEMENT PROGRAMME
# ===================================================================================================================

listeAccords ='Accords disponibles : '
for cle in dictAccord:
    listeAccords += cle + ' '
print(listeAccords)

while True:
       try:
           accordDemande = input("Quel accord afficher ? ")
           if accordDemande.upper() in dictAccord.keys():
               accord = dictAccord[accordDemande.upper()]
               print("Accord demandé : " , accord)
               print(type(accord))
               print(accord)
               break
           else:
               print('Accord non géré.')
               print(listeAccords)
       except ValueError:
           print("Oops!  Réponse incorrecte... Réessayer...")

#
# Execution avec turtle
#

# Vitesse de la tortue
turtle.speed(speed)
dessine_moi_un_manche(position)
dessine_moi_un_accord(accord, position)
turtle.hideturtle()
turtle.done()
