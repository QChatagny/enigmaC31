
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
def applyReflecteur(lettre, decalage):
  intLettre = ord(lettre.upper()) - 65
  return (chr(((intLettre + decalage) % 26) + 65))

