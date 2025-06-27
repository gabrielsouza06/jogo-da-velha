# main.py
# Arquivo principal do projeto. É onde o jogo começa e roda no terminal.
# Ele controla a interação com os jogadores, alterna os turnos e usa o Tabuleiro para jogar.
# main.py
from jogo import JogoDaVelha

def main():
    jogo = JogoDaVelha()
    print("=== JOGO DA VELHA ===")
    jogo.jogadores['X'] = input("Nome do jogador X: ")
    jogo.jogadores['O'] = input("Nome do jogador O: ")

    terminou = False
    while not terminou:
        jogo.imprimir_tabuleiro()
        print(f"Vez de {jogo.jogador_atual}")
        try:
            linha = int(input("Linha (0-2): "))
            coluna = int(input("Coluna (0-2): "))
            terminou = jogo.jogar(linha, coluna)
        except ValueError:
            print("Entrada inválida. Use apenas números inteiros.")

    jogo.imprimir_tabuleiro()
    print(f"Fim de jogo! Resultado: {jogo.resultado}")
    jogo.salvar()

if __name__ == "__main__":
    main()
