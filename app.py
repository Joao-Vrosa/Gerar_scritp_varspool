import random # Gerar números pseudoaleatórios
from colorama import Fore, Style # Inserir cores no terminal


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
            print(f'O {contador} ja existe')
            contador = random.randint(111111111, 999999999)


        # Gerando o script
        comando = f'mv -v {lista_arquivos[i]} /var/spool/nexxera/skyline/recebe/ident/{lista_nomenclatura[i]}.{id_caixa_retorno}.T{contador}.{parametro_conect_vrs}'
        comandos.append(comando)

    return comandos


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
        
    except ValueError as erro:
        print(f'{Fore.RED}ERRO: {Style.RESET_ALL}{Style.BRIGHT}{erro}{Style.RESET_ALL}')


if __name__ == "__main__":
    dados()