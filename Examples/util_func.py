import re

def bp(lista, patron):
   elementos = []
   for e in lista:
       p = re.search(patron, e)
       if p is not None:
           elementos.append(e)
   print elementos 
