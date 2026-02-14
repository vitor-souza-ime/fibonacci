# Fibonacci – Cálculo e Análise da Sequência

Repositório: https://github.com/vitor-souza-ime/fibonacci  
Arquivo principal: `main.py`

## 📌 Descrição

Este projeto implementa funcionalidades relacionadas à sequência de Fibonacci, incluindo cálculo de termos, análise de convergência e possíveis aplicações práticas da sequência em matemática e ciência da computação.

A sequência de Fibonacci é definida recursivamente por:

\[
F_0 = 0, \quad F_1 = 1
\]
\[
F_n = F_{n-1} + F_{n-2} \quad \text{para} \quad n \geq 2
\]

O repositório contém um script em Python (`main.py`) que calcula termos da sequência, exibe resultados e pode ser usado como base para experimentos com séries recursivas.

---

## 🔢 Funcionalidades

O arquivo principal `main.py` inclui:

- Cálculo de termos da sequência de Fibonacci
- Impressão dos primeiros **N termos** da sequência
- Cálculo iterativo e recursivo
- Possibilidade de comparação de desempenho entre métodos (se implementado)

---

## ▶️ Como executar

### 1️⃣ Clonar este repositório

```bash
git clone https://github.com/vitor-souza-ime/fibonacci.git
cd fibonacci
````

### 2️⃣ Instalar dependências

Este projeto foi desenvolvido com Python 3.8 ou superior. Não há dependências externas obrigatórias além da própria linguagem.

Caso seja necessário instalar pacotes externos, execute:

```bash
pip install -r requirements.txt
```

---

## ▶️ Executar o script

Para executar:

```bash
python main.py
```

Você poderá inserir um valor para **n** e receber os termos de Fibonacci correspondentes.

---

## 🧠 Conceitos Matemáticos

A sequência de Fibonacci é um dos exemplos mais clássicos de recorrência linear de segunda ordem. Suas propriedades incluem:

* Aproximação da razão áurea ( \phi ) através da razão entre termos consecutivos
* Aplicações em algoritmos, estruturas de dados e teoria dos números
* Relações com problemas de combinatória e modelagem de crescimento

---

## 🧪 Exemplos de Uso

Se `main.py` solicitar entrada, um exemplo de uso pode ser:

```
Digite a quantidade de termos: 10
Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

---

## 📚 Aplicações

* Análise de algoritmos (por exemplo, desempenho exponencial de recursões simples)
* Testes de otimização de código
* Exercícios de programação e matemática
* Modelagem de fenômenos naturais

---

## 📄 Licença

Este projeto está disponível para fins educacionais e de pesquisa.

```
