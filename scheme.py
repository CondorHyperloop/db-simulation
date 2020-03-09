from random import randint
import json

data = json.load(open("scheme.json"))

def procedure(latest, variant):
   for x in latest:

      generated = None

      if data[x] == "int":
         generated = randint(2, 3)
         print("%s: %s" % (x,))


def setup( str ):
   print (str)
   return