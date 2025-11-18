import pygame

# Configurações "Hardcoded" que o jogo é obrigado a saber
LARGURA_TELA = 640
TAMANHO_CASA = LARGURA_TELA // 8

class JogoDamasSemPadrao:
    def __init__(self):
        self.tabuleiro = self.criar_tabuleiro()

    def criar_tabuleiro(self):
        # (Lógica simplificada de criação da matriz 8x8 do seu PDF)
        return [["-" for _ in range(8)] for _ in range(8)]

    def processar_clique(self, pos_mouse_x, pos_mouse_y):
        """
        PROBLEMA: A lógica do jogo está 'suja' com detalhes de interface.
        Ela sabe sobre pixels e matemática de tela.
        """
        # Conversão direta (Acoplamento forte com a interface gráfica)
        coluna = pos_mouse_x // TAMANHO_CASA
        linha = pos_mouse_y // TAMANHO_CASA
        
        print(f"[SEM PADRÃO] Processando clique nos Pixels ({pos_mouse_x}, {pos_mouse_y})")
        print(f"             Convertido internamente para Matriz [{linha}][{coluna}]")
        self.mover_peca(linha, coluna)

    def mover_peca(self, linha, coluna):
        print(f"             > Tentando mover peça na casa {linha}x{coluna}...")

# Simulação do Loop Principal
jogo = JogoDamasSemPadrao()
# O Pygame envia um clique na coordenada de tela (ex: 450px, 300px)
jogo.processar_clique(450, 300)