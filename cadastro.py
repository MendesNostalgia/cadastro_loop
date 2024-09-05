# Solicita a quantidade de usuários a serem cadastrados
quantidade_usuarios = int(input("Quantos usuários serão cadastrados? "))

# Inicializa as estruturas homogêneas para armazenar os nomes e idades
nomes = [None] * quantidade_usuarios
idades = [None] * quantidade_usuarios

# Inicializa o contador de usuários cadastrados
indice_usuario = 0

# Função para exibir o menu
def exibir_menu():
    print("\nMenu de opções:")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar todos os usuários cadastrados")
    print("3 - Sair do sistema")

# Inicia o loop principal do sistema
while True:
    exibir_menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        # Verifica se ainda há espaço para cadastrar novos usuários
        if indice_usuario < quantidade_usuarios:
            # Solicita as informações do novo usuário
            nome = input("Digite o nome do usuário: ")
            idade = int(input("Digite a idade do usuário: "))

            # Armazena o novo usuário nas próximas posições disponíveis
            nomes[indice_usuario] = nome
            idades[indice_usuario] = idade

            # Incrementa o índice para o próximo usuário
            indice_usuario += 1

            print("Usuário cadastrado com sucesso!")
        else:
            print("Limite de usuários atingido!")

    elif opcao == 2:
        # Lista todos os usuários cadastrados
        if indice_usuario == 0:
            print("Nenhum usuário cadastrado.")
        else:
            for i in range(indice_usuario):
                print(f"Nome: {nomes[i]}, Idade: {idades[i]}")

    elif opcao == 3:
        # Encerra o sistema
        print("Saindo do sistema...")
        break

    else:
        # Trata a entrada de opção inválida
        print("Opção inválida! Por favor, escolha uma opção válida.")