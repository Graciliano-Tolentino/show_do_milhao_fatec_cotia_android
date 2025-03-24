import random
from .etapa2_perguntas import carregar_perguntas, sortear_pergunta

def eliminar_duas(pergunta_dict):
    """Remove duas opções erradas e exibe as restantes."""
    correta = pergunta_dict["resposta"]
    opcoes = pergunta_dict["opcoes"]
    erradas = [op for op in opcoes if op != correta]
    eliminadas = random.sample(erradas, 2)
    print("Duas alternativas incorretas foram eliminadas:")
    for op in opcoes:
        if op not in eliminadas:
            print(f"- {op}")

def apresentar_pergunta(pergunta_dict, numero):
    """Exibe a pergunta e opções no terminal."""
    print(f"\nPergunta {numero}: {pergunta_dict['pergunta']}")
    for i, opcao in enumerate(pergunta_dict["opcoes"], 1):
        print(f"{i}. {opcao}")
    print("\n[D]ica  |  [P]ular  |  [E]liminar duas  |  [S]air")
    return input("Sua resposta (ou comando): ").strip().lower()

def jogar():
    """Executa o jogo completo no terminal e retorna a pontuação final."""
    ajudas = {"dica": 1, "pular": 1, "eliminar": 1}
    perguntas = carregar_perguntas()
    usadas = []
    pontuacao = 0
    rodada = 1

    while rodada <= 10:
        resultado = sortear_pergunta(perguntas, usadas)
        if not resultado:
            print("Todas as perguntas foram utilizadas.")
            break

        indice, pergunta = resultado
        usadas.append(indice)

        while True:
            resposta = apresentar_pergunta(pergunta, rodada)

            if resposta == "d":
                if ajudas["dica"] > 0:
                    print(f"Dica: {pergunta['dica']}")
                    ajudas["dica"] -= 1
                else:
                    print("Você já usou sua dica.")
            elif resposta == "p":
                if ajudas["pular"] > 0:
                    print("Pergunta pulada.")
                    ajudas["pular"] -= 1
                    break
                else:
                    print("Você já usou o pulo.")
            elif resposta == "e":
                if ajudas["eliminar"] > 0:
                    eliminar_duas(pergunta)
                    ajudas["eliminar"] -= 1
                else:
                    print("Você já usou a eliminação.")
            elif resposta == "s":
                print("Você escolheu encerrar o jogo.")
                print(f"Sua pontuação final foi: {pontuacao}")
                return pontuacao
            elif resposta.isdigit():
                try:
                    indice_escolhido = int(resposta)
                    if 1 <= indice_escolhido <= len(pergunta["opcoes"]):
                        escolha = pergunta["opcoes"][indice_escolhido - 1]
                        if escolha == pergunta["resposta"]:
                            print("Resposta correta!")
                            pontuacao += 10
                        else:
                            print(f"Errado! A resposta correta era: {pergunta['resposta']}")
                        rodada += 1
                        break
                    else:
                        print("Opção fora do intervalo. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite o número da opção.")
            else:
                print("Entrada inválida. Tente novamente.")

    print(f"\nFim de jogo! Sua pontuação final foi: {pontuacao}")
    return pontuacao
