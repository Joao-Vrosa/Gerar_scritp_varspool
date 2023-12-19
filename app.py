import random  # Gerar números pseudoaleatórios
from colorama import Fore, Style  # Inserir cores no terminal
from time import sleep
import os


# VARSPOOL

def gerar_comandos_varspool(arquivo_quarentena, nomenclatura_retorno, id_caixa_retorno, parametro_conect_vrs, contadores_utilizados):
    """
    -> Esta fução recebe os parametros inseridos na função dados e gera os scripts.
    arquivo_quarentena: Nomenclatura do arquivos que está em quarentena;
    nomenclatura_retorno: Nomenclatura renomeada dos arquivos;
    id_caixa_retorno: ID da caixa postal onde esta o cadastro (caixa postal cliente);
    parametro_conect_vrs: Parametro de retorno do CONNECT ou RVS;
    return: Retorna a lista comandos com os scripts gerados;
    Criado por João V. Rosa
    """
    lista_arquivos = arquivo_quarentena.split()
    lista_nomenclatura = nomenclatura_retorno.split()

    comandos = []

    # Gerando Contador
    for i in range(len(lista_arquivos)):
        contador = random.randint(111111111, 999999999)

        # Verificando se o contador ja existe
        while contador in contadores_utilizados:
            print(f'{Fore.YELLOW}[ALERTA]{Style.RESET_ALL} O {contador} ja existe, gerando um novo contador...')
            contador = random.randint(111111111, 999999999)

        # Gerando o script
        comando = f'mv -v {lista_arquivos[i]} /var/spool/nexxera/skyline/recebe/ident/{lista_nomenclatura[i]}.{id_caixa_retorno}.T{contador}.{parametro_conect_vrs}'
        comandos.append(comando)

        contadores_utilizados.append(contador)

    return comandos


def dados_varspool():
    """
    -> Esta função recebe os dados de entrada e escreve a saida dos scripts na tela.
    return: Sem retorno.
    Criado por João V. Rosa
    """
    try:
        contadores_utilizados = list()

        print("\n---------------------------- DADOS DE ENTRADA ----------------------------")
        arquivo_quarentena = input("> Nome do arquivo: ")
        nomenclatura_retorno = input("> DSNAME de retorno: ")
        id_caixa_retorno = int(input("> ID cliente: "))
        parametro_conect_vrs = input("> Parâmetro Connect/RVS: ")
        print("--------------------------------------------------------------------------")

        comandos_gerados = gerar_comandos_varspool(arquivo_quarentena, nomenclatura_retorno, id_caixa_retorno, parametro_conect_vrs, contadores_utilizados)

        print("\n\n\n---------------------------- COMANDOS GERADOS ----------------------------")
        for cmd in comandos_gerados:
            print(cmd)
        print("--------------------------------------------------------------------------\n")

        # Gerando um contador apos a geração dos scripts
        contador_segundo(tempo_total=45)

    except ValueError as erro:
        print(f'{Fore.RED}ERRO: {Style.RESET_ALL}{Style.BRIGHT}{erro}{Style.RESET_ALL}')


# Contador dinamico

def contador_segundo(tempo_total):
    """
    -> Funcao criada para gerar um contador dinamico, infomando o tempo restante da execucao da aplicacao.
    return: Sem retorno
    Criado por João V. Rosa
    """
    for segundos_restantes in range(tempo_total, 0, -1):
        # divmod é usado para converter o tempo total em minutos e segundos, facilitando a formatação da saída
        minutos, segundos = divmod(segundos_restantes, 60)
        tempo_formatado = f'{minutos:02d}:{segundos:02d}'
        # end="\r" é usada para reescrever a linha atual no terminal
        print(f'{Fore.GREEN}Finalizando a execução em {Style.RESET_ALL}{tempo_formatado}', end="\r")
        sleep(1)


# Limpar a tela

def limpa_tela():
    sleep(3)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# JUDGE

def gerar_comandos_judge(caixa_cadastro, caixa_arquivo_rem, nomenclatura_arquivo, contadores_utilizados):
    lista_arquivos = nomenclatura_arquivo.split(" ")

    comandos = list()

    # Gerando contador
    for i in range(len(lista_arquivos)):
        contador = random.randint(11111, 99999)

        # Verificando se contador ja existe
        while contador in contadores_utilizados:
            print(f'{Fore.YELLOW}[ALERTA]{Style.RESET_ALL} O {contador} ja existe, gerando um novo contador...')
            contador = random.randint(11111, 99999)

        # Gerando Script
        comando = f'$JUDGE_CMD $JUDGE_CFG {caixa_cadastro} ~/{caixa_arquivo_rem}/mailbox/{lista_arquivos[i]}.{contador}'
        comandos.append(comando)

    return comandos


def dados_judge():
    """
    -> Esta função recebe os dados de entrada e escreve a saida dos scripts na tela.
    return: Sem retorno.
    Criado por João V. Rosa
    """
    contadores_utilizados = list()

    try:
        print("\n---------------------------- DADOS DE ENTRADA ----------------------------")
        caixa_cadastro = input("Caixa postal cadastro: ")
        caixa_arquivo_rem = input("Caixa arquivo remessa: ")
        nomenclatura_arquivo = input("Nomenclatura arquivo: ")
        print("--------------------------------------------------------------------------")

        comandos_gerados = gerar_comandos_judge(caixa_cadastro, caixa_arquivo_rem, nomenclatura_arquivo, contadores_utilizados)

        print("\n\n\n---------------------------- COMANDOS GERADOS ----------------------------")
        for cmd in comandos_gerados:
            print(cmd)
        print("--------------------------------------------------------------------------\n")

        # Gerando um contador apos a geração dos scripts
        contador_segundo(tempo_total=45)

    except ValueError as erro:
        print(f'{Fore.RED}ERRO: {Style.RESET_ALL}{Style.BRIGHT}{erro}{Style.RESET_ALL}')


# Fluxo RET ou REM

def escolher_fluxo():
    try:
        fluxo = input("> Escolha o fluxo desejado:\n\n[ 1 ] Fluxo de Retorno - var/spool\n[ 2 ] Fluxo de Remessa - JUDGE\n\n> Digite a opcao: ")
        while fluxo != "1" and fluxo != "2":
            print(f'\n{Fore.RED}[ERRO] {Style.RESET_ALL}{Style.BRIGHT}Opcao invalida, tente novamente!{Style.RESET_ALL}')
            limpa_tela()
            fluxo = input("\n> Escolha o fluxo desejado:\n\n[1] Fluxo de Retorno - var/spool\n[2] Fluxo de Remessa - JUDGE\n\n> Digite a opcao: ")
            
    except ValueError as erro:
        print(f'{Fore.RED}ERRO: {Style.RESET_ALL}{Style.BRIGHT}{erro}{Style.RESET_ALL}')

    if fluxo == "1":
        dados_varspool()
    elif fluxo == "2":
        dados_judge()



if __name__ == "__main__":
    escolher_fluxo()
