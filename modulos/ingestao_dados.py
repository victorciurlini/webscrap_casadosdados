import boto3
import pandas as pd
import mariadb
from datetime import datetime
from funcoes_aux import *
import sys
import logging

def ingest_csv_to_s3(file_path, bucket_name, s3_key):
    # Carrega o arquivo CSV em um DataFrame do pandas
    # df = pd.read_csv(file_path)
    
    # Converte o DataFrame em uma string no formato CSV
    # csv_data = df.to_csv(index=False)
    
    # Cria uma instância do cliente S3 da AWS
    try:
        s3_client = boto3.client('s3')
        # Realiza a ingestão do arquivo no bucket S3
        response = s3_client.put_object(Body=file_path, Bucket=bucket_name, Key=s3_key)
        print("Arquivo ingestado com sucesso no S3!")
    except Exception as e:
        print(f"Falha ao realizar a ingestão do arquivo: {e}")

def ingest_dataframe_to_s3(dataframe, bucket_name, s3_key):
    # Converte o DataFrame em uma string no formato CSV com separador "|" e codificação UTF-8
    csv_data = dataframe.to_csv(index=False, sep='|', encoding='utf-8')
    
    # Cria uma instância do cliente S3
    s3_client = boto3.client('s3')

    try:
        # Faz o upload do CSV para o bucket S3
        response = s3_client.put_object(Body=csv_data, Bucket=bucket_name, Key=s3_key)
        print(f"Arquivo CSV ingerido com sucesso no bucket S3: {response}")
    except Exception as e:
        print("Falha ao realizar a ingestão do arquivo CSV:", e)

def ingest_csv_to_mariaDB():
    # conecta mariadb localhost
    conn = mariadb.connect()
    pass

def connect_db(path_db_access):
    logging.info('Conectando ao banco de dados')
    cred = read_yaml(path_db_access)
    try:
        conn = mariadb.connect(
            user=cred['DB']['USER'],
            password=cred['DB']['PSSWRD'],
            host="localhost",
            port=3306,
            database="dev"
        )
        logging.info("Conexão estabelecida")
    except mariadb.Error as e:
        logging.error(f"Falha na conexão: {e}")
        sys.exit(1)

    cur = conn.cursor()

    return conn, cur

def list_files_local(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file))

    return files

if __name__ == '__main__':
    # file_path = 'dados/informacoes_cnpj_sem_cargos.csv'
    # bucket_arn = 'bucketdatabasecasadosdados'
    # timestamp = datetime.now().strftime("%Y%m%d")
    # file_name = f"{timestamp}_informacoes_cnpj_sem_cargos.csv"

    # ingest_csv_to_s3(file_path, bucket_arn, file_name)
    path_db_access = '../config/db_access.yaml'
    print("Iniciando conexão ao banco de dados")
    logging.info("Iniciando conexão ao banco de dados")
    conn, cur = connect_db(path_db_access)
    logging.info("Conexão estabelecida")
    list_of_files = list_files_local('../dados')

    if len(list_of_files) > 0:
        logging.info("Iniciando ingestão de dados")
        for file in list_of_files:
            try:
                df = pd.read_csv(file, sep='|', encoding='utf-8')
                logging.info(f"Leitura de dados do arquivo {file} realizada com sucesso")

            except Exception as e:
                logging.error(f"Falha ao realizar a leitura do arquivo {file}: {e}")
    else:
        logging.error("Nenhum arquivo encontrado")

