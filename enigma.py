#enigma1

# CODE POUR L'INTERFACE

# VARIABLES
valeurBaseCles = []
valeurDecalage = []
messageCode = ""
messageDecoder = ""
# reponseValide = False
nombreCles = ["1er", "2e", "3e", "4e"]

def encoder_Affichage():
  iterationCles = 0
  while iterationCles <= 3:
    tempCles = int(input(f"Quelle est la valeur de base de la {nombreCles[iterationCles]} cles ? "))
    valeurBaseCles.append(tempCles)
    iterationCles += 1
  print(valeurBaseCles)

    

def decoder_Affichage():
  print("zeub")

def question_de_depart():
  reponseValide = False
  quitter = False
  print("Bienvenue sur ENIGMA ! \n\n")
  while reponseValide == False and quitter == False:
    rep = str(input("Souhaiter vous encoder (e) ou decoder (d) ou quitter (q) ? "))
    if rep == 'q':
      quitter = True
    elif rep == 'e':
      encoder_Affichage()
    elif rep == 'd':
      decoder_Affichage()
    else:
      reponseValide = False
      print("Pas un choix valide ressayer \n\n")

question_de_depart()
      