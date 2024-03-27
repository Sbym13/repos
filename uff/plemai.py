# Escola de Engenharia - Eng. Civil
# TCC00239 - Programação de Computadores
# Turma I1 2024/1; Professor - John Reed
# Programador: Maurício Yan Barroso de Souza Mat: 124037033
# plemai.py: Pega dois valores inteiros fornecidos pelo usuário e retorna o maior
import time

def maior (n1, n2):
   if n1 > n2:
    print(f"{n1} é maior do que {n2}")
   elif n1 < n2:
    print(f"{n2} é maior do que {n1}")
   else:
    print(f"{n1} é igual à {n2}")


while True:
  n1 = int(input("Digite o primeiro valor: "))
  n2 = int(input("Digite o segundo valor: "))
  maior(n1, n2)
  repetir = input("Gostaria de testar outros dois valores?(s/n) ")
  if repetir.lower() != "s":
    break

print('Execução concluída. Tenha um bom dia!')
time.sleep(2)