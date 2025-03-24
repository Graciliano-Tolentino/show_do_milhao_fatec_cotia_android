def menu():
    print("\n" + "=" * 50)
    print("SHOW DO MILHÃO – VERSÃO MULTI-INTERFACE".center(50))
    print("=" * 50)
    print("1. Jogar no terminal")
    print("2. Jogar com interface gráfica (Tkinter)")
    print("3. Sair")
    print("=" * 50)
    escolha = input("Escolha uma opção: ").strip()
    return escolha

def rodar_terminal():
    from scripts.etapa1_intro import exibir_menu
    from scripts.etapa3_jogo import jogar
    from scripts.encerrar_jogo import encerrar_jogo

    exibir_menu()
    pontuacao = jogar()
    encerrar_jogo(pontuacao)

def rodar_tkinter():
    from scripts.interface_tkinter import ShowDoMilhaoApp
    import tkinter as tk

    root = tk.Tk()
    app = ShowDoMilhaoApp(root)
    root.mainloop()

if __name__ == "__main__":
    while True:
        opcao = menu()
        if opcao == "1":
            rodar_terminal()
        elif opcao == "2":
            rodar_tkinter()
            break
        elif opcao == "3":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")
