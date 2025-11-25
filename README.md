# Trabalho de Engenharia de Software II - Padrões de Projeto (Design Patterns)

**Instituição:** Faculdades Senac  
**Disciplina:** Engenharia de Software II  
**Entrega:** 25/11/2025  
**Categoria de Padrões:** Estruturais (Structural Patterns)

---

## 👥 Integrantes do Grupo
1. **Guilherme Viegas** - Responsável pelo Padrão **Adapter** (Projeto: Jogo de Damas)
2. **Christian Pieper** - Responsável pelo Padrão **Facade** (Projeto: Calculadora Financeira)

---

## 🎯 Objetivo do Trabalho
Estudar e aplicar padrões de projeto do GoF (Gang of Four), demonstrando na prática a diferença entre uma implementação "ingênua" (sem padrões) e uma solução arquiteturalmente robusta (com padrões). O grupo focou na categoria de **Padrões Estruturais**, que lidam com a composição de classes e objetos.

---

## 🧩 Padrão 1: Adapter (Aplicado ao Jogo de Damas)

### Contexto do Problema
No desenvolvimento do Jogo de Damas, surgiu um problema clássico de incompatibilidade de interfaces:
* **O Motor do Jogo (Domínio):** Trabalha com uma matriz lógica 8x8 (linhas 0-7, colunas 0-7).
* **A Interface Gráfica (Pygame):** Trabalha com coordenadas de tela em pixels (ex: x=450, y=300).

Na solução sem padrão, a lógica do jogo estava "suja", misturando regras de damas com cálculos matemáticos de pixels, violando o princípio de responsabilidade única.

### A Solução (Adapter)
O padrão **Adapter** (Adaptador) foi utilizado para criar uma ponte entre essas duas interfaces incompatíveis. Ele age como um tradutor: recebe os cliques em pixels do Pygame, converte matemática e geometricamente, e entrega coordenadas limpas (linha, coluna) para o jogo.

### 📂 Estrutura dos Arquivos
* `damasSemPad.py`: **Implementação sem o padrão.** Demonstra o acoplamento forte, onde a classe do jogo é obrigada a conhecer o tamanho da tela e fazer contas de divisão para entender onde o usuário clicou.
* `damasComPad.py`: **Implementação com Adapter.** Introduz a classe `MouseParaTabuleiroAdapter`, que isola completamente a lógica de conversão. O jogo passa a receber apenas comandos limpos.
* `damas.py`: O jogo completo funcional (utilizando a lógica demonstrada).

### ⚖️ Análise Crítica (Pontos Fortes e Fracos)

**✅ Pontos Fortes (Pros):**
* **Desacoplamento:** A lógica do jogo não sabe mais que existe uma tela ou pixels. Isso permite trocar a interface gráfica (ex: de Pygame para Terminal) sem mexer nas regras do jogo.
* **Princípio de Responsabilidade Única (SRP):** A conversão de dados fica isolada na classe adaptadora, limpando o código de negócio.
* **Reutilização:** Permite integrar classes legadas ou bibliotecas de terceiros sem alterar seu código original.

**❌ Pontos Fracos (Cons):**
* **Complexidade:** Para problemas muito simples, criar uma classe extra (Adapter) pode ser um excesso de engenharia (*overkill*).
* **Overhead:** Adiciona uma pequena camada indireta de processamento, embora irrelevante para este tipo de jogo.

---

## 🔄 Comparativo do Grupo: Adapter vs. Facade

Embora ambos sejam padrões **Estruturais** (funcionam como "wrappers" ou invólucros de outras classes), seus propósitos identificados no trabalho foram distintos:

| Característica | Adapter (Jogo de Damas) | Facade (Calculadora Financeira) |
| :--- | :--- | :--- |
| **Problema** | Incompatibilidade de interfaces (A não encaixa em B). | Complexidade de subsistema (Muitas classes difíceis de usar). |
| **Solução** | **Conversão**. Faz a tradução de dados (Pixels $\to$ Matriz). | **Simplificação**. Cria uma interface única para várias funções matemáticas. |
| **Objetivo** | Fazer funcionar junto o que não foi feito para tal. | Tornar o uso do sistema mais fácil e limpo. |

---

## 🚀 Como Executar

Certifique-se de ter o Python e o Pygame instalados:

```bash
pip install pygame
