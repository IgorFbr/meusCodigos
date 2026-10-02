
import random

def mostrar_tabuleiro(tabuleiro):
    print("\n")
    for i in range(3):
        print(" " + " | ".join(tabuleiro[i]))
        if i < 2:
            print("---+---+---")
    print()


def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)):
            return True
        if all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True

    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False


def tabuleiro_cheio(tabuleiro):
    return all(
        tabuleiro[i][j] != " "
        for i in range(3)
        for j in range(3)
    )


def jogada_jogador(tabuleiro, jogador):
    while True:
        try:
            linha = int(input("Escolha a linha (1-3): ")) - 1
            coluna = int(input("Escolha a coluna (1-3): ")) - 1

            if linha not in range(3) or coluna not in range(3):
                print("Escolha números entre 1 e 3.")
                continue

            if tabuleiro[linha][coluna] != " ":
                print("Essa posição já está ocupada!")
                continue

            tabuleiro[linha][coluna] = jogador
            break

        except ValueError:
            print("Digite apenas números inteiros.")


def jogada_computador(tabuleiro):
    posicoes = [
        (i, j)
        for i in range(3)
        for j in range(3)
        if tabuleiro[i][j] == " "
    ]

    if posicoes:
        linha, coluna = random.choice(posicoes)
        tabuleiro[linha][coluna] = "O"
        print("O computador fez sua jogada!")


def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    print("\n=== JOGO DA VELHA ===")
    print("Você é X e o computador é O.")

    while True:
        mostrar_tabuleiro(tabuleiro)
        jogada_jogador(tabuleiro, "X")

        if verificar_vitoria(tabuleiro, "X"):
            mostrar_tabuleiro(tabuleiro)
            print("Parabéns! Você venceu!")
            break

        if tabuleiro_cheio(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogada_computador(tabuleiro)

        if verificar_vitoria(tabuleiro, "O"):
            mostrar_tabuleiro(tabuleiro)
            print("O computador venceu!")
            break

        if tabuleiro_cheio(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("Empate!")
            break


while True:
    jogar()
    novamente = input("\nJogar novamente? (s/n): ").lower()

    if novamente != "s":
        print("Obrigado por jogar!")
        break