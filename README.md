# Trabalho de Engenharia de Software II - Padrões de Desenvolvimento

**Instituição:** Faculdades Senac  
**Disciplina:** Engenharia de Software II  
**Tema:** Padrão de Projeto *Adapter* (Estrutural)

---

## 👥 Integrantes do Grupo
Christian Pieper,
Guilherme Viegas

---

## 🎯 Objetivo do Trabalho
[cite_start]Estudar padrões de projeto, entender o seu funcionamento e aplicação prática através de um comparativo entre uma solução "ingênua" (sem padrão) e uma solução estruturada (com padrão)[cite: 1238].

## 🧩 O Padrão Escolhido: Adapter

O **Adapter** (ou Adaptador) é um padrão estrutural que permite que objetos com interfaces incompatíveis colaborem entre si.

> [cite_start]**Definição do GoF:** "Converter a interface de uma classe em outra interface, esperada pelos clientes. O Adapter permite que classes com interfaces incompatíveis trabalhem em conjunto – o que, de outra forma, seria impossível."[cite: 111, 977].

### Aplicação no Projeto (Jogo de Damas)
No contexto deste jogo de damas, o problema de incompatibilidade ocorre entre a **Interface Gráfica** (que "fala" em pixels da tela, ex: `x=450`, `y=300`) e a **Lógica do Jogo** (que "fala" em índices da matriz do tabuleiro, ex: `linha=4`, `coluna=3`).

---

## 📂 Estrutura do Código

O projeto contém dois arquivos principais para demonstração:

1.  `sem_adapter.py`: Implementação onde a lógica do jogo é obrigada a fazer cálculos matemáticos de tela (alto acoplamento).
2.  `com_adapter.py`: Implementação onde um **Adapter** traduz os pixels para coordenadas de tabuleiro, isolando o jogo da interface.

### Diagrama Conceitual (Adapter)

* **Client (Jogo):** Espera receber coordenadas limpas `(linha, coluna)`.
* **Adaptee (Pygame):** Fornece coordenadas brutas `(pixels_x, pixels_y)`.
* **Adapter (MouseParaTabuleiro):** Recebe os pixels do Adaptee e converte para o formato esperado pelo Client.

---

## 🚀 Como Executar

### Pré-requisitos
Você precisará ter o Python instalado e a biblioteca `pygame` e um pentium 486 ja roda o jogo.

```bash
pip install pygame
python damas.py
