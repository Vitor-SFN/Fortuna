import tkinter as tk
import math

class Table(tk.Frame):
    def __init__(self, master, jogadores):
        super().__init__(master)
        self.master = master
        self.jogadores = jogadores
        self.num_jogadores = len(jogadores)

        # --- Configurações Visuais (você pode ajustar aqui) ---
        self.LARGURA_JANELA = 1200
        self.ALTURA_JANELA = 1200
        self.COR_MESA = "#a06a50"  #Marrom
        self.COR_JOGADOR = "black"
        self.RAIO_MESA = 200
        self.TAMANHO_CORPO_JOGADOR = 90
        self.LARGURA_CORPO_JOGADOR = 40
        self.RAIO_CABECA_JOGADOR = 20
        self.DISTANCIA_JOGADOR_DA_MESA = 5

        # Janela principal
        self.master.title(f"Mesa com {self.num_jogadores} jogadores")
        self.master.geometry(f"{self.LARGURA_JANELA}x{self.ALTURA_JANELA}")

        # Cria o Canvas (a área de desenho)
        self.canvas = tk.Canvas(self.master, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # Desenha a cena
        self.desenhar_cena()


    def desenhar_cena(self):
        """Limpa o canvas e desenha a mesa e todos os jogadores."""
        self.canvas.delete("all")

        centro_x = self.LARGURA_JANELA / 2
        centro_y = self.ALTURA_JANELA / 2

        # 1. Desenha a Mesa
        self.canvas.create_oval(
            centro_x - self.RAIO_MESA,
            centro_y - self.RAIO_MESA,
            centro_x + self.RAIO_MESA,
            centro_y + self.RAIO_MESA,
            fill=self.COR_MESA,
            outline="black",
            width=2
        )

        # 2. Desenha cada jogador
        if self.num_jogadores == 0:
            return

        # Calcula o ângulo entre cada jogador em radianos
        angulo_incremento = 2 * math.pi / self.num_jogadores

        for i, nome in enumerate(self.jogadores):
            # Calcula o ângulo para o jogador atual
            # Adicionamos -math.pi / 2 para que o primeiro jogador comece no topo
            angulo = i * angulo_incremento - (math.pi / 2)

            # --- Calcula as posições usando trigonometria ---

            # Posição do corpo (mais perto da mesa)
            raio_corpo = self.RAIO_MESA + self.DISTANCIA_JOGADOR_DA_MESA
            x_corpo = centro_x + raio_corpo * math.cos(angulo)
            y_corpo = centro_y + raio_corpo * math.sin(angulo)

            # Posição da cabeça (mais longe da mesa)
            raio_cabeca = raio_corpo + self.TAMANHO_CORPO_JOGADOR
            x_cabeca = centro_x + raio_cabeca * math.cos(angulo)
            y_cabeca = centro_y + raio_cabeca * math.sin(angulo)

            # Posição do nome (acima da cabeça)
            raio_nome = raio_cabeca + self.RAIO_CABECA_JOGADOR + 60
            x_nome = centro_x + raio_nome * math.cos(angulo)
            y_nome = centro_y + raio_nome * math.sin(angulo)

            # --- Desenha os elementos do jogador ---

            # Corpo (desenhado como uma linha grossa)
            self.canvas.create_line(
                x_corpo, y_corpo, x_cabeca, y_cabeca,
                fill=self.COR_JOGADOR,
                width=self.LARGURA_CORPO_JOGADOR
            )

            # Cabeça (um círculo)
            self.canvas.create_oval(
                x_cabeca - self.RAIO_CABECA_JOGADOR,
                y_cabeca - self.RAIO_CABECA_JOGADOR,
                x_cabeca + self.RAIO_CABECA_JOGADOR,
                y_cabeca + self.RAIO_CABECA_JOGADOR,
                fill=self.COR_JOGADOR,
                outline=self.COR_JOGADOR
            )

            # Nome
            self.canvas.create_text(
                x_nome, y_nome,
                text=nome,
                font=("Arial", 12, "bold"),
                fill="black"
            )