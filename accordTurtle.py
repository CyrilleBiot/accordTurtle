#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle

# Les accords majeurs
dictAccord = {
    "A" : ("X",0,2,2,2,0, "A", "LA"),
    "B" : ("X", 2, 4,4,4,2, "B", "SI"),
    "C" : ("X",3,2,0,1,0,"C", "DO"),
    "D" : ("X","X",0,2,3,2, "D", "RE"),
    "E" : (0,2,2,1,0,0, "E", "MI"),
    "F" : ("X", "X", 3,2,1,1, "F", "FA"),
    "G" : (3,2,0,0,0,1, "G", "SOL")
    }
# Tuple contenant : position x, position y et la largeur d'une case de manche
position = (-100, 100, 25)
# Vitesse de la tortue
speed = 0

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
    turtle.color('red', 'yellow')
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
    for i in range(len(accord)-2) :
        if isinstance(accord[i], int):
            y = ybase - (accord[i] * largeur) + (largeur/2)
            turtle.goto(x, y)
            print(accord[i])
            # Corde à vide, on fait un cercle
            if accord[i] == 0:
                turtle.dot(largeur - 5, 'blue')
                turtle.dot(largeur - 10, 'white')

            # Corde pincée, on met un point
            else:
                turtle.dot(largeur - 5, 'blue')
        else:
            y = ybase + (largeur/2)
            turtle.goto(x, y)
            turtle.dot(largeur - 5,'red')
            turtle.dot(largeur - 10,'white')
        x = x + largeur
        turtle.goto(x, y)
    # Ligne à revoir
    turtle.goto(xbase + largeur,(ybase - (5 * largeur)))
    turtle.write(accord[len(accord)-2] + ' --- ' + accord[len(accord)-1], font=("Arial", 14, "bold"))

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
