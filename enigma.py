#enigma1

# CODE POUR L'INTERFACE

# VARIABLES
valeurBaseCles = []
valeurDecalage = []
messageCode = ""
messageDecoder = ""
reponseValide = True
nombreCles = ["1er", "2e", "3e", "4e"]

def encoder_Affichage():
  iterationCles = 0
  while iterationCles <= 3:
    tempCles = int(input(print(f"Quelle est la valeur de base de la {nombreCles[iterationCles]} ? ")))
    valeurBaseCles.append(tempCles)
    iterationCles += 1

    

def decoder_Affichage():
  print("zeub")

def question_de_depart():
  print("Bienvenue sur ENIGMA ! \n\n")
  while reponseValide != True:
    rep = chr(input("Souhaiter vous encoder (e) ou decoder (d) ou quitter (q) ? "))
    if rep == 'q':
      quitter = True
    elif rep == 'e':
      encoder_Affichage()
    elif rep == 'd':
      decoder_Affichage()
    else:
      reponseValide = False
      print("Pas un choix valide ressayer \n\n")


      