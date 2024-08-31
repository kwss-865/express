import os

proprietarios = [{"nome":"Ricardo", "imóvel":"prédio", "ativo":True},
                 {"nome": "Roberta", "imóvel":"casa", "ativo": False},
                 {"nome": "Lisa", "imóvel":"sala-comercial", "ativo":True}] 

def mostra_titulo():
    print("""

    ██████████████████████████████████████████████████████████████████████████████████████████
    █▄─▄█▄─▀█▀─▄█─▄▄─█▄─▄─▀█▄─▄█▄─▄███▄─▄██▀▄─██▄─▄▄▀█▄─▄██▀▄─████▄─█─▄█▄─█▀▀▀█─▄█─▄▄▄▄█─▄▄▄▄█
    ██─███─█▄█─██─██─██─▄─▀██─███─██▀██─███─▀─███─▄─▄██─███─▀─█████─▄▀███─█─█─█─██▄▄▄▄─█▄▄▄▄─█
    ▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▀▄▄▀▀▀▄▄▀▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀
    """);

def mostra_escolhas():
    print("1. Cadastrar proprietário")
    print("2. Listar proprietários")
    print("3. Ativar proprietário")
    print("4. Sair\n")

def escolhe_opcao():

    def exibir_subtitulo(texto):
        os.system("cls")
        linha = "*" * len(texto)
        print(linha)
        print(texto)
        print(linha)
        print(" ")

    def retorna_menu():
        input("Digite uma tecla para voltar ao menu principal")
        main()

    def cadastra_proprietario():
        exibir_subtitulo("Cadastar proprietário")

        nome_proprietario = input("Digite o nome do proprietário que deseja cadastrar")
        imovel_proprietario = input(f"Digite o imóvel que {nome_proprietario} irá comprar/alugar") 
        dados_do_proprietario = {"nome":nome_proprietario, "imóvel":imovel_proprietario, "ativo":True}
        proprietarios.append(dados_do_proprietario) 
        print(f" o proprietario {nome_proprietario} foi cadastrado com sucesso\n") 

        retorna_menu()
    
    def listar_proprietarios():
        exibir_subtitulo("Listar proprietários cadastrados")
        
        print(f"{"Nome do proprietário".ljust(22)} | {"imóvel".ljust(20)} | Status ")
        for proprietario in proprietarios:
            nome_proprietario = proprietario["nome"]
            imovel_propritario  = proprietario["imóvel"] 
            ativo = "Ativado" if proprietario["ativo"] else "Desativado"
            print(f" - {nome_proprietario.ljust(20)} | {imovel_propritario.ljust(20)} | {ativo}")
            

        retorna_menu()
    
    def ativar_proprietario():
        exibir_subtitulo("Ativar proprietário")
        nome_proprietario = input("Digite o nome do proprietário que deseja ativar:")
        proprietario_encontrado = False 

        for proprietario in proprietarios:
            if nome_proprietario == proprietario["nome"]:
                proprietario_encontrado = True
                proprietario["ativo"] = not proprietario["ativo"]
                mensagem = f"O imóvel de {nome_proprietario} foi ativado com sucesso" if proprietario["ativo"] else f" O imóvel {nome_proprietario} foi desativado com sucesso"
                print(mensagem)

        if not proprietario_encontrado:
            print("Não encontrado") 
        retorna_menu()

    def finalizar_programa():
        exibir_subtitulo("Flinalizando o progrma\n")
    
    def opcao_invalida():
        print("Esse carácter não é permitido ")
        
        retorna_menu()

    try:
        opcao_escolhida = int(input("Escolha um opção:"))
        
        if opcao_escolhida == 1:
            cadastra_proprietario()
        elif opcao_escolhida ==2:
            listar_proprietarios()
        elif opcao_escolhida ==3:
            ativar_proprietario()
        elif opcao_escolhida ==4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
        os.system("cls")
        mostra_titulo()
        mostra_escolhas()
        escolhe_opcao()

if __name__=='__main__':
        main()