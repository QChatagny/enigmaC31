#enigma1

import reflecteur as r
import decalage as d

#ENCODE

#FUNCTION#################################
#Def:
#Params:
#return:
#rtype:
#########################################
def moteur(contenu, cles, decs, ref, isEncoding):
  if (isEncoding):
    encode(cles, decs, ref)
  else:
    decode(cles, decs, ref)

#FUNCTION#################################
#Def:
#Params:
#return:
#rtype:
#########################################
def encode(cles, contenu, Ref):
  contenuEncode = []
  contenuEncodeTemp = []

  for i in range(0,len(cles) - 1):
    if i == 0:
      for lettre in contenu:
        contenuEncode.append(d.decaleLettre(lettre, cles[i]))
    else: 
      for lettre in contenuEncode:
        contenuEncodeTemp.append(d.decaleLettre(lettre, cles[i]))

      contenuEncode = contenuEncodeTemp
      contenuEncodeTemp = []
  
  return contenuEncode

def encodeTEST():
  cles = [1,1,1,1]
  contenu = "AAAAAAAA"

  testResult = encode(cles, contenu, 1)
  print(testResult)

encodeTEST()


#FUNCTION#################################
#Def:
#Params:
#return:
#rtype:
#########################################
def decode(Cles, Decs, ref):
  pass






