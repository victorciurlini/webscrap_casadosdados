import yaml
from datetime import datetime, timedelta
import re
import pandas as pd
import os


def read_yaml(path):
    with open(path) as file:
        cred = yaml.load(file, Loader=yaml.FullLoader)
    
    return cred

def read_file(path):
    with open(path) as f:
        file_return = [line.strip() for line in f.readlines()]
    
    return file_return

def return_datetime():
    dt_today = datetime.now()
    dt_tomorrow = datetime.now() + timedelta(days=1)
    str_date_today = dt_today.strftime("%m-%d-%Y")
    str_date_tomorrow = dt_tomorrow.strftime("%m-%d-%Y")

    return str_date_today, str_date_tomorrow

def remover_espacos_em_branco(df):
    # Aplica a função lambda em cada elemento do DataFrame
    df = df.applymap(lambda x: re.sub(r'\s{2,}', ' ', str(x)))

    return df

def tratar_capital_social(df, coluna):
    new_df = df.copy()
    new_df[coluna] = new_df[coluna].str.replace('R\$', '')  # Remove o símbolo de R$
    new_df[coluna] = new_df[coluna].str.replace('.', '')  # Remove o separador de milhares
    new_df[coluna] = new_df[coluna].str.replace(',', '.')  # Substitui o separador decimal por ponto
    new_df[coluna] = new_df[coluna].astype(float)  # Converte para o tipo floa

    return new_df

def converte_data(df, coluna):
    new_df = df.copy()
    # Trata dados nulos e datas inválidas
    placeholder_date = "01/01/1900"
    new_df[coluna] = new_df[coluna].apply(
        lambda x: placeholder_date if pd.isna(x) or x == "01/01/0001" else x
    )
    new_df[coluna] = pd.to_datetime(new_df[coluna], format='%d/%m/%Y')  # Converte para o tipo data
    new_df[coluna].dt.strftime('%Y-%m-%d %H:%M:%S')
    new_df[coluna] = new_df[coluna].dt.strftime('%Y-%m-%d %H:%M:%S')
    # new_df[coluna] = str(new_df[coluna])

    return new_df

def processa_dados(df):
    df = remover_espacos_em_branco(df)
    df_capital_tratado = tratar_capital_social(df, 'CapitalSocial')
    df_data_abertura = converte_data(df_capital_tratado, 'DataAbertura')
    df_dados_tratados = converte_data(df_data_abertura, 'DataSituacaoCadastral')

    return df_dados_tratados

def cria_df(lista_dict):
    # transforma o dicionário em um dataframe, com separador | e utf-8
    print(lista_dict)
    df = pd.DataFrame(lista_dict)
    column_mapping = {
    'CNPJ': 'CNPJ',
    'Razão Social': 'RazaoSocial',
    'Nome Fantasia': 'NomeFantasia',
    'Tipo': 'Tipo',
    'Data Abertura': 'DataAbertura',
    'Situação Cadastral': 'SituacaoCadastral',
    'Data da Situação Cadastral': 'DataSituacaoCadastral',
    'Capital Social': 'CapitalSocial',
    'Natureza Jurídica': 'NaturezaJuridica',
    'Empresa MEI': 'EmpresaMEI',
    'Logradouro': 'Logradouro',
    'Número': 'Numero',
    'Complemento': 'Complemento',
    'CEP': 'CEP',
    'Bairro': 'Bairro',
    'Município': 'Municipio',
    'UF': 'UF',
    'Telefone': 'Telefone',
    'E-MAIL': 'EMAIL',
    'Quadro Societário': 'QuadroSocietario'
    }
    df.rename(columns=column_mapping, inplace=True)
    df_tratado = processa_dados(df)

    return df_tratado


if __name__ == "__main__":
    cred = read_yaml('config/db_access.yaml')
    print(type(cred))
    print(cred)