# Escola de Engenharia - Eng. Civil
# TCC00239 - Programação de Computadores
# Turma I1 2024/1; Professor - John Reed
# Programador: Maurício Yan Barroso de Souza Mat: 124037033
# pleimp.py: Cria uma ficha para o usuário com os dados fornecidos
import time

# Função para centralizar o msg
def centralizar(msg, lt):
    espacos_total = lt - len(msg)
    espacos_antes = espacos_total // 2
    espacos_depois = espacos_total - espacos_antes
    return ' ' * espacos_antes + msg + ' ' * espacos_depois

while True:
    # Boas vindas
    print("Bem-vindo, Sr. Usuário!")
    print("Programa ficha cadastral")
    print('')

    # Diálogo de entradas de dados
    nome = input("Escreva seu nome: ")
    idade = int(input("Insira sua idade (em anos): "))
    genero = input("Informe seu gênero (M/F/O): ")
    print('')

    # Processamento
    tam = len(nome)+38

    # Emissão do relatório de saída
    print('*'*(tam+2))
    print(f'*{centralizar("Ficha", tam)}*')
    print(f'*{centralizar("", tam)}*')
    print(f'*{centralizar("Nome: " + nome, tam)}*')
    print(f'*{centralizar("Idade: " + str(idade), tam)}*')
    print(f'*{centralizar("Gênero: " + genero, tam)}*')
    print('*'*(tam+2))
    print('')

    # Pergunta se deseja fazer outra ficha
    repetir = input("Gostaria de fazer outra ficha? (s/n): ")
    if repetir.lower() != 's':
        break

# Despedida
print('Execução concluída. Tenha um bom dia!')
time.sleep(2)

