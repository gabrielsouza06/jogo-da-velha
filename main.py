# main.py
# Arquivo principal do projeto. É onde o jogo começa e roda no terminal.
# Ele controla a interação com os jogadores, alterna os turnos e usa o Tabuleiro para jogar.

from jogo import JogoDaVelha

def main():
    jogo = JogoDaVelha()
    print("=== JOGO DA VELHA ===")
    # Pede os nomes dos jogadores via terminal
    jogo.jogadores['X'] = input("Nome do jogador X: ")
    jogo.jogadores['O'] = input("Nome do jogador O: ")

    terminou = False
    # Loop principal que roda o jogo via terminal, pedindo entrada de linha e coluna
    while not terminou:
        jogo.imprimir_tabuleiro()  # Exibe tabuleiro no terminal
        print(f"Vez de {jogo.jogador_atual}")
        try:
            linha = int(input("Linha (0-2): "))
            coluna = int(input("Coluna (0-2): "))
            terminou = jogo.jogar(linha, coluna)  # Executa jogada e checa fim
        except ValueError:
            print("Entrada inválida. Use apenas números inteiros.")

    jogo.imprimir_tabuleiro()
    print(f"Fim de jogo! Resultado: {jogo.resultado}")
    jogo.salvar()

if __name__ == "__main__":
    main()

# -------------------------------------------
# Comentário explicando a inutilização deste main.py:

# Com a criação da interface gráfica usando Tkinter, este main.py se tornou
# praticamente inutilizável porque:

# 1. A interação com o usuário deixou de ser feita pelo terminal (input/print)
#    e passou a ser feita por botões, caixas de diálogo e eventos na janela gráfica.

# 2. O controle do fluxo do jogo mudou: ao invés de um loop while ativo que espera
#    entradas do terminal, agora o Tkinter usa um loop de eventos (mainloop) que
#    responde a cliques e ações do usuário.

# 3. Funções como 'input' e 'print' não são mais usadas, e o tabuleiro não é exibido
#    em texto no terminal, mas sim desenhado na interface gráfica.

# 4. Dessa forma, a lógica principal do jogo foi desacoplada da interface, e o main.py
#    do terminal não coordena mais o jogo, que agora é controlado pela classe da GUI.

# Portanto, o main.py é mantido apenas para fins de legado ou para executar a versão
# em terminal, mas no projeto com interface gráfica, ele não é mais usado.

