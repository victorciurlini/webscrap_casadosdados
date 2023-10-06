import boto3
import pandas as pd
from datetime import datetime
import sys
import logging
from modulos.funcoes_aux import *

def ingest_dataframe_to_s3(dataframe, bucket_name, s3_key):
    # Converte o DataFrame em uma string no formato CSV com separador "|" e codificação UTF-8
    csv_data = dataframe.to_csv(index=False, sep='|', encoding='utf-8')
    
    # Cria uma instância do cliente S3
    s3_client = boto3.client('s3')

    try:
        # Faz o upload do CSV para o bucket S3
        response = s3_client.put_object(Body=csv_data, Bucket=bucket_name, Key=s3_key)
        print(f"Arquivo CSV ingerido com sucesso no bucket S3: {response}")
        return {
            'statusCode': 200,
            'body': f'Pipeline executada com sucesso'
            }

    except Exception as e:
        print("Falha ao realizar a ingestão do arquivo CSV:", e)
        return {
        'statusCode': 400,
        'body': f'Falha ao realizar a ingestão do arquivo CSV: {e}'
        }

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

