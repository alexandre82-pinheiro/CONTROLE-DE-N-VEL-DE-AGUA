# 💧 Sistema de Monitoramento de Níveis de Água

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Biblioteca-Colorama-orange?style=for-the-badge" alt="Colorama">
  <img src="https://img.shields.io/badge/Licença-MIT-blue.svg?style=for-the-badge" alt="License">
</p>

---

## 📋 Sobre o Projeto

O **Sistema de Monitoramento de Níveis de Água** é uma aplicação desenvolvida em Python para simular o comportamento de um painel de controle industrial ou residencial de reservatórios. O programa exibe mensagens de alerta em tempo de execução no terminal, utilizando cores dinâmicas para representar diferentes graus de risco e criticidade do volume de água.

---

## 🚀 Tecnologias Utilizadas

* **[Python](https://www.python.org/)** (Versão 3.14) - Linguagem principal de programação.
* **[Colorama](https://pypi.org/project/colorama/)** - Biblioteca utilizada para manipulação de cores e estilização de texto no terminal de forma multiplataforma.

---

## 📊 Estrutura de Níveis e Progressão de Risco

O sistema trabalha com uma lista estruturada contendo cinco níveis sequenciais de monitoramento:

| Nível do Reservatório | Situação / Alerta | Cor no Terminal |
| :--- | :--- | :--- |
| **Nível 1** | Muito baixo (crítico) | 🔴 Vermelho (`Fore.RED`) |
| **Nível 2** | Baixo | 🟡 Amarelo (`Fore.YELLOW`) |
| **Nível 3** | Médio | 🟢 Verde (`Fore.GREEN`) |
| **Nível 4** | Alto | 🔵 Ciano (`Fore.CYAN`) |
| **Nível 5** | Muito alto (alerta) | 🔵 Azul (`Fore.BLUE`) |

---

## ⚙️ Lógica de Funcionamento

A simulação percorre iterativamente uma lista de dicionários em Python. Cada elemento armazena o número do nível, a descrição da situação e a formatação de cor correspondente. Uma função dedicada (`exibir_alerta_reservatorio`) processa os dados e aplica a biblioteca `colorama` com autorrestauração (`autoreset=True`), garantindo que o terminal retorne ao padrão visual após cada exibição.

---

## 📥 Como Executar o Programa

Siga os passos abaixo para clonar, configurar e rodar o projeto em sua máquina:

Siga os passos abaixo para rodar a simulação no seu ambiente local:

1. Pré-requisitos

Certifique-se de ter o **Python** instalado em sua máquina. Você pode verificar executando no terminal:

python --version

2. Instalar a dependência

O projeto utiliza a biblioteca colorama. Instale-a via terminal executando:

pip install colorama

3. Executar o script

Baixe o arquivo Python do projeto, abra o terminal na pasta onde ele está salvo e execute o comando:

python nome_do_arquivo.py

(Substitua nome_do_arquivo.py pelo nome real do arquivo salvo em sua máquina).