Jogo de Damas com Python e Pygame

Este é um projeto acadêmico do jogo de Damas, desenvolvido como parte da disciplina de Algoritmos e Estruturas de Dados.

O objetivo principal foi aplicar os conceitos aprendidos em aula para criar um jogo funcional, com lógica de movimentação, captura e regras de turno, utilizando a biblioteca pygame para a interface gráfica. O jogo é autocontido em um único script Python, desenhando suas próprias peças sem a necessidade de arquivos de imagem externos.

🚀 Recursos Implementados

O jogo implementa as seguintes regras e funcionalidades:

Tabuleiro 8x8: Renderização de um tabuleiro oficial de damas com pygame.draw.rect.

Peças Desenhadas: As peças são desenhadas programaticamente com pygame.draw.circle.

Movimentação de Peças: Peças comuns podem se mover uma casa na diagonal, para frente.

Sistema de Turnos: O jogo alterna o controle entre o jogador das peças brancas (b) e o das peças pretas (p).

Captura de Peças: Implementação da captura por "pulo" simples por cima da peça adversária.

Coroação (Promoção): Peças comuns que alcançam a extremidade oposta do tabuleiro são promovidas a "Dama" (diferenciadas por uma "coroa" visual).

Lógica de Estado: O jogo gerencia o estado de "peça selecionada" para permitir a seleção (com destaque visual) e, em seguida, o movimento.

🏛️ Estrutura de Dados

O pilar do projeto é a estrutura de dados escolhida para representar o tabuleiro. Foi utilizada uma matriz 8x8 (lista de listas em Python), onde cada posição armazena um caractere que define o estado daquela casa:

"p": Peça comum preta

"b": Peça comum branca

"P": Dama preta

"B": Dama branca

" ": Casa jogável vazia

"-": Casa não jogável

Toda a lógica do jogo (eh_movimento_valido(), mover_peca()) e a renderização gráfica (desenhar_pecas()) operam lendo e modificando diretamente esta matriz.

🛠️ Tecnologias Utilizadas

Python 3.x: Linguagem base do projeto.

Pygame: Biblioteca utilizada para a criação da janela, renderização dos elementos gráficos (tabuleiro, peças) e captura de eventos do mouse.

▶️ Como Executar o Projeto

Para rodar este projeto em sua máquina local, siga os passos abaixo:

1. Pré-requisitos:

Você precisa ter o Python 3 instalado.

Você precisará da biblioteca pygame.

2. Instale as dependências:

O projeto requer apenas a biblioteca pygame. Você pode instalá-la usando pip:

pip install pygame


3. Execute o jogo:

Como o projeto é um único arquivo (damas.py) e não depende de imagens externas, basta executá-lo diretamente:

python damas.py


🧠 Próximos Passos (Melhorias Futuras)

Como o foco do projeto era a implementação da estrutura de dados e algoritmos básicos, existem várias melhorias que podem ser adicionadas:

[ ] Implementar a movimentação completa da "Dama" (múltiplas casas, para frente e para trás).

[ ] Adicionar a regra de "captura múltipla" em uma única jogada.

[ ] Criar um indicador visual de "Vencedor" ao final do jogo.

[ ] Adicionar um menu inicial.

[ ] (Desafio) Implementar uma Inteligência Artificial (IA) simples como oponente para aprendizado básico do jogo.