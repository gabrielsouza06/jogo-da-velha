# salvar_resultados.py
# Responsável por salvar os dados das partidas (jogadores e resultado) em um arquivo de texto.
# Isso permite manter um histórico das partidas jogadas.

def salvar_partida(jogador_x, jogador_o, resultado):
    with open("historico_partidas.txt", "a") as f:
        f.write(f"Jogador X: {jogador_x}\n")
        f.write(f"Jogador O: {jogador_o}\n")
        f.write(f"Resultado: {resultado}\n")
        f.write("-" * 30 + "\n")
