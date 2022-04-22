# Importando lib
from random import randrange, seed

seed(11)

randrange(0,11)

notas_matematica = []

for notas in range(8):
  notas_matematica.append(randrange(0,11))

notas_matematica
# [8, 7, 7, 8, 9, 3, 2, 8]
