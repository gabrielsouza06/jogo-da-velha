from celula import Celula
from salvar_resultados import salvar_partida
import random

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[Celula() for _ in range(3)] for _ in range(3)]
        self.jogadores = {'X': 'Jogador X', 'O': 'Jogador O'}
        self.jogador_atual = 'X'
        self.resultado = None
        self.sequencia_vencedora = []
        self.dificuldade = "facil"  # Padrão: fácil

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

    def jogada_computador(self):
        """Realiza a jogada do computador baseada na dificuldade selecionada"""
        if self.dificuldade == "facil":
            return self.jogada_facil()
        elif self.dificuldade == "medio":
            return self.jogada_media()
        else:  # dificil
            return self.jogada_dificil()

    def jogada_facil(self):
        """Jogada aleatória (nível fácil)"""
        celulas_vazias = []
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j].esta_vazia():
                    celulas_vazias.append((i, j))
        
        if celulas_vazias:
            return random.choice(celulas_vazias)
        return None

    def jogada_media(self):
        """Jogada semi-inteligente (nível médio)"""
        # 1. Primeiro verifica se pode vencer na próxima jogada
        jogada = self.verificar_jogada_vencedora(self.jogador_atual)
        if jogada:
            return jogada
        
        # 2. Verifica se o oponente pode vencer na próxima jogada e bloqueia
        oponente = 'O' if self.jogador_atual == 'X' else 'X'
        jogada = self.verificar_jogada_vencedora(oponente)
        if jogada:
            return jogada
        
        # 3. Se não, faz uma jogada aleatória
        return self.jogada_facil()

    def jogada_dificil(self):
        """Jogada perfeita usando algoritmo minimax (nível difícil)"""
        melhor_jogada = self.minimax(self.jogador_atual)
        return melhor_jogada[0], melhor_jogada[1]

    def verificar_jogada_vencedora(self, jogador):
        """Verifica se há uma jogada que leve à vitória imediata"""
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j].esta_vazia():
                    self.tabuleiro[i][j].simbolo = jogador
                    vitoria = self.verificar_vitoria()
                    self.tabuleiro[i][j].simbolo = ' '  # Desfaz a jogada
                    if vitoria:
                        return (i, j)
        return None

    def minimax(self, jogador, profundidade=0):
        """Algoritmo minimax para encontrar a melhor jogada"""
        melhor_jogada = [-1, -1, -float('inf') if jogador == self.jogador_atual else float('inf')]
        
        # Verifica estados terminais
        if self.verificar_vitoria():
            if jogador == self.jogador_atual:
                return [-1, -1, -1]
            else:
                return [-1, -1, 1]
        elif self.tabuleiro_cheio():
            return [-1, -1, 0]

        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j].esta_vazia():
                    self.tabuleiro[i][j].simbolo = jogador
                    pontuacao = self.minimax('O' if jogador == 'X' else 'X', profundidade+1)
                    self.tabuleiro[i][j].simbolo = ' '  # Desfaz a jogada
                    pontuacao[0], pontuacao[1] = i, j
                    
                    if jogador == self.jogador_atual:
                        if pontuacao[2] > melhor_jogada[2]:
                            melhor_jogada = pontuacao
                    else:
                        if pontuacao[2] < melhor_jogada[2]:
                            melhor_jogada = pontuacao
        
        return melhor_jogada

    def realizar_jogada_computador(self):
        """Realiza a jogada do computador e retorna True se bem sucedido"""
        if self.jogador_atual == 'O' or self.jogadores['O'] == 'Computador':
            jogada = self.jogada_computador()
            if jogada:
                linha, coluna = jogada
                self.tabuleiro[linha][coluna].simbolo = self.jogador_atual
                return True
        return False