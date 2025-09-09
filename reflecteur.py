
#FUNCTION#################################
#Def:
#Params:
#return:
#rtype:
#########################################
def getReflecteurDecalage(reflecteur):
  return 26 - reflecteur.index('A')


#########################################
#TESTS
#########################################
def getReflecteurDecalageTEST():
  ref = "DEFGHIJKLMNOPQRSTUVWXYZABC"
  testedDecalage = getReflecteurDecalage(ref)
  message = "PASSED" if testedDecalage == 3 else "FAILED"
  print(message)


#FUNCTION#################################
#Def:
#Params:
#return:
#rtype:
#########################################
def applyDecalage(lettre, decalage):
  intLettre = ord(lettre.upper()) - 65
  return (chr(((intLettre + decalage) % 26) + 65))

def reflexion(reflecteur, contenu):
  contenuReflechit = []
  decalage = getReflecteurDecalage(reflecteur)

  for lettre in contenu:
    contenuReflechit.append(applyDecalage(lettre, decalage))
    
  return contenuReflechit