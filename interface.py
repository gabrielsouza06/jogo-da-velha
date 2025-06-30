import tkinter as tk
from tkinter import messagebox
from jogo import JogoDaVelha

class JogoDaVelhaGUI:
    def __init__(self, nome_x, nome_o):
        self.jogo = JogoDaVelha()
        self.jogo.jogadores['X'] = nome_x
        self.jogo.jogadores['O'] = nome_o

        self.root = tk.Tk()
        self.root.title("Jogo da Velha")

        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        self.label_info = tk.Label(self.root, text=f"Vez de {self.jogo.jogador_atual}", font=("Arial", 16))
        self.label_info.grid(row=0, column=0, columnspan=3, pady=(10, 5))

        self.criar_tabuleiro()

    def criar_tabuleiro(self):
        for i in range(3):
            for j in range(3):
                botao = tk.Button(
                    self.root,
                    text=" ",
                    width=6,
                    height=3,
                    font=("Arial", 24),
                    command=lambda linha=i, coluna=j: self.jogar(linha, coluna)
                )
                botao.grid(row=i+1, column=j, padx=5, pady=5)
                self.botoes[i][j] = botao

    def jogar(self, linha, coluna):
        celula = self.jogo.tabuleiro[linha][coluna]
        if celula.esta_vazia():
            celula.simbolo = self.jogo.jogador_atual
            self.botoes[linha][coluna].config(text=self.jogo.jogador_atual)

            if self.jogo.verificar_vitoria():
                self.fim_de_jogo(f"{self.jogo.jogadores[self.jogo.jogador_atual]} venceu!")
            elif self.jogo.tabuleiro_cheio():
                self.fim_de_jogo("Empate!")
            else:
                self.jogo.jogador_atual = 'O' if self.jogo.jogador_atual == 'X' else 'X'
                self.label_info.config(text=f"Vez de {self.jogo.jogador_atual}")
        else:
            messagebox.showinfo("Jogada inválida", "Essa célula já está ocupada.")

    def fim_de_jogo(self, mensagem):
        messagebox.showinfo("Fim de jogo", mensagem)
        self.jogo.resultado = mensagem
        self.jogo.salvar()
        self.root.quit()

    def iniciar(self):
        self.root.mainloop()
