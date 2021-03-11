import os
import re

path = os.getcwd() #pega path

PATH_EXEC = f"{path}/execucao" #Caminho onde está o arquivo para execução
PATH_GERADOS = f"{path}/gerados" #Caminho onde os arquivos serão gerados

#VARIAVEL PARA DEFINIR QTD DE LINHA DE CADA ARQUIVO
qtd_linhas_div = 2500

#QTD LINHAS ARQUIVO DE EXECUCAO
qtd_linhas_arq = 0

#INDICE PARA CRIACAO DOS ARQUIVOS
indice_arquivos = 1

#PARA REALIZAR A DIVISÃO POR ARQUIVOS
linha = 0

#PALAVRA PARA QUEBRAR ARQUIVO APÓS linha >= qtd_linhas_div
pal_search = ';'

#PEGANDO NOME DO ARQUIVO
arquivo_exec = ""
for arquivo in os.listdir(PATH_EXEC):
    arquivo_exec = str(arquivo)
    print('Arquivo que será quebrado:::', arquivo_exec)
    nme_arquivo_fim = arquivo_exec.replace('.txt', '')
    #print(nme_arquivo_fim)

if arquivo_exec: #VERIFICA SE HAVIA ARQUIVO NA PASTA
    #ABRINDO ARQUIVO
    ref_arquivo = open(f'{PATH_EXEC}/{arquivo_exec}', 'r')
    for valor in ref_arquivo:
        qtd_linhas_arq += 1 #somando linhas do arquivo
        linha += 1 #somando linhas para fazer o batimento

        #abrindo arquivo novo
        arquivo_novo = open(f'{PATH_GERADOS}/{nme_arquivo_fim}_{indice_arquivos}.txt', 'a')
        arquivo_novo.write(valor)
        
        #para gerar novos arquivos
        if linha >= qtd_linhas_div and re.search(pal_search, valor, re.IGNORECASE):
            indice_arquivos += 1 #aumentar para criar arquivos
            arquivo_novo.close() #fechando arquivo criado acima
            #print(linha)
            linha = 0 #resetando linhas para fazer batimento

    ref_arquivo.close() #fecha arquivo final
    print('Qtd de linhas do arquivo principal:', qtd_linhas_arq)
    print(f'Arquivos separados em média de {qtd_linhas_div} linhas.')
