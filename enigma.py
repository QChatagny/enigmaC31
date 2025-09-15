#enigma1

# CODE POUR L'INTERFACE

# VARIABLES
valeurBaseCles = []
valeurDecalage = []
messageDecoder = ""
# reponseValide = False
nombreCles = ["1er", "2e", "3e", "4e"]

def Affichage():
  iterationCles = 0
  while iterationCles <= 3:
    tempCles = int(input(f"Quelle est la valeur de base de la {nombreCles[iterationCles]} cles ? \n"))
    tempBase = int(input(f"Quelle est l'itération de la {nombreCles[iterationCles]} cles ? \n"))
    valeurBaseCles.append(tempCles)
    valeurDecalage.append(tempBase)
    iterationCles += 1
  print(valeurBaseCles)
  print(valeurDecalage)

def messageCoder():
  messageCodetemp = str(input("Quelle est le message que vous vouler encoder ?: "))
  return messageCodetemp

def messagerDecoder():
  messageCodetemp = str(input("Quelle est le message que vous vouler décrypter ?: "))
  return messageCodetemp

def question_de_depart():
  reponseValide = False
  quitter = False
  print("Bienvenue sur ENIGMA ! \n\n")
  while reponseValide == False and quitter == False:
    rep = str(input("Souhaiter vous encoder (e) ou decoder (d) ou quitter (q) ? "))
    if rep == 'q':
      quitter = True
    elif rep == 'e':
      Affichage()
      messageCode = messageCoder()
    elif rep == 'd':
      Affichage()
      messageCode = messageDecoder
    else:
      reponseValide = False
      print("Pas un choix valide ressayer \n\n")

question_de_depart()
      