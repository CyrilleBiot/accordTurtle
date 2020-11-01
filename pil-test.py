#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__copyright__ = "Copyleft"
__credits__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__license__ = "GPL"
__version__ = "0.1"
__date__ = "2020/10/21"
__maintainer__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__email__ = "cyrille@cbiot.fr"
__status__ = "Devel"
"""

from PIL import Image, ImageDraw, ImageFont

x,y = 150, 150
l = 40
xbase = x
ybase = y

colorLine = "red"
colorBack = "yellow"
colorBackCircle = "blue"

dictAccord = {
    "A" : ("X",0,(2,1),(2,2),(2,3),0, "A", "LA"),
    "B" : ("X", (2,1),(4,2),(4,3),(4,4),(2,1), "B", "SI"),
    "C" : ("X",(3,3),(2,2),0,(1,1),0,"C", "DO"),
    "D" : ("X","X",0,(2,1),(3,2),(2,3), "D", "RE"),
    "E" : (0,(2,3),(2,2),(1,1),0,0, "E", "MI"),
    "F" : ("X", "X", (3,3),(2,2),(1,1),(1,1), "F", "FA"),
    "G" : ((3,1),(2,2),0,0,0,(1,3), "G", "SOL")
    }

def creer_image():
    # Création d'une image
    image = Image.new('RGBA', (400, 400), (255,255,255))
    # Création d'un espace de dessin
    draw = ImageDraw.Draw(image)
    return image, draw

def dessine_moi_un_manche(draw, x,y,l):
    xbase = x
    # Dessin du manche
    draw.line([(x,y),(x + (5* l),y)], fill=colorLine, width=5)
    for i in range(4):
        for i in range(5):
            draw.rectangle([(x,y),(x+l,y+l)], fill=colorBack, outline=colorLine)
            x = x + l
        x = xbase
        y = y + l

def dessine_moi_un_accord(draw, accord, x,y,l):
    # Recupere les valeurs par défaut de X et de Y
    ybase = y
    xbase = x

    # On parcourt l'entrée du dictionnaire correspondant à l'accord
    for i in range(len(accord)-2) :

        # Le tuple contient un string, c'est une corde à vide
        if isinstance(accord[i], str):
            fontPath = '/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf'
            fontSize = 40
            font = ImageFont.truetype(fontPath, 40)
            draw.text((x - 1/3 * fontSize,  y - fontSize * 8/7 ), "X", font=font, fill='red')


        # L'entrée du tuple contient soit un integer, soit un tuple, c'est une corde à jouer
        else:

            # l'entrée est un 0 (integer):
            # Corde à vide, on fait un cercle
            if accord[i] == 0:
                draw.ellipse((x - 3 / 8 * l , y - 7 / 8 * l , x + 3 / 8 * l , y - 1 / 8 * l ),
                             fill=colorBackCircle, outline=colorLine)

            # L'intrée est un tuple de 2 integers ->
            # -------> premier chiffre :  n° case à pincer
            # -------> premier chiffre :  n° du doigt à utiliser
            # Corde pincée,
            else:
                draw.ellipse((x - 3 / 8 * l , (y - 7 / 8 * l) +  accord[i][0] * l  , x + 3 / 8 * l , (y - 1 / 8 * l) +  accord[i][0] * l ),
                             fill=colorBackCircle, outline=colorLine)
        x = x + l
    fontPath ='/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf'
    font = ImageFont.truetype(fontPath, 40)
    draw.text((50,50), accord[len(accord)-1] + " / " + accord[len(accord)-2], font=font, fill='red')

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

image, draw = creer_image()
dessine_moi_un_manche(draw, x,y,l)
dessine_moi_un_accord(draw, accord,x,y,l)

image.show()
