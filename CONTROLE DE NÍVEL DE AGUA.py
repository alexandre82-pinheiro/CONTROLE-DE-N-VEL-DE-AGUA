from colorama import Fore, Style, init

# Inicializa o colorama para gerenciar as cores no terminal (autoreset garante a restauração padrão)

init(autoreset=True)

# Lista contendo os dados dos cinco níveis do reservatório, suas situações e cores correspondentes

niveis_reservatorio = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE}
]

def exibir_alerta_reservatorio(dados_nivel):
    cor = dados_nivel["cor"]
    nivel = dados_nivel["nivel"]
    situacao = dados_nivel["situacao"]
    
    # Exibe a mensagem formatada com a cor específica e restaura o estilo ao final
    print(f"{cor}[ALERTA] Nível {nivel} - Situação: {situacao}{Style.RESET_ALL}")

def simular_monitoramento():
    ("=" * 60)
    print(" SIMULAÇÃO DE MONITORAMENTO DO RESERVATÓRIO DE ÁGUA ")
    print("=" * 60)
    
    # Percorre a lista simulando a variação dos níveis
    
    for item in niveis_reservatorio:
        exibir_alerta_reservatorio(item)
if __name__ == "__main__":
    simular_monitoramento()