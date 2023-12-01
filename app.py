import random # Gerar números pseudoaleatórios
from colorama import Fore, Style # Inserir cores no terminal
from time import sleep


def gerar_comandos(arquivo_quarentena, nomenclatura_retorno, id_caixa_retorno, parametro_conect_vrs):
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

    for i in range(len(lista_arquivos)):
        contador = random.randint(111111111, 999999999)
        
        # Verificando se o contador ja existe
        while contador in comandos:
            print(f'[*] O {contador} ja existe, gerando um novo contador...')
            contador = random.randint(111111111, 999999999)


        # Gerando o script
        comando = f'mv -v {lista_arquivos[i]} /var/spool/nexxera/skyline/recebe/ident/{lista_nomenclatura[i]}.{id_caixa_retorno}.T{contador}.{parametro_conect_vrs}'
        comandos.append(comando)

    return comandos


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
        print(f'{Fore.GREEN}Tempo restante: {Style.RESET_ALL}{tempo_formatado}', end="\r")
        sleep(1)


def dados():
    """
    -> Esta função recebe os dados de entrada e escreve a saida dos scripts na tela.
    return: Sem retorno.
    Criado por João V. Rosa
    """
    try:
        print("\n---------------------------- DADOS DE ENTRADA ----------------------------")
        arquivo_quarentena = input("Nome do arquivo: ")
        nomenclatura_retorno = input("DSNAME de retorno: ")
        id_caixa_retorno = int(input("ID cliente: "))
        parametro_conect_vrs = input("Parâmetro Connect/RVS: ")
        print("--------------------------------------------------------------------------")

        comandos_gerados = gerar_comandos(arquivo_quarentena, nomenclatura_retorno, id_caixa_retorno, parametro_conect_vrs)

        print("\n\n\n---------------------------- COMANDOS GERADOS ----------------------------")
        for cmd in comandos_gerados:
            print(cmd)
        print("--------------------------------------------------------------------------")
        
        # Gerando um contador apos a geração dos scripts
        contador_segundo(tempo_total=40)
        
    except ValueError as erro:
        print(f'{Fore.RED}ERRO: {Style.RESET_ALL}{Style.BRIGHT}{erro}{Style.RESET_ALL}')


if __name__ == "__main__":
    dados()
