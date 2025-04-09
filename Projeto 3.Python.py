
#Projeto 03 – Jogo da Velha
#Criar um jogo da velha interativo onde dois jogadores podem alternar turnos até
#um deles vencer ou dar empate.
#Habilidades trabalhadas:
#• Uso de matrizes NumPy para organizar o tabuleiro
#• Manipulação de loops e verificações de vitória
#• Entrada de dados e interação com o usuário

import numpy as np

def criar_tabuleiro():
    return np.full((3, 3), ' ')

def mostrar_tabuleiro(tabuleiro):
    print("\n")
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if np.all(tabuleiro[i, :] == jogador) or np.all(tabuleiro[:, i] == jogador):
            return True
    # Verifica diagonais
    if np.all(np.diag(tabuleiro) == jogador) or np.all(np.diag(np.fliplr(tabuleiro)) == jogador):
        return True
    return False

def verificar_empate(tabuleiro):
    return np.all(tabuleiro != ' ')

def jogar():
    tabuleiro = criar_tabuleiro()
    jogador_atual = 'X'

    while True:
        mostrar_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")
        
        try:
            linha = int(input("Escolha a linha (0, 1 ou 2): "))
            coluna = int(input("Escolha a coluna (0, 1 ou 2): "))
            
            if tabuleiro[linha, coluna] != ' ':
                print("Essa posição já está ocupada. Escolha outra.")
                continue

            tabuleiro[linha, coluna] = jogador_atual

            if verificar_vitoria(tabuleiro, jogador_atual):
                mostrar_tabuleiro(tabuleiro)
                print(f"Parabéns! Jogador {jogador_atual} venceu!")
                break

            if verificar_empate(tabuleiro):
                mostrar_tabuleiro(tabuleiro)
                print("Empate!")
                break

            # Trocar de jogador
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        
        except (ValueError, IndexError):
            print("Entrada inválida. Tente novamente usando números 0, 1 ou 2.")

# Executa o jogo
jogar()
