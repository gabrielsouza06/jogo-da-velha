# celula.py
# Esse arquivo define a classe Celula, que representa uma casa do tabuleiro do jogo da velha.
# Cada célula pode estar vazia ou conter um símbolo ('X' ou 'O').
# Essa classe ajuda a verificar se a jogada é válida e guardar o símbolo jogado.
class Celula:
    def __init__(self):
        self.simbolo = ' '

    def __str__(self):
        return self.simbolo

    def esta_vazia(self):
        return self.simbolo == ' '
