# 🐍 Estudos de Python — Breno J. Oliveira

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Plataforma-Codedex-FF6B6B?style=for-the-badge" alt="Codedex">
  <img src="https://img.shields.io/badge/Módulos-2%2F8-orange?style=for-the-badge" alt="Módulos">
  <img src="https://img.shields.io/badge/Exercícios-9%2F9-brightgreen?style=for-the-badge" alt="Exercícios">
  <br>
  <img src="https://img.shields.io/badge/status-em%20progresso-yellow?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/nível-iniciante-blue?style=flat-square" alt="Nível">
  <img src="https://img.shields.io/badge/licença-MIT-blue?style=flat-square" alt="Licença">
</p>

---

## O que é este repositório?

Este repositório reúne todos os meus exercícios e projetos de **aprendizado de Python**, realizados pela plataforma [Codedex](https://www.codedex.io/). Cada pasta representa um módulo do curso, com os exercícios resolvidos e anotações de aprendizado.

Projeto de **estudo pessoal (solo)**, documentando minha evolução do zero até dominar Python na prática.

---

## O que já aprendi?

### Módulo 1 — Hello World
Primeiros passos com Python: saída de dados, formatação de texto e a função `print()`.

| Exercício | O que praticou | Arquivo |
|-----------|---------------|---------|
| **Hello World** | Primeiro `print()`, sintaxe básica de Python | `helloworld.py` |
| **Initials** | Arte ASCII com múltiplos `print()` | `Initials.py` |
| **Pattern** | Alinhamento e formatação de texto no terminal | `Pattern.py` |
| **Snail Mail** | Impressão de mensagens personalizadas | `Snail Mail.py` |

### Módulo 2 — Variables
Variáveis, tipos de dados, operações matemáticas e entrada do usuário com `input()`.

| Exercício | O que praticou | Arquivo |
|-----------|---------------|---------|
| **Variable** | Declaração de variáveis, tipos `str`, `float`, `bool`, f-strings | `variable.py` |
| **Temperature** | Conversão Fahrenheit → Celsius com operações aritméticas | `Temperature.py` |
| **BMI** | Cálculo de IMC com potenciação e f-strings formatadas | `BMI.py` |
| **Pythagorean Theorem** | Teorema de Pitágoras, `input()`, raiz quadrada | `Pythagorean Theorem.py` |
| **Currency** | Conversão de moedas (Peso, Sol, Real → Dólar) com múltiplos `input()` | `currency.py` |

---

## Exemplos de Código

### Hello World clássico
```python
print("Hello World")
```

### Calculadora de Hipotenusa
```python
print("Calculadora de Hipotenusa 3000")

a = int(input('Qual o valor de A no seu triangulo? '))
b = int(input('Agora qual é o valor do B do seu Triangulo? '))

c = ((a ** 2) + (b ** 2)) ** (1/2)

print(c)
```

### Conversor de Moedas
```python
peso  = int(input("What do you have left in pesos? "))
soles = int(input("What do you have left in soles? "))
reais = int(input("What do you have left in reais? "))

dolar = (peso * 0.00068) + (soles * 0.29) + (reais * 0.20)

print(dolar)
```

---

## Estrutura do Repositório

```
_estudos-python/
├── Codedex/
│   ├── 1. Hello World/
│   │   ├── Hello World/        ✅ print() básico
│   │   ├── Initials/           ✅ Arte ASCII com nome
│   │   ├── Pattern/            ✅ Padrão numérico
│   │   └── Snail Mail/         ✅ Mensagem personalizada
│   ├── 2. Variables/
│   │   ├── variable/           ✅ Tipos e f-strings
│   │   ├── Temperature/        ✅ Fahrenheit → Celsius
│   │   ├── BMI/                ✅ Cálculo de IMC
│   │   ├── Pythagorean Theorem/ ✅ Hipotenusa
│   │   └── Currency/           ✅ Conversor de moedas
│   ├── 3. Control Flow/        🔜 Em breve
│   ├── 4. Loops/               🔜 Em breve
│   ├── 5. Functions/           🔜 Em breve
│   ├── 6. List/                🔜 Em breve
│   ├── 7. Classes and Objects/ 🔜 Em breve
│   └── 8. Modules/             🔜 Em breve
└── Projects/                   🔜 Em breve
```

---

## Roadmap de Aprendizado

| Módulo | Conteúdo | Status |
|--------|----------|--------|
| **1. Hello World** | `print()`, sintaxe básica, saída de texto | ✅ Concluído |
| **2. Variables** | Variáveis, tipos, `input()`, operações matemáticas | ✅ Concluído |
| **3. Control Flow** | `if`, `elif`, `else`, operadores lógicos | 🔜 Planejado |
| **4. Loops** | `for`, `while`, `range()`, iterações | 🔜 Planejado |
| **5. Functions** | Definição de funções, parâmetros, `return` | 🔜 Planejado |
| **6. Lists** | Listas, índices, slicing, métodos de lista | 🔜 Planejado |
| **7. Classes and Objects** | POO, classes, instâncias, atributos | 🔜 Planejado |
| **8. Modules** | Importações, bibliotecas padrão, `pip` | 🔜 Planejado |
| **Projects** | Projetos práticos integrando tudo | 🔜 Planejado |

---

## Como Rodar os Exercícios

### Pré-requisitos
- Python 3.x instalado ([python.org](https://www.python.org/downloads/))

### Executando qualquer exercício
```bash
# Clone o repositório
git clone https://github.com/Breno-J-Oliveira/_estudos-python.git
cd _estudos-python

# Execute qualquer script Python
python "Codedex/1. Hello World/Hello World/helloworld.py"
python "Codedex/2. Variables/Currency/currency.py"
```

Exercícios com `input()` aguardam digitação no terminal — basta seguir os prompts.

---

## Plataforma de Estudo

Este repositório acompanha o curso de Python da **[Codedex](https://www.codedex.io/)** — plataforma gamificada de programação com exercícios práticos e progressão por capítulos.

---

## Contatos e Redes Sociais

<p align="center">
  <a href="https://github.com/Breno-J-Oliveira" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="https://www.linkedin.com/in/breno-j-oliveira-672619352/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="https://www.instagram.com/brenoov" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram">
  </a>
  <a href="https://x.com/BrenoJOliveira_" target="_blank">
    <img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" alt="X (Twitter)">
  </a>
</p>

---

<p align="center">
  <strong>🐍 Jornada em andamento — de Hello World ao Python avançado.</strong><br>
  2/8 módulos concluídos • 9/9 exercícios passando • progresso constante
</p>
