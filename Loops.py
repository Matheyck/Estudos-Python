idades = [20, 14, 40]

# for fora da função

def verifica_se_pode_dirigir(idade):
  if idade >= 18:
    print(f' {idade} anos de idade, TEM permissão para dirigir')
  else:
    print(f' {idade} anos de idade, NÃO tem permissão para dirigir')

for idade in idades:
  verifica_se_pode_dirigir(idade)
 

  

# for dentro da função

def verifica_se_pode_dirigir(idades):
  for idade in idades:
    if idade >= 18:
      print(f' {idade} anos de idade, TEM permissão para dirigir')
    else:
      print(f' {idade} anos de idade, NÃO tem permissão para dirigir')

verifica_se_pode_dirigir(idades)
