
#FUNCTION#################################
#Def:
#Params:
#return:
#rtype:
#########################################

def decaleLettre(lettre, cle):
  intLettre = ord(lettre.upper()) - 65
  return (chr(((intLettre + cle) % 26) + 65))

def decaleC