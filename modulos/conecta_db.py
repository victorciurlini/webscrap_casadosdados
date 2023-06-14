import mariadb
import sys
import re
import pandas as pd
from modulos.funcoes_aux import read_yaml

def connect_db(LOGGER_OBJ):
    LOGGER_OBJ.info('Conectando ao banco de dados')
    cred = read_yaml('config/db_access.yaml')
    try:
        conn = mariadb.connect(
            user=cred['DB']['USER'],
            password=cred['DB']['PSSWRD'],
            host="localhost",
            port=3306,
            database="ALBION"
        )
        LOGGER_OBJ.info("Conexão estabelecida")
    except mariadb.Error as e:
        LOGGER_OBJ.error(f"Falha na conexão: {e}")
        sys.exit(1)

    cur = conn.cursor()

    return conn, cur

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

def ingest_data(df_ingest, table, conn, cur, LOGGER_OBJ):
    LOGGER_OBJ.info(f"Realizando ingestão de dados da tabela {table}")
    cols = "`,`".join([str(i) for i in df_ingest.columns.tolist()])

    try:
        values = df_ingest.to_numpy().tolist()
        placeholders = ",".join(["%s"] * len(df_ingest.columns))
        sql = f"INSERT INTO {table} (`{cols}`) VALUES ({placeholders})"
        cur.executemany(sql, values)
        conn.commit()
        LOGGER_OBJ.info("Ingestão realizada com sucesso")
    except Exception as e:
        LOGGER_OBJ.error(f"Falha ao realizar ingestão de dados: {e}")

def read_data(table, conn, cur, LOGGER_OBJ):
    LOGGER_OBJ.info(f"Realizando a leitura de dados da tabela {table}")
    try:
        df = pd.read_sql(f"SELECT  * FROM {table}", conn)
        LOGGER_OBJ.info("Leitura realizada com sucesso")
    except Exception as e:
        LOGGER_OBJ.error(f"Falha ao realizar ingestão de dados: {e}")
    return df

