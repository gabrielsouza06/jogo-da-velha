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
        self.jogadores = {'X': 'Jogador X', 'O': 'Jogador O'}
        self.jogador_atual = 'X'
        self.resultado = None
        self.sequencia_vencedora = []

    def verificar_vitoria(self):
        tab = self.tabuleiro

        # Linhas
        for i in range(3):
            if tab[i][0].simbolo != ' ' and tab[i][0].simbolo == tab[i][1].simbolo == tab[i][2].simbolo:
                self.sequencia_vencedora = [(i, 0), (i, 1), (i, 2)]
                return True

        # Colunas
        for j in range(3):
            if tab[0][j].simbolo != ' ' and tab[0][j].simbolo == tab[1][j].simbolo == tab[2][j].simbolo:
                self.sequencia_vencedora = [(0, j), (1, j), (2, j)]
                return True

        # Diagonal principal
        if tab[0][0].simbolo != ' ' and tab[0][0].simbolo == tab[1][1].simbolo == tab[2][2].simbolo:
            self.sequencia_vencedora = [(0, 0), (1, 1), (2, 2)]
            return True

        # Diagonal secundária
        if tab[0][2].simbolo != ' ' and tab[0][2].simbolo == tab[1][1].simbolo == tab[2][0].simbolo:
            self.sequencia_vencedora = [(0, 2), (1, 1), (2, 0)]
            return True

        self.sequencia_vencedora = []
        return False

    def tabuleiro_cheio(self):
        for linha in self.tabuleiro:
            for celula in linha:
                if celula.esta_vazia():
                    return False
        return True
    
    def salvar(self):
        salvar_partida(self.jogadores['X'], self.jogadores['O'], self.resultado)
