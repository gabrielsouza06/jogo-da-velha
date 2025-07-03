import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font
from interface import JogoDaVelhaGUI  # Importa a GUI do jogo

class TelaLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jogo da Velha - Login")
        self.root.geometry("600x600")
        self.root.minsize(500, 550)
        
        # Configuração de estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Variáveis de controle
        self.modo_jogo = tk.StringVar(value="2jogadores")
        self.dificuldade = tk.StringVar(value="facil")
        self.tema_selecionado = tk.StringVar(value="Moderno")
        
        # Cores personalizadas
        self.cores = {
            'Moderno': {
                'fundo': '#f5f5f5',
                'fundo_card': '#ffffff',
                'texto': '#333333',
                'destaque': '#4a6fa5',
                'botao': '#4a6fa5',
                'botao_hover': '#3a5a8f',
                'borda': '#e0e0e0'
            },
            'Escuro': {
                'fundo': '#2d2d2d',
                'fundo_card': '#3d3d3d',
                'texto': '#e0e0e0',
                'destaque': '#6a8fc5',
                'botao': '#6a8fc5',
                'botao_hover': '#5a7fb5',
                'borda': '#4d4d4d'
            },
            'Colorido': {
                'fundo': '#e6f7ff',
                'fundo_card': '#ffffff',
                'texto': '#0066cc',
                'destaque': '#ff6b6b',
                'botao': '#ff6b6b',
                'botao_hover': '#ff5b5b',
                'borda': '#b3e0ff'
            }
        }
        
        # Primeiro criamos todos os widgets
        self.criar_interface()
        
        # Depois aplicamos o tema
        self.aplicar_tema("Moderno")
        
        # Configurações iniciais
        self.atualizar_opcoes()
        self.nome_x_entry.focus()
        self.root.bind('<Return>', lambda event: self.comecar_jogo())
        
        # Centralizar na tela
        self.root.eval('tk::PlaceWindow . center')

    def criar_interface(self):
        """Cria todos os elementos da interface"""
        # Frame principal
        self.main_frame = tk.Frame(self.root, bg=self.cores['Moderno']['fundo'])
        self.main_frame.pack(fill="both", expand=True, padx=40, pady=40)
        
        # Card central
        self.card = tk.Frame(self.main_frame, bg=self.cores['Moderno']['fundo_card'],
                          bd=0, highlightthickness=0, relief='flat')
        self.card.pack(expand=True, fill="both")
        self.card.grid_propagate(False)
        
        # Configurar grid
        self.card.columnconfigure(0, weight=1)
        self.card.rowconfigure(1, weight=1)
        
        # Cabeçalho
        self.cabecalho = tk.Frame(self.card, bg=self.cores['Moderno']['fundo_card'], 
                                height=80, bd=0, highlightthickness=0)
        self.cabecalho.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        
        titulo_font = Font(family='Helvetica', size=18, weight='bold')
        self.titulo = tk.Label(self.cabecalho, text="JOGO DA VELHA", 
                             font=titulo_font, bg=self.cores['Moderno']['fundo_card'],
                             fg=self.cores['Moderno']['destaque'])
        self.titulo.pack(side="top", pady=(10, 5))
        
        subtitulo_font = Font(family='Helvetica', size=10)
        self.subtitulo = tk.Label(self.cabecalho, text="Preencha os dados para começar", 
                                font=subtitulo_font, bg=self.cores['Moderno']['fundo_card'],
                                fg=self.cores['Moderno']['texto'])
        self.subtitulo.pack(side="top")
        
        # Corpo do card
        self.corpo = tk.Frame(self.card, bg=self.cores['Moderno']['fundo_card'], 
                            bd=0, highlightthickness=0)
        self.corpo.grid(row=1, column=0, sticky="nsew", padx=40, pady=(0, 20))
        
        # Frame dos jogadores
        frame_jogadores = tk.Frame(self.corpo, bg=self.cores['Moderno']['fundo_card'])
        frame_jogadores.pack(fill="x", pady=(10, 20))
        
        # Jogador X
        label_x = tk.Label(frame_jogadores, text="Jogador X (❌):", 
                         bg=self.cores['Moderno']['fundo_card'],
                         fg=self.cores['Moderno']['texto'], anchor="w")
        label_x.pack(fill="x", pady=(0, 5))
        
        self.nome_x_entry = ttk.Entry(frame_jogadores)
        self.nome_x_entry.pack(fill="x", pady=(0, 15), ipady=5)
        
        # Jogador O
        label_o = tk.Label(frame_jogadores, text="Jogador O (⭕):", 
                         bg=self.cores['Moderno']['fundo_card'],
                         fg=self.cores['Moderno']['texto'], anchor="w")
        label_o.pack(fill="x", pady=(0, 5))
        
        self.nome_o_entry = ttk.Entry(frame_jogadores)
        self.nome_o_entry.pack(fill="x", pady=(0, 20), ipady=5)
        
        # Frame do modo de jogo
        frame_modo = tk.LabelFrame(self.corpo, text=" Modo de Jogo ", 
                                 bg=self.cores['Moderno']['fundo_card'],
                                 fg=self.cores['Moderno']['destaque'],
                                 bd=1, relief="solid",
                                 highlightbackground=self.cores['Moderno']['borda'])
        frame_modo.pack(fill="x", pady=(0, 15))
        
        rb_2jogadores = ttk.Radiobutton(frame_modo, text="Dois Jogadores", 
                                      variable=self.modo_jogo, 
                                      value="2jogadores", 
                                      command=self.atualizar_opcoes)
        rb_2jogadores.pack(anchor="w", padx=5, pady=3)
        
        rb_maquina = ttk.Radiobutton(frame_modo, text="Contra o Computador", 
                                   variable=self.modo_jogo, 
                                   value="maquina", 
                                   command=self.atualizar_opcoes)
        rb_maquina.pack(anchor="w", padx=5, pady=3)
        
        # Frame de dificuldade
        self.frame_dificuldade = tk.LabelFrame(self.corpo, text=" Dificuldade ", 
                                            bg=self.cores['Moderno']['fundo_card'],
                                            fg=self.cores['Moderno']['destaque'],
                                            bd=1, relief="solid",
                                            highlightbackground=self.cores['Moderno']['borda'])
        
        rb_facil = ttk.Radiobutton(self.frame_dificuldade, text="Fácil", 
                                 variable=self.dificuldade, 
                                 value="facil")
        rb_facil.pack(anchor="w", padx=5, pady=3)
        
        rb_medio = ttk.Radiobutton(self.frame_dificuldade, text="Médio", 
                                 variable=self.dificuldade, 
                                 value="medio")
        rb_medio.pack(anchor="w", padx=5, pady=3)
        
        rb_dificil = ttk.Radiobutton(self.frame_dificuldade, text="Difícil", 
                                   variable=self.dificuldade, 
                                   value="dificil")
        rb_dificil.pack(anchor="w", padx=5, pady=3)
        
        # Frame de temas
        frame_temas = tk.LabelFrame(self.corpo, text=" Aparência ", 
                                  bg=self.cores['Moderno']['fundo_card'],
                                  fg=self.cores['Moderno']['destaque'],
                                  bd=1, relief="solid",
                                  highlightbackground=self.cores['Moderno']['borda'])
        frame_temas.pack(fill="x", pady=(15, 20))
        
        temas = ["Moderno", "Escuro", "Colorido"]
        for tema in temas:
            rb = ttk.Radiobutton(frame_temas, text=tema, 
                               variable=self.tema_selecionado, 
                               value=tema,
                               command=lambda t=tema: self.aplicar_tema(t))
            rb.pack(anchor="w", padx=5, pady=3)
        
        # Botão para começar o jogo
        self.btn_comecar = tk.Button(self.corpo, text="COMEÇAR JOGO", 
                                   command=self.comecar_jogo,
                                   bg=self.cores['Moderno']['botao'],
                                   fg='white',
                                   bd=0,
                                   highlightthickness=0,
                                   activebackground=self.cores['Moderno']['botao_hover'],
                                   activeforeground='white',
                                   padx=20, pady=10)
        self.btn_comecar.pack(fill="x", pady=(10, 0), ipady=5)
        
        # Efeito hover no botão
        self.btn_comecar.bind("<Enter>", lambda e: self.btn_comecar.config(
            bg=self.cores['Moderno']['botao_hover']))
        self.btn_comecar.bind("<Leave>", lambda e: self.btn_comecar.config(
            bg=self.cores['Moderno']['botao']))

    def aplicar_tema(self, tema):
        """Aplica o tema selecionado à interface"""
        cor = self.cores[tema]
        
        # Atualizar cores do root e frames principais
        self.root.configure(bg=cor['fundo'])
        if hasattr(self, 'main_frame'):
            self.main_frame.configure(bg=cor['fundo'])
            self.card.configure(bg=cor['fundo_card'])
            self.cabecalho.configure(bg=cor['fundo_card'])
            self.corpo.configure(bg=cor['fundo_card'])
            
            # Atualizar textos
            self.titulo.configure(bg=cor['fundo_card'], fg=cor['destaque'])
            self.subtitulo.configure(bg=cor['fundo_card'], fg=cor['texto'])
            
            # Atualizar botão
            self.btn_comecar.configure(bg=cor['botao'], 
                                      activebackground=cor['botao_hover'])
            
            # Atualizar estilo dos widgets ttk
            self.style.configure('TEntry', fieldbackground='white', foreground='black')
            self.style.configure('TRadiobutton', background=cor['fundo_card'], 
                               foreground=cor['texto'])
            self.style.map('TRadiobutton', 
                          background=[('active', cor['fundo_card'])])
            
            # Atualizar frames com borda
            for frame in [self.frame_dificuldade, self.corpo.winfo_children()[2]]:  # Modo e Aparência
                if isinstance(frame, tk.LabelFrame):
                    frame.configure(bg=cor['fundo_card'], fg=cor['destaque'],
                                  highlightbackground=cor['borda'])

    def atualizar_opcoes(self):
        """Atualiza as opções da interface com base no modo de jogo selecionado"""
        if self.modo_jogo.get() == "maquina":
            self.frame_dificuldade.pack(fill="x", pady=(0, 15))
            self.nome_o_entry.config(state="disabled")
            self.nome_o_entry.delete(0, tk.END)
            self.nome_o_entry.insert(0, "Computador")
        else:
            self.frame_dificuldade.pack_forget()
            self.nome_o_entry.config(state="normal")
            if self.nome_o_entry.get() == "Computador":
                self.nome_o_entry.delete(0, tk.END)

    def comecar_jogo(self):
        """Inicia o jogo com as configurações selecionadas"""
        nome_x = self.nome_x_entry.get().strip()
        nome_o = self.nome_o_entry.get().strip()

        if not nome_x:
            messagebox.showwarning("Aviso", "Por favor, insira o nome do Jogador X.")
            self.nome_x_entry.focus()
            return

        if self.modo_jogo.get() == "2jogadores" and not nome_o:
            messagebox.showwarning("Aviso", "Por favor, insira o nome do Jogador O.")
            self.nome_o_entry.focus()
            return

        modo = self.modo_jogo.get()
        dificuldade = self.dificuldade.get()

        # Fecha a janela de login
        self.root.destroy()

        # Abre a janela do jogo com as configurações selecionadas
        if modo == "maquina":
            jogo_gui = JogoDaVelhaGUI(nome_x, "Computador", dificuldade)
        else:
            jogo_gui = JogoDaVelhaGUI(nome_x, nome_o)
            
        jogo_gui.iniciar()

    def iniciar(self):
        """Inicia a interface gráfica"""
        self.root.mainloop()

if __name__ == "__main__":
    tela = TelaLogin()
    tela.iniciar()