#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import turtle

# Les accords majeurs
A = ("X",0,2,2,2,0, "A", "LA")
B = ("X", 2, 4,4,4,2, "B", "SI")
C = ("X",3,2,0,1,0,"C", "DO")
D = ("X","X",0,2,3,2, "D", "RE")
E = (0,2,2,1,0,0, "E", "MI")
F = ("X", "X", 3,2,1,1, "F", "FA")
G = (3,2,0,0,0,1, "G", "SOL")

# Vitesse de la tortue
turtle.speed(0)

def dessine_moi_un_manche(x,y, largeur):
    """
    Fonction dessinant le manche de la guitare
    :param x: position x (integer)
    :param y: position y (integer)
    :param largueur: largeur case du manche (integer)
    :return:
    """

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


def dessine_moi_un_accord(accord, x, y, largeur):
    """
    Fonction représentant la tablature de l'accord
    :param accord: Tuple Accord de tablature encodé + Notation Américaine + Notation Française
    :param x: Coordonnée X du manche
    :param y: Coordonnée y du manche
    :return:
    """

    ybase = y
    for i in range(len(accord)-2) :
        if isinstance(accord[i], int):
            y = ybase - (accord[i] * largeur) + (largeur/2)
            turtle.goto(x, y)
            print(accord[i])
            # Corde à vide, on fait un cercle
            if accord[i] == 0:
                turtle.dot(20, 'blue')
                turtle.dot(16, 'white')

            # Corde pincée, on met un point
            else:
                turtle.dot(20, 'blue')
        else:
            y = 100 + 12.5
            turtle.goto(x, y)
            turtle.dot(20,'red')
            turtle.dot(16,'white')
        x = x + 25

        turtle.goto(x, y)
    turtle.goto(-70,-30)
    turtle.write(accord[len(accord)-2] + ' --- ' + accord[len(accord)-1], font=("Arial", 14, "bold"))



# =========================================
#            Fin des fonctions
# =========================================

dessine_moi_un_manche(-100, 100, 25)
dessine_moi_un_accord(G, -100, 100, 25)
turtle.hideturtle()


turtle.done()








