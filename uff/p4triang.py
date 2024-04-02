# Escola de Engenharia - Eng. Civil
# TCC00239 - Programação de Computadores
# Turma I1 2024/1; Professor - John Reed
# Programador: Maurício Yan Barroso de Souza Mat: 124037033
# p4triang.py: Classifica os triângulos
import time

# Função para classificar o triângulo
def classificação (a, b, c):
    if (a + b < c) or (a + c < b) or (b + c < a):
        print("Os valores dados não formam um triângulo:")
    elif a == b == c:
        print(f"Este triângulo é equilátero.")
    elif a != b != c:
        print(f"Este triângulo é escaleno.")
    else:
        print(f"Este triângulo é isósceles.")

while True:
    # Boas vindas
    print("Bem-vindo, Sr. Usuário!")
    print("Programa classificação triângulo")
    print('')

    # Diálogo de entradas de dados
    a = float(input("Informe o primeiro lado do triângulo: "))
    b = float(input("Informe o segundo lado do triângulo: "))
    c = float(input("Informe o terceiro lado do triângulo: "))
    print('')
    
    # Emissão do relatório de saída
    classificação(a, b, c)
    repetir = input("Gostaria de testar outro triângulo? (s/n): ")
    if repetir.lower() != 's':
        break
# Despedida
print('Execução concluída. Tenha um bom dia!')
time.sleep(3)

