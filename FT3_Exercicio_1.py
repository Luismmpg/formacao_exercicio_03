personagens = []


def adicionar_personagem():
    personagem = {}
    personagem["nome"] = input("Nome: ")
    personagem["idade"] = input("Idade: ")
    personagem["profissao"] = input("Profissão: ")
    personagem["hobbies"] = input("Hobbies (utilize virgulas para separar): ").split(
        ","
    )
    personagem["descricao"] = input("Descrição: ")

    personagens.append(personagem)
    print("Perfil adicionado com sucesso!")
    print("\n")


def modificar_personagem():
    nome = input("Digite o nome do personagem que deseja modificar: ")
    for personagem in personagens:
        if personagem["nome"].lower() == nome.lower():
            print("Personagem encontrado. Insira as novas informações:")
            personagem["nome"] = input("Nome: ")
            personagem["idade"] = input("Idade: ")
            personagem["profissao"] = input("Profissão: ")
            personagem["hobbies"] = input("Hobbies (separados por vírgula): ").split(
                ","
            )
            personagem["descricao"] = input("Descrição: ")
            print("Personagem modificado com sucesso!")
            print("\n")
            return
    print("Personagem não encontrado.")
    print("\n")


def remover_personagem():
    nome = input("Digite o nome do personagem que deseja remover: ")
    for personagem in personagens:
        if personagem["nome"].lower() == nome.lower():
            personagens.remove(personagem)
            print("Personagem removido com sucesso!")
            print("\n")
            return
    print("Personagem não encontrado.")
    print("\n")


def visualizar_personagens():
    if len(personagens) == 0:
        print(
            "Não existem personagens criados. Para criar um personagem, selecionar a opção 1."
        )
        print("\n")
    else:
        print("Lista de Personagens:")
        for personagem in personagens:
            print("Nome:", personagem["nome"])
            print("Idade:", personagem["idade"])
            print("Profissão:", personagem["profissao"])
            print("Hobbies:", ", ".join(personagem["hobbies"]))
            print("Descrição:", personagem["descricao"])
            print("\n")


def pesquisar_personagem():
    nome = input("Digite o nome do personagem que deseja pesquisar: ")
    for personagem in personagens:
        if personagem["nome"].lower() == nome.lower():
            print("Personagem encontrado:")
            print("Nome:", personagem["nome"])
            print("Idade:", personagem["idade"])
            print("Profissão:", personagem["profissao"])
            print("Hobbies:", ", ".join(personagem["hobbies"]))
            print("Descrição:", personagem["descricao"])
            print("\n")
            return
    print("Personagem não encontrado.")
    print("\n")


while True:
    print(
        "Bem-vindo ao Criador de Perfil de Personagem. Selecione o número da opção do menu abaixo que deseja selecionar e siga as instruções dadas de seguida."
    )
    print("\n")
    print("----- Menu -----")
    print("1. Adicionar personagem")
    print("2. Modificar personagem")
    print("3. Remover personagem")
    print("4. Visualizar personagens")
    print("5. Pesquisar personagem")
    print("6. Sair")
    opcao = input("Selecione uma opção: ")
    print("\n")

    if opcao == "1":
        adicionar_personagem()
    elif opcao == "2":
        modificar_personagem()
    elif opcao == "3":
        remover_personagem()
    elif opcao == "4":
        visualizar_personagens()
    elif opcao == "5":
        pesquisar_personagem()
    elif opcao == "6":
        break
    else:
        print("Opção inválida. Tente novamente.")
        print("\n")
