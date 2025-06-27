# jogo.py
# Aqui estão as classes principais do jogo:
# - Tabuleiro: representa o tabuleiro 3x3 usando células.
#   Permite exibir o tabuleiro, registrar jogadas e verificar quem venceu.
# - (Opcionalmente) também pode conter a lógica principal do jogo.
from celula import Celula
from salvar_resultados import salvar_partida

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[Celula() for _ in range(3)] for _ in range(3)]
        self.jogador_atual = 'X'
        self.jogadores = {'X': '', 'O': ''}
        self.resultado = None

    def imprimir_tabuleiro(self):
        print("\n  0   1   2")
        for i, linha in enumerate(self.tabuleiro):
            linha_str = f"{i} " + " | ".join(str(celula) for celula in linha)
            print(linha_str)
            if i < 2:
                print("  ---------")
        print()

    def jogar(self, linha, coluna):
        if 0 <= linha < 3 and 0 <= coluna < 3:
            celula = self.tabuleiro[linha][coluna]
            if celula.esta_vazia():
                celula.simbolo = self.jogador_atual
                if self.verificar_vitoria():
                    self.resultado = f"{self.jogador_atual} venceu"
                    return True
                elif self.tabuleiro_cheio():
                    self.resultado = "Empate"
                    return True
                self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
                return False
            else:
                print("Essa célula já está ocupada.")
        else:
            print("Posição inválida.")
        return False

    def tabuleiro_cheio(self):
        return all(not celula.esta_vazia() for linha in self.tabuleiro for celula in linha)

    def verificar_vitoria(self):
        t = self.tabuleiro
        linhas = [t[i] for i in range(3)]
        colunas = [[t[i][j] for i in range(3)] for j in range(3)]
        diagonais = [[t[i][i] for i in range(3)], [t[i][2 - i] for i in range(3)]]
        for grupo in linhas + colunas + diagonais:
            if all(celula.simbolo == self.jogador_atual for celula in grupo):
                return True
        return False

    def salvar(self):
        salvar_partida(self.jogadores['X'], self.jogadores['O'], self.resultado)
