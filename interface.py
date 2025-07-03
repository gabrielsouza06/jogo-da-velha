import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.font import Font
from jogo import JogoDaVelha

class JogoDaVelhaGUI:
    def __init__(self, nome_x, nome_o, dificuldade="facil"):
        self.jogo = JogoDaVelha()
        self.jogo.jogadores['X'] = nome_x
        self.jogo.jogadores['O'] = nome_o
        self.jogo.dificuldade = dificuldade
        self.is_against_computer = (nome_o == "Computador")

        self.root = tk.Tk()
        self.root.title("Jogo da Velha")
        self.root.geometry("500x650")  # Aumentado para acomodar os novos botões
        self.root.minsize(450, 600)
        self.root.configure(bg='#f5f5f5')
        
        # Configuração de estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Cores personalizadas
        self.cores = {
            'fundo': '#f5f5f5',
            'fundo_card': '#ffffff',
            'texto': '#333333',
            'destaque': '#4a6fa5',
            'botao': '#4a6fa5',
            'botao_hover': '#3a5a8f',
            'borda': '#e0e0e0',
            'celula': '#f0f0f0',
            'celula_hover': '#e0e0e0',
            'texto_celula': '#333333',
            'botao_secundario': '#6c757d',
            'botao_secundario_hover': '#5a6268'
        }
        
        # Frame principal
        self.main_frame = tk.Frame(self.root, bg=self.cores['fundo'])
        self.main_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        # Card central
        self.card = tk.Frame(self.main_frame, bg=self.cores['fundo_card'],
                          bd=0, highlightthickness=0, relief='flat')
        self.card.pack(expand=True, fill="both")
        
        # Cabeçalho
        self.cabecalho = tk.Frame(self.card, bg=self.cores['fundo_card'], 
                                height=60, bd=0, highlightthickness=0)
        self.cabecalho.pack(fill="x", pady=(10, 5), padx=20)
        
        # Label de informação
        info_font = Font(family='Helvetica', size=14)
        self.label_info = tk.Label(
            self.cabecalho, 
            text=f"Vez de {self.jogo.jogadores[self.jogo.jogador_atual]} ({self.jogo.jogador_atual})",
            font=info_font,
            bg=self.cores['fundo_card'],
            fg=self.cores['destaque']
        )
        self.label_info.pack(side="top", pady=(5, 10))
        
        # Frame do tabuleiro
        self.frame_tabuleiro = tk.Frame(self.card, bg=self.cores['fundo_card'])
        self.frame_tabuleiro.pack(pady=(0, 20))
        
        # Criar tabuleiro
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        self.criar_tabuleiro()
        
        # Frame de rodapé
        self.rodape = tk.Frame(self.card, bg=self.cores['fundo_card'])
        self.rodape.pack(fill="x", pady=(0, 10))
        
        # Frame para os botões de ação
        self.frame_botoes_acao = tk.Frame(self.rodape, bg=self.cores['fundo_card'])
        self.frame_botoes_acao.pack(fill="x", expand=True)
        
        # Botão de revanche (só aparece no modo PvP)
        self.btn_revanche = tk.Button(
            self.frame_botoes_acao,
            text="Revanche",
            command=self.revanche,
            bg=self.cores['botao_secundario'],
            fg='white',
            bd=0,
            highlightthickness=0,
            activebackground=self.cores['botao_secundario_hover'],
            activeforeground='white',
            padx=15,
            pady=8,
            font=('Helvetica', 10),
            state='disabled'  # Inicialmente desabilitado
        )
        self.btn_revanche.pack(side="left", padx=5, expand=True, fill="x")
        
        # Botão de jogar novamente (só aparece no modo vs Computador)
        self.btn_jogar_novamente = tk.Button(
            self.frame_botoes_acao,
            text="Jogar Novamente",
            command=self.reiniciar_jogo,
            bg=self.cores['botao'],
            fg='white',
            bd=0,
            highlightthickness=0,
            activebackground=self.cores['botao_hover'],
            activeforeground='white',
            padx=15,
            pady=8,
            font=('Helvetica', 10),
            state='disabled'  # Inicialmente desabilitado
        )
        self.btn_jogar_novamente.pack(side="left", padx=5, expand=True, fill="x")
        
        # Botão de voltar ao lobby
        self.btn_voltar_lobby = tk.Button(
            self.frame_botoes_acao,
            text="Voltar ao Lobby",
            command=self.voltar_lobby,
            bg=self.cores['botao_secundario'],
            fg='white',
            bd=0,
            highlightthickness=0,
            activebackground=self.cores['botao_secundario_hover'],
            activeforeground='white',
            padx=15,
            pady=8,
            font=('Helvetica', 10)
        )
        self.btn_voltar_lobby.pack(side="left", padx=5, expand=True, fill="x")
        
        # Configurar visibilidade dos botões conforme o modo de jogo
        self.atualizar_botoes_acao()
        
        # Se for contra o computador e for a vez dele, faz a primeira jogada
        if self.is_against_computer and self.jogo.jogador_atual == 'O':
            self.root.after(500, self.jogada_computador)
        
        # Centralizar na tela
        self.root.eval('tk::PlaceWindow . center')

    def atualizar_botoes_acao(self):
        """Atualiza a visibilidade dos botões de ação conforme o modo de jogo"""
        if self.is_against_computer:
            self.btn_revanche.pack_forget()
            self.btn_jogar_novamente.pack(side="left", padx=5, expand=True, fill="x")
        else:
            self.btn_jogar_novamente.pack_forget()
            self.btn_revanche.pack(side="left", padx=5, expand=True, fill="x")

    def criar_tabuleiro(self):
        for i in range(3):
            for j in range(3):
                botao = tk.Button(
                    self.frame_tabuleiro,
                    text=" ",
                    width=6,
                    height=3,
                    font=('Helvetica', 24, 'bold'),
                    bg=self.cores['celula'],
                    fg=self.cores['texto_celula'],
                    activebackground=self.cores['celula_hover'],
                    bd=0,
                    highlightthickness=0,
                    command=lambda linha=i, coluna=j: self.jogar(linha, coluna)
                )
                botao.grid(row=i, column=j, padx=5, pady=5, ipadx=10, ipady=10)
                self.botoes[i][j] = botao
                
                # Efeito hover nas células
                botao.bind("<Enter>", lambda e, b=botao: b.config(bg=self.cores['celula_hover']))
                botao.bind("<Leave>", lambda e, b=botao: b.config(bg=self.cores['celula']))

    def jogar(self, linha, coluna):
        # Verifica se é um jogo contra computador e se é a vez do jogador humano
        if self.is_against_computer and self.jogo.jogador_atual == 'O':
            return
        
        celula = self.jogo.tabuleiro[linha][coluna]
        if celula.esta_vazia():
            celula.simbolo = self.jogo.jogador_atual
            self.botoes[linha][coluna].config(
                text=self.jogo.jogador_atual,
                fg='red' if self.jogo.jogador_atual == 'X' else 'blue'
            )

            if self.jogo.verificar_vitoria():
                self.fim_de_jogo(f"{self.jogo.jogadores[self.jogo.jogador_atual]} venceu!")
            elif self.jogo.tabuleiro_cheio():
                self.fim_de_jogo("Empate!")
            else:
                # Alternar jogador
                self.jogo.jogador_atual = 'O' if self.jogo.jogador_atual == 'X' else 'X'
                self.label_info.config(
                    text=f"Vez de {self.jogo.jogadores[self.jogo.jogador_atual]} ({self.jogo.jogador_atual})",
                    fg='red' if self.jogo.jogador_atual == 'X' else 'blue'
                )
                
                # Se for contra o computador e for a vez dele, faz a jogada
                if self.is_against_computer and self.jogo.jogador_atual == 'O':
                    self.root.after(500, self.jogada_computador)
        else:
            messagebox.showinfo("Jogada inválida", "Essa célula já está ocupada.")

    def jogada_computador(self):
        """Realiza a jogada do computador"""
        # Desabilita os botões durante a jogada do computador
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(state='disabled')
        
        # Faz a jogada
        jogada = self.jogo.jogada_computador()
        if jogada:
            linha, coluna = jogada
            self.jogo.tabuleiro[linha][coluna].simbolo = self.jogo.jogador_atual
            self.botoes[linha][coluna].config(
                text=self.jogo.jogador_atual,
                fg='red' if self.jogo.jogador_atual == 'X' else 'blue'
            )
            
            # Verifica resultado
            if self.jogo.verificar_vitoria():
                self.fim_de_jogo(f"{self.jogo.jogadores[self.jogo.jogador_atual]} venceu!")
            elif self.jogo.tabuleiro_cheio():
                self.fim_de_jogo("Empate!")
            else:
                # Alternar jogador
                self.jogo.jogador_atual = 'O' if self.jogo.jogador_atual == 'X' else 'X'
                self.label_info.config(
                    text=f"Vez de {self.jogo.jogadores[self.jogo.jogador_atual]} ({self.jogo.jogador_atual})",
                    fg='red' if self.jogo.jogador_atual == 'X' else 'blue'
                )
        
        # Reabilita os botões após a jogada
        for i in range(3):
            for j in range(3):
                if self.jogo.tabuleiro[i][j].esta_vazia():
                    self.botoes[i][j].config(state='normal')

    def fim_de_jogo(self, mensagem):
        # Desabilitar todos os botões do tabuleiro
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(state='disabled')
        
        # Habilitar os botões de ação apropriados
        if self.is_against_computer:
            self.btn_jogar_novamente.config(state='normal')
        else:
            self.btn_revanche.config(state='normal')
        
        self.btn_voltar_lobby.config(state='normal')
        
        # Mostrar mensagem de fim de jogo
        self.jogo.resultado = mensagem
        self.jogo.salvar()

    def revanche(self):
        """Reinicia o jogo trocando os jogadores de posição"""
        # Troca os jogadores
        nome_x = self.jogo.jogadores['O']
        nome_o = self.jogo.jogadores['X']
        
        # Reinicia o jogo
        self.jogo = JogoDaVelha()
        self.jogo.jogadores['X'] = nome_x
        self.jogo.jogadores['O'] = nome_o
        
        # Resetar a interface
        self.label_info.config(
            text=f"Vez de {self.jogo.jogadores[self.jogo.jogador_atual]} ({self.jogo.jogador_atual})",
            fg=self.cores['destaque']
        )
        
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text=" ", state='normal', fg=self.cores['texto_celula'])
        
        # Desabilita os botões de ação até o próximo fim de jogo
        self.btn_revanche.config(state='disabled')
        self.btn_voltar_lobby.config(state='disabled')

    def reiniciar_jogo(self):
        """Reinicia o jogo com as mesmas configurações"""
        # Mantém os nomes e dificuldade
        nome_x = self.jogo.jogadores['X']
        nome_o = self.jogo.jogadores['O']
        dificuldade = self.jogo.dificuldade
        
        # Reinicia o jogo
        self.jogo = JogoDaVelha()
        self.jogo.jogadores['X'] = nome_x
        self.jogo.jogadores['O'] = nome_o
        self.jogo.dificuldade = dificuldade
        
        # Resetar a interface
        self.label_info.config(
            text=f"Vez de {self.jogo.jogadores[self.jogo.jogador_atual]} ({self.jogo.jogador_atual})",
            fg=self.cores['destaque']
        )
        
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text=" ", state='normal', fg=self.cores['texto_celula'])
        
        # Desabilita os botões de ação até o próximo fim de jogo
        self.btn_jogar_novamente.config(state='disabled')
        self.btn_voltar_lobby.config(state='disabled')
        
        # Se for contra o computador e for a vez dele, faz a primeira jogada
        if self.is_against_computer and self.jogo.jogador_atual == 'O':
            self.root.after(500, self.jogada_computador)

    def voltar_lobby(self):
        """Fecha a janela do jogo e volta para a tela de login"""
        self.root.destroy()
        from login import TelaLogin
        tela_login = TelaLogin()
        tela_login.iniciar()

    def iniciar(self):
        self.root.mainloop()