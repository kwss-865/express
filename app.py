import os

def mostra_titulo():
    print("""

    ██████████████████████████████████████████████████████████████████████████████████████████
    █▄─▄█▄─▀█▀─▄█─▄▄─█▄─▄─▀█▄─▄█▄─▄███▄─▄██▀▄─██▄─▄▄▀█▄─▄██▀▄─████▄─█─▄█▄─█▀▀▀█─▄█─▄▄▄▄█─▄▄▄▄█
    ██─███─█▄█─██─██─██─▄─▀██─███─██▀██─███─▀─███─▄─▄██─███─▀─█████─▄▀███─█─█─█─██▄▄▄▄─█▄▄▄▄─█
    ▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▀▄▄▀▀▀▄▄▀▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀
    """);

def mostra_escolhas():
    print("1. Cadastrar proprietário")
    print("2. Listar Imóveis")
    print("3. Ativar Imóvel")
    print("4. Sair")

def escolhe_opcao():
    
    def finalizar_programa():
        os.system("cls")
        print("Flinalizando o progrma\n")
    
    def opcao_invalida():
        print("Esse carácter não é permitido ")
        input("Aperte qualquer tecla para voltar")
        main()

    try:
        opcao_escolhida = int(input("Escolha um opção:"))
        
        if opcao_escolhida == 1:
            print("Você escolher Cadastrar proprietário")
        elif opcao_escolhida ==2:
            print("Você escolher Listar Imóveis")
        elif opcao_escolhida ==3:
            print("Você escolher Ativar Imóvel")
        elif opcao_escolhida ==4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
        mostra_titulo()
        mostra_escolhas()
        escolhe_opcao()

if __name__=='__main__':
        main()