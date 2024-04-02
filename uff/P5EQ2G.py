# Escola de Engenharia - Eng. Civil
# TCC00239 - Programação de Computadores
# Turma I1 2024/1; Professor - John Reed
# Programador: Maurício Yan Barroso de Souza Mat: 124037033
# P5EQ2G.py: Classifica as raízes dados coeficientes a, b e c de X

# BOAS-VINDAS
print('Bem-vindo, Sr. Usuário')
print('Programa P5EQ2G, classifica as raízes dados coeficientes a, b e c de X')
print('')

while True:
  # DIÁLOGO DE ENTRADA DE DADOS
  a = float(input('Insira o coeficiente a: '))
  print('')
  print(f'Coeficiente a: {a}')
  print('')
  b = float(input('Insira o coeficiente b: '))
  print('')
  print(f'Coeficiente b: {b}')
  print('')
  c = float(input('Insira o coeficiente c: '))
  print('')
  print(f'Coeficiente c: {c}')
  print('')
  # PROCESSAMENTO
  D = b**2 - 4 * a * c
  # EMISÃO DO RELATÓRIO DE SAÍDA
  if D < 0: # RC E RPI
    if b == 0: # RPI
      print('Esta equação é puramente imaginária.')
    else:
      print('Esta equação admite raízes complexas.')
  else: # RRI E RRD
    if D > 0: # RRD
      print('Esta equação admite 2 raízes reais diferentes.')
    else: # RRI
      print('Esta equação admite 2 raízes reais iguais.')
  # DESPEDIDA
  print('')
  rep = input('Deseja testar outros valores (s/n)? ')
  if rep.lower() != 's':
    break
print('')
print('Execução concluída. Tenha um bom dia!')