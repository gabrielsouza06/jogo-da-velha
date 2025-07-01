import tkinter as tk
from tkinter import ttk, messagebox
from interface import JogoDaVelhaGUI  # Importa a GUI do jogo

class TelaLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jogo da Velha - Configuração Inicial")
        self.root.geometry("500x500")
        self.root.minsize(450, 450)
        
        # Inicializa o estilo antes de usar
        self.style = ttk.Style()
        
        # Variáveis de controle
        self.modo_jogo = tk.StringVar(value="2jogadores")
        self.dificuldade = tk.StringVar(value="facil")
        self.tema_selecionado = tk.StringVar(value="Claro")
        
        # Configurar tema inicial
        self.aplicar_tema("Claro")
        
        # Frame principal
        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Conteúdo
        self.criar_widgets()
        
        # Configurações iniciais
        self.atualizar_opcoes()
        self.nome_x_entry.focus()
        self.root.bind('<Return>', lambda event: self.comecar_jogo())
        self.root.bind("<Configure>", self.on_window_resize)

    def criar_widgets(self):
        """Cria todos os widgets da interface"""
        # Frame de conteúdo
        content_frame = ttk.Frame(self.main_container)
        content_frame.pack(expand=True)
        
        # Título
        self.titulo = ttk.Label(content_frame, text="CONFIGURAÇÃO DO JOGO", 
                              font=('Arial', 14, 'bold'))
        self.titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Frame dos jogadores
        frame_jogadores = ttk.LabelFrame(content_frame, text="Jogadores", padding=10)
        frame_jogadores.grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)
        
        ttk.Label(frame_jogadores, text="Jogador X (🔴):").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.nome_x_entry = ttk.Entry(frame_jogadores, width=25)
        self.nome_x_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        ttk.Label(frame_jogadores, text="Jogador O (🔵):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.nome_o_entry = ttk.Entry(frame_jogadores, width=25)
        self.nome_o_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Frame do modo de jogo
        frame_modo = ttk.LabelFrame(content_frame, text="Modo de Jogo", padding=10)
        frame_modo.grid(row=2, column=0, sticky="nsew", pady=5, padx=5)
        
        ttk.Radiobutton(frame_modo, text="Dois Jogadores", variable=self.modo_jogo, 
                       value="2jogadores", command=self.atualizar_opcoes).pack(anchor="w", padx=5, pady=3)
        ttk.Radiobutton(frame_modo, text="Contra o Computador", variable=self.modo_jogo, 
                       value="maquina", command=self.atualizar_opcoes).pack(anchor="w", padx=5, pady=3)
        
        # Frame de dificuldade
        self.frame_dificuldade = ttk.LabelFrame(content_frame, text="Dificuldade", padding=10)
        self.frame_dificuldade.grid(row=2, column=1, sticky="nsew", pady=5, padx=5)
        
        ttk.Radiobutton(self.frame_dificuldade, text="Fácil", variable=self.dificuldade, 
                       value="facil").pack(anchor="w", padx=5, pady=3)
        ttk.Radiobutton(self.frame_dificuldade, text="Médio", variable=self.dificuldade, 
                       value="medio").pack(anchor="w", padx=5, pady=3)
        ttk.Radiobutton(self.frame_dificuldade, text="Difícil", variable=self.dificuldade, 
                       value="dificil").pack(anchor="w", padx=5, pady=3)
        
        # Frame de opções de tema
        frame_opcoes = ttk.LabelFrame(content_frame, text="Opções de Tema", padding=10)
        frame_opcoes.grid(row=3, column=0, columnspan=2, sticky="ew", pady=5)
        
        ttk.Label(frame_opcoes, text="Tema Visual:").grid(row=0, column=0, sticky="e", padx=5, pady=3)
        self.combo_tema = ttk.Combobox(frame_opcoes, textvariable=self.tema_selecionado, 
                                     values=["Claro", "Escuro", "Colorido"], state="readonly")
        self.combo_tema.grid(row=0, column=1, sticky="ew", padx=5, pady=3)
        self.combo_tema.bind("<<ComboboxSelected>>", self.mudar_tema)
        
        # Botão para começar o jogo
        btn_frame = ttk.Frame(content_frame)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=(20, 0))
        
        self.btn_comecar = ttk.Button(btn_frame, text="INICIAR JOGO", command=self.comecar_jogo)
        self.btn_comecar.pack(fill="x", ipady=5)
        
        # Configurar pesos
        content_frame.columnconfigure(0, weight=1)
        content_frame.columnconfigure(1, weight=1)
        frame_jogadores.columnconfigure(1, weight=1)
        frame_opcoes.columnconfigure(1, weight=1)

    def aplicar_tema(self, tema):
        """Aplica o tema selecionado à interface"""
        if tema == "Claro":
            self.style.theme_use('clam')
            bg_color = '#f0f0f0'
            fg_color = 'black'
            btn_bg = '#e1e1e1'
            active_bg = '#d5d5d5'
        elif tema == "Escuro":
            self.style.theme_use('alt')
            bg_color = '#333333'
            fg_color = 'white'
            btn_bg = '#555555'
            active_bg = '#666666'
        elif tema == "Colorido":
            self.style.theme_use('default')
            bg_color = '#e6f7ff'
            fg_color = '#0066cc'
            btn_bg = '#b3e0ff'
            active_bg = '#99ccff'
        
        # Aplicar cores aos elementos
        self.style.configure('.', background=bg_color, foreground=fg_color)
        self.style.configure('TFrame', background=bg_color)
        self.style.configure('TLabel', background=bg_color, foreground=fg_color)
        self.style.configure('TButton', background=btn_bg, foreground=fg_color)
        self.style.configure('TLabelframe', background=bg_color, foreground=fg_color)
        self.style.configure('TLabelframe.Label', background=bg_color, foreground=fg_color)
        self.style.map('TButton', background=[('active', active_bg)])

    def mudar_tema(self, event=None):
        """Muda o tema quando selecionado no combobox"""
        tema = self.tema_selecionado.get()
        self.aplicar_tema(tema)

    def on_window_resize(self, event):
        """Ajusta o layout quando a janela é redimensionada"""
        if self.root.state() == 'zoomed':
            for child in self.root.winfo_children():
                child.pack_configure(expand=True)
        else:
            for child in self.root.winfo_children():
                child.pack_configure(expand=False)

    def atualizar_opcoes(self):
        """Atualiza as opções da interface com base no modo de jogo selecionado"""
        if self.modo_jogo.get() == "maquina":
            self.frame_dificuldade.grid()
            self.nome_o_entry.config(state="disabled")
            self.nome_o_entry.delete(0, tk.END)
            self.nome_o_entry.insert(0, "Computador")
        else:
            self.frame_dificuldade.grid_remove()
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
        tema = self.tema_selecionado.get()

        if modo == "2jogadores":
            self.root.destroy()
            jogo_gui = JogoDaVelhaGUI(nome_x, nome_o)
            jogo_gui.iniciar()
        else:
            messagebox.showinfo("Aviso", "Opção contra máquina ainda não implementada.")

    def iniciar(self):
        """Inicia a interface gráfica"""
        self.root.mainloop()

if __name__ == "__main__":
    tela = TelaLogin()
    tela.iniciar()