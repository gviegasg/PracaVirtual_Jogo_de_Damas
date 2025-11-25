import pygame

# --- CONFIGURAÇÕES GERAIS ---
LARGURA, ALTURA = 640, 640
LINHAS, COLUNAS = 8, 8
TAMANHO_CASA = LARGURA // COLUNAS

# Cores
MARROM_ESCURO = (139, 69, 19)
MARROM_CLARO = (222, 184, 135)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE_DESTAQUE = (0, 255, 0)
CINZA = (128, 128, 128)

# --- 1. LÓGICA DO JOGO (CLIENT) ---
# Esta classe contém TODA a regra de negócio. 
# Ela não sabe que existe Pygame, mouse ou pixels. Só entende matrizes.

class JogoDamas:
    def __init__(self):
        self.tabuleiro = self.criar_tabuleiro()
        self.jogador_atual = 'b' # 'b' para brancas, 'p' para pretas
        self.peca_selecionada = None # Guarda a tupla (linha, coluna) da peça selecionada

    def criar_tabuleiro(self):
        """Cria e retorna a matriz 8x8 inicial."""
        tabuleiro = []
        for i in range(8):
            linha = []
            for j in range(8):
                if (i + j) % 2 != 0:
                    if i < 3:
                        linha.append("p")
                    elif i > 4:
                        linha.append("b")
                    else:
                        linha.append(" ")
                else:
                    linha.append("-")
            tabuleiro.append(linha)
        return tabuleiro

    def processar_jogada(self, linha, coluna):
        """
        Recebe coordenadas LIMPAS (0-7) e decide se seleciona ou move.
        Este é o método principal que o Adapter vai alimentar.
        """
        print(f"[JOGO] Processando ação na casa [{linha}, {coluna}]")
        
        # Se já tem peça selecionada, tenta mover
        if self.peca_selecionada:
            l_origem, c_origem = self.peca_selecionada
            if self.eh_movimento_valido(l_origem, c_origem, linha, coluna):
                self.mover_peca(l_origem, c_origem, linha, coluna)
                self.trocar_turno()
                self.peca_selecionada = None # Desseleciona
            else:
                # Se clicou em outra peça sua, troca a seleção
                peca_clicada = self.tabuleiro[linha][coluna]
                if peca_clicada.lower() == self.jogador_atual:
                    self.peca_selecionada = (linha, coluna)
                else:
                    self.peca_selecionada = None # Clique inválido, cancela
        
        # Se não tem seleção, tenta selecionar
        else:
            peca = self.tabuleiro[linha][coluna]
            if peca.lower() == self.jogador_atual:
                self.peca_selecionada = (linha, coluna)

    def eh_movimento_valido(self, l_origem, c_origem, l_destino, c_destino):
        """Verifica regras de movimento."""
        peca = self.tabuleiro[l_origem][c_origem]
        
        # Verifica limites e se destino está vazio
        if not (0 <= l_destino < 8 and 0 <= c_destino < 8): return False
        if self.tabuleiro[l_destino][c_destino] != " ": return False

        # Regras para peças comuns
        if peca in ('b', 'p'):
            direcao = -1 if self.jogador_atual == 'b' else 1
            
            # Movimento simples
            if l_destino == l_origem + direcao and abs(c_destino - c_origem) == 1:
                return True
            
            # Captura simples
            if abs(l_destino - l_origem) == 2 and abs(c_destino - c_origem) == 2:
                l_cap = (l_origem + l_destino) // 2
                c_cap = (c_origem + c_destino) // 2
                peca_cap = self.tabuleiro[l_cap][c_cap]
                if peca_cap.lower() not in (" ", "-", self.jogador_atual):
                    return True

        # Regras para Damas (B, P)
        if peca in ('B', 'P'):
            if abs(l_destino - l_origem) == abs(c_destino - c_origem): # Diagonal
                dist = abs(l_destino - l_origem)
                if dist == 1: return True # Movimento curto
                if dist == 2: # Captura curta (simplificado)
                    l_cap = (l_origem + l_destino) // 2
                    c_cap = (c_origem + c_destino) // 2
                    if self.tabuleiro[l_cap][c_cap].lower() not in (" ", "-", self.jogador_atual):
                        return True
        return False

    def mover_peca(self, l_orig, c_orig, l_dest, c_dest):
        """Executa o movimento na matriz."""
        peca = self.tabuleiro[l_orig][c_orig]
        self.tabuleiro[l_dest][c_dest] = peca
        self.tabuleiro[l_orig][c_orig] = " "

        # Captura (remove peça)
        if abs(l_dest - l_orig) == 2:
            l_cap = (l_orig + l_dest) // 2
            c_cap = (c_orig + c_dest) // 2
            self.tabuleiro[l_cap][c_cap] = " "

        # Promoção à Dama
        if peca == 'b' and l_dest == 0:
            self.tabuleiro[l_dest][c_dest] = 'B'
        elif peca == 'p' and l_dest == 7:
            self.tabuleiro[l_dest][c_dest] = 'P'

    def trocar_turno(self):
        self.jogador_atual = 'p' if self.jogador_atual == 'b' else 'b'


# --- 2. O ADAPTER (A estrela do show) ---
class PygameMouseAdapter:
    """
    Converte a interface de entrada do Pygame (Pixels) 
    para a interface do Jogo (Linha/Coluna).
    """
    def __init__(self, tamanho_casa):
        self.tamanho_casa = tamanho_casa

    def converter_clique(self, pos_pixels):
        """
        Entrada: (x, y) em pixels
        Saída: (linha, coluna) índices da matriz
        """
        x, y = pos_pixels
        coluna = x // self.tamanho_casa
        linha = y // self.tamanho_casa
        return linha, coluna


# --- 3. INTERFACE GRÁFICA (VIEW) ---
# Responsável apenas por desenhar o estado atual do jogo na tela.
class InterfaceGrafica:
    def __init__(self, tela):
        self.tela = tela

    def desenhar(self, jogo):
        self.desenhar_tabuleiro()
        self.desenhar_pecas(jogo.tabuleiro)
        self.desenhar_destaque(jogo.peca_selecionada)
        pygame.display.flip()

    def desenhar_tabuleiro(self):
        self.tela.fill(MARROM_CLARO)
        for linha in range(LINHAS):
            for coluna in range(linha % 2, COLUNAS, 2):
                pygame.draw.rect(self.tela, MARROM_ESCURO, 
                               (coluna*TAMANHO_CASA, linha*TAMANHO_CASA, TAMANHO_CASA, TAMANHO_CASA))

    def desenhar_pecas(self, tabuleiro):
        raio = TAMANHO_CASA // 2 - 10
        for l in range(LINHAS):
            for c in range(COLUNAS):
                peca = tabuleiro[l][c]
                if peca != ' ' and peca != '-':
                    x = c * TAMANHO_CASA + TAMANHO_CASA // 2
                    y = l * TAMANHO_CASA + TAMANHO_CASA // 2
                    cor = BRANCO if peca.lower() == 'b' else PRETO
                    pygame.draw.circle(self.tela, cor, (x, y), raio)
                    # Coroa da dama
                    if peca in ('B', 'P'):
                        pygame.draw.circle(self.tela, VERDE_DESTAQUE, (x, y), raio // 3)

    def desenhar_destaque(self, selecionada):
        if selecionada:
            l, c = selecionada
            pygame.draw.rect(self.tela, VERDE_DESTAQUE, 
                           (c*TAMANHO_CASA, l*TAMANHO_CASA, TAMANHO_CASA, TAMANHO_CASA), 4)


# --- 4. EXECUÇÃO (MAIN LOOP) ---
def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Damas com Adapter Pattern")
    clock = pygame.time.Clock()

    # --- Instanciação dos Componentes ---
    
    # 1. O Jogo (Regras puras, não sabe de pixels)
    jogo = JogoDamas()
    
    # 2. O Adapter (Sabe converter Mouse -> Tabuleiro)
    input_adapter = PygameMouseAdapter(TAMANHO_CASA)
    
    # 3. A View (Sabe desenhar)
    gui = InterfaceGrafica(tela)

    rodando = True
    while rodando:
        clock.tick(60)

        # --- INPUT (Via Adapter) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 1. Obtém dado bruto (incompatível com o jogo)
                posicao_pixels = pygame.mouse.get_pos()
                print(f"[INPUT] Clique bruto: {posicao_pixels}")

                # 2. Adapter converte para dado compatível
                linha, coluna = input_adapter.converter_clique(posicao_pixels)
                
                # 3. Jogo recebe o dado limpo
                jogo.processar_jogada(linha, coluna)

        # --- DRAW ---
        gui.desenhar(jogo)

    pygame.quit()

if __name__ == "__main__":
    main()
