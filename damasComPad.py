# --- 1. A Interface do Jogo (Client) ---
class JogoDamas:
    def __init__(self):
        self.tabuleiro = [] # Matriz 8x8

    # O jogo agora é "limpo". Ele só entende a linguagem do tabuleiro (0 a 7).
    # Não sabe o que é um pixel ou tamanho de tela.
    def realizar_jogada(self, linha, coluna):
        print(f"[JOGO] Recebi comando limpo para atuar na Matriz [{linha}][{coluna}]")
        # Lógica de movimento aqui...

# --- 2. O Adaptado (Adaptee) - Simulando o Pygame ---
class SistemaPygame:
    def obter_evento_mouse(self):
        # Simula o Pygame retornando uma tupla de pixels bruta
        return (450, 300)  # Exemplo: x=450, y=300

# --- 3. O ADAPTER (A estrela do show) ---
class MouseParaTabuleiroAdapter:
    def __init__(self, tamanho_casa):
        self.tamanho_casa = tamanho_casa

    def converter_entrada(self, pos_pixels):
        """
        Adapta a interface de Pixels (Pygame) para a interface de Matriz (Jogo).
        """
        pixel_x, pixel_y = pos_pixels
        
        # A lógica de conversão fica isolada aqui
        coluna = pixel_x // self.tamanho_casa
        linha = pixel_y // self.tamanho_casa
        
        return linha, coluna

# --- Execução (Client Code) ---
if __name__ == "__main__":
    # Configuração
    TAMANHO_REAL_CASA = 80 # 640 / 8
    
    # Instanciação
    jogo = JogoDamas()
    pygame_simulado = SistemaPygame()
    
    # O Adapter é configurado com as regras de conversão
    adaptador = MouseParaTabuleiroAdapter(TAMANHO_REAL_CASA)

    print("--- INICIANDO COM ADAPTER ---")
    
    # 1. O sistema pega o dado bruto (Pixels)
    evento_mouse = pygame_simulado.obter_evento_mouse()
    print(f"[INPUT] Clique detectado nos pixels: {evento_mouse}")

    # 2. O Adapter traduz
    linha_convertida, col_convertida = adaptador.converter_entrada(evento_mouse)
    print(f"[ADAPTER] Traduzindo para coordenadas de tabuleiro...")

    # 3. O Jogo recebe o dado limpo
    jogo.realizar_jogada(linha_convertida, col_convertida)