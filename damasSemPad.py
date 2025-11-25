import pygame
import os

def criar_tabuleiro():
    """Cria e retorna o tabuleiro inicial do jogo de damas em uma matriz 8x8."""
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

def eh_movimento_valido(tabuleiro, jogador, l_origem, c_origem, l_destino, c_destino):
    """Verifica se um movimento é válido (versão simplificada para GUI)."""
    peca = tabuleiro[l_origem][c_origem]
    if peca.lower() != jogador or tabuleiro[l_destino][c_destino] != " ":
        return False
    if peca in ('b', 'p'):
        direcao = -1 if jogador == 'b' else 1
        if l_destino == l_origem + direcao and abs(c_destino - c_origem) == 1:
            return True
        if abs(l_destino - l_origem) == 2 and abs(c_destino - c_origem) == 2:
            l_captura, c_captura = (l_origem + l_destino) // 2, (c_origem + c_destino) // 2
            peca_capturada = tabuleiro[l_captura][c_captura]
            if peca_capturada.lower() not in (" ", jogador):
                return True

    if peca in ('B', 'P'):
        if abs(l_destino - l_origem) == 1 and abs(c_destino - c_origem) == 1:
            return True
        if abs(l_destino - l_origem) == 2 and abs(c_destino - c_origem) == 2:
            l_captura, c_captura = (l_origem + l_destino) // 2, (c_origem + c_destino) // 2
            peca_capturada = tabuleiro[l_captura][c_captura]
            if peca_capturada.lower() not in (" ", jogador):
                return True

    return False

def mover_peca(tabuleiro, l_origem, c_origem, l_destino, c_destino):
    """Move a peça e promove a Dama se necessário."""
    peca = tabuleiro[l_origem][c_origem]
    tabuleiro[l_destino][c_destino] = peca
    tabuleiro[l_origem][c_origem] = " "

    if abs(l_destino - l_origem) == 2:
        l_captura, c_captura = (l_origem + l_destino) // 2, (c_origem + c_destino) // 2
        tabuleiro[l_captura][c_captura] = " "

    if peca == 'b' and l_destino == 0:
        tabuleiro[l_destino][c_destino] = 'B'
    elif peca == 'p' and l_destino == 7:
        tabuleiro[l_destino][c_destino] = 'P'

pygame.init()

LARGURA, ALTURA = 640, 640
LINHAS, COLUNAS = 8, 8
TAMANHO_CASA = LARGURA // COLUNAS
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Damas")

MARROM_ESCURO = (139, 69, 19)
MARROM_CLARO = (222, 184, 135)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE_DESTAQUE = (0, 255, 0) 

def desenhar_tabuleiro(tela):
    """Desenha as casas do tabuleiro."""
    tela.fill(MARROM_CLARO)
    for linha in range(LINHAS):
        for coluna in range(linha % 2, COLUNAS, 2):
            pygame.draw.rect(tela, MARROM_ESCURO, (linha*TAMANHO_CASA, coluna*TAMANHO_CASA, TAMANHO_CASA, TAMANHO_CASA))

def desenhar_pecas(tela, tabuleiro):
    """Desenha as peças com base na matriz do tabuleiro."""
    raio = TAMANHO_CASA // 2 - 10
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            peca = tabuleiro[linha][coluna]
            if peca != ' ' and peca != '-':
                centro_x = coluna * TAMANHO_CASA + TAMANHO_CASA // 2
                centro_y = linha * TAMANHO_CASA + TAMANHO_CASA // 2
                
                cor_peca = BRANCO if peca.lower() == 'b' else PRETO
                pygame.draw.circle(tela, cor_peca, (centro_x, centro_y), raio)
                
                if peca in ('B', 'P'):
                    pygame.draw.circle(tela, VERDE_DESTAQUE, (centro_x, centro_y), raio // 2)

def main():
    rodando = True
    clock = pygame.time.Clock()
    tabuleiro = criar_tabuleiro()
    jogador_atual = 'b'
    peca_selecionada = None

    while rodando:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                linha, coluna = pos_y // TAMANHO_CASA, pos_x // TAMANHO_CASA

                if peca_selecionada:
                    l_origem, c_origem = peca_selecionada
                    if eh_movimento_valido(tabuleiro, jogador_atual, l_origem, c_origem, linha, coluna):
                        mover_peca(tabuleiro, l_origem, c_origem, linha, coluna)
                        jogador_atual = 'p' if jogador_atual == 'b' else 'b'
                    peca_selecionada = None 
                else:
                    if tabuleiro[linha][coluna].lower() == jogador_atual:
                        peca_selecionada = (linha, coluna)

        desenhar_tabuleiro(tela)
        desenhar_pecas(tela, tabuleiro)
        
        if peca_selecionada:
            l, c = peca_selecionada
            pygame.draw.rect(tela, VERDE_DESTAQUE, (c*TAMANHO_CASA, l*TAMANHO_CASA, TAMANHO_CASA, TAMANHO_CASA), 4)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
