def encerrar_jogo(pontuacao):
    """Exibe o resultado final com feedback motivacional e retorna a escolha do jogador."""
    print("\n" + "=" * 50)
    print("          FIM DE JOGO - RESULTADO FINAL          ".center(50))
    print("=" * 50)
    print(f"\nSua pontuação final foi: {pontuacao}\n")

    if pontuacao == 100:
        print("Parabéns! Você acertou todas as perguntas. Excelente desempenho!")
    elif pontuacao >= 70:
        print("Muito bom! Você demonstrou ótimo domínio dos conteúdos.")
    elif pontuacao >= 40:
        print("Bom esforço! Ainda dá para melhorar com mais prática.")
    else:
        print("Não desanime! Use esse resultado como ponto de partida para evoluir.")

    print("\nDeseja jogar novamente?")
    print("[S] Sim   |   [N] Não")

    return input("Escolha: ").strip().lower()
