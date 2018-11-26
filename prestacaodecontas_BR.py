# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 15:52:10 2018

@author: Laura Simonsen Leal
"""
# Site para pegar os dados:
# http://www.tse.jus.br/eleicoes/estatisticas/repositorio-de-dados-eleitorais-1/repositorio-de-dados-eleitorais

#%%
import os
os.chdir(r"C:\Users\Laura\Documents\Princeton\Python Training\Politica\Dados\prestacao_de_contas_eleitorais_candidatos_2018")

# editar para o caminho dos dados no seu computador

#%%
import pandas as pd # Para criarmos DataFrames

#%%
# Vamos começar a leitura do nosso arquivo
despesas_contratadas = pd.read_csv(r"despesas_contratadas_candidatos_2018_BR.csv",encoding = "Latin 1",sep=';')

#%%
despesas_contratadas.head(3) # Três primeiras linhas do arquivo
despesas_contratadas.dtypes

#%%
#despesas_contratadas = despesas_contratadas[["ST_TURNO","TP_PRESTACAO_CONTAS","NR_CANDIDATO","NM_CANDIDATO","SG_PARTIDO","CD_TIPO_FORNECEDOR","DS_TIPO_FORNECEDOR","CD_CNAE_FORNECEDOR","DS_CNAE_FORNECEDOR","NR_CPF_CNPJ_FORNECEDOR","NM_FORNECEDOR","NM_FORNECEDOR_RFB","SG_UF_FORNECEDOR","DS_TIPO_DOCUMENTO","VR_DESPESA_CONTRATADA"]]

#%% Reduzindo dados para primeira análise:
despesas_contratadas = despesas_contratadas[["SQ_PRESTADOR_CONTAS","ST_TURNO","NR_CANDIDATO","NM_CANDIDATO","NM_FORNECEDOR","SG_UF_FORNECEDOR","VR_DESPESA_CONTRATADA"]]

#%%
despesas_contratadas.dtypes
despesas_contratadas['VR_DESPESA_CONTRATADA'] = despesas_contratadas['VR_DESPESA_CONTRATADA'].str.replace(',','.').astype('float')


#%%
despesas_contratadas.groupby(["SQ_PRESTADOR_CONTAS","NR_CANDIDATO","ST_TURNO"]).sum()





#%%
#%%
#%% DESPESAS PAGAS (OBS: O LINK ENTRE DESPESAS PAGAS E CONTRATADAS É A COLUNA "SQ_PRESTADOR_CONTAS")

despesas_pagas = pd.read_csv(r"C:\Users\Laura\Documents\Princeton\Python Training\Politica\Dados\prestacao_de_contas_eleitorais_candidatos_2018\despesas_pagas_candidatos_2018_BR.csv",encoding = "Latin 1",sep=';')

#%%
despesas_pagas = despesas_pagas[["SQ_PRESTADOR_CONTAS","ST_TURNO","CD_FONTE_DESPESA","DS_FONTE_DESPESA","VR_PAGTO_DESPESA"]]
despesas_pagas.dtypes
despesas_pagas['VR_PAGTO_DESPESA'] = despesas_pagas['VR_PAGTO_DESPESA'].str.replace(',','.').astype('float')

#%% Comparação entre despesas pagas e contratadas
despesas_pagas.groupby(["SQ_PRESTADOR_CONTAS","ST_TURNO"]).sum()
despesas_contratadas.groupby(["SQ_PRESTADOR_CONTAS","ST_TURNO"]).sum()

