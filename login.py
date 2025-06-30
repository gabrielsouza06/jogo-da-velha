import tkinter as tk
from tkinter import messagebox
from interface import JogoDaVelhaGUI  # Importa a GUI do jogo

class TelaLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login - Jogo da Velha")

        self.modo_jogo = tk.StringVar(value="2jogadores")
        self.dificuldade = tk.StringVar(value="facil")

        frame_nomes = tk.Frame(self.root)
        frame_nomes.pack(padx=20, pady=10)

        tk.Label(frame_nomes, text="Nome do Jogador X:").grid(row=0, column=0, sticky="e")
        self.nome_x_entry = tk.Entry(frame_nomes)
        self.nome_x_entry.grid(row=0, column=1)

        tk.Label(frame_nomes, text="Nome do Jogador O:").grid(row=1, column=0, sticky="e")
        self.nome_o_entry = tk.Entry(frame_nomes)
        self.nome_o_entry.grid(row=1, column=1)

        frame_modo = tk.Frame(self.root)
        frame_modo.pack(padx=20, pady=10, fill="x")

        tk.Label(frame_modo, text="Modo de Jogo:").pack(anchor="w")

        rb_2jogadores = tk.Radiobutton(frame_modo, text="2 Jogadores", variable=self.modo_jogo, value="2jogadores", command=self.atualizar_opcoes)
        rb_2jogadores.pack(anchor="w")

        rb_maquina = tk.Radiobutton(frame_modo, text="Contra Máquina", variable=self.modo_jogo, value="maquina", command=self.atualizar_opcoes)
        rb_maquina.pack(anchor="w")

        self.frame_dificuldade = tk.Frame(self.root)
        self.frame_dificuldade.pack(padx=20, pady=10, fill="x")

        tk.Label(self.frame_dificuldade, text="Dificuldade:").pack(anchor="w")
        tk.Radiobutton(self.frame_dificuldade, text="Fácil", variable=self.dificuldade, value="facil").pack(anchor="w")
        tk.Radiobutton(self.frame_dificuldade, text="Médio", variable=self.dificuldade, value="medio").pack(anchor="w")
        tk.Radiobutton(self.frame_dificuldade, text="Difícil", variable=self.dificuldade, value="dificil").pack(anchor="w")

        btn_comecar = tk.Button(self.root, text="Começar Jogo", command=self.comecar_jogo)
        btn_comecar.pack(pady=10)

        self.atualizar_opcoes()

    def atualizar_opcoes(self):
        if self.modo_jogo.get() == "maquina":
            self.frame_dificuldade.pack(padx=20, pady=10, fill="x")
            self.nome_o_entry.config(state="disabled")
            self.nome_o_entry.delete(0, tk.END)
            self.nome_o_entry.insert(0, "Máquina")
        else:
            self.frame_dificuldade.pack_forget()
            self.nome_o_entry.config(state="normal")
            self.nome_o_entry.delete(0, tk.END)

    def comecar_jogo(self):
        nome_x = self.nome_x_entry.get().strip()
        nome_o = self.nome_o_entry.get().strip()

        if not nome_x:
            messagebox.showwarning("Aviso", "Por favor, insira o nome do jogador X.")
            return

        if self.modo_jogo.get() == "2jogadores" and not nome_o:
            messagebox.showwarning("Aviso", "Por favor, insira o nome do jogador O.")
            return

        modo = self.modo_jogo.get()
        dificuldade = self.dificuldade.get()

        if modo == "2jogadores":
            # Fecha a janela de login
            self.root.destroy()

            # Abre a janela do jogo com os nomes informados
            jogo_gui = JogoDaVelhaGUI(nome_x, nome_o)
            jogo_gui.iniciar()
        else:
            messagebox.showinfo("Aviso", "Opção contra máquina ainda não implementada.")

    def iniciar(self):
        self.root.mainloop()


if __name__ == "__main__":
    tela = TelaLogin()
    tela.iniciar()
