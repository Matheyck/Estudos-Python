idade = 18
idade >= 18
#True

permissoes = []
idades = [20, 14, 40]

def verifica_se_pode_dirigir(idades, permissoes):
  for idade in idades:
    if idade >= 18:
      permissoes.append(True)
    else:
      permissoes.append(False)

verifica_se_pode_dirigir(idades, permissoes)

permissoes
# [True, False, True]

for permissao in permissoes:
  if permissao == True:
    print('Tem permissão para dirigir')
  else:
    print('Não tem permissão para dirigir')  
    
 #Tem permissão para dirigir
 #Não tem permissão para dirigir
 #Tem permissão para dirigir
