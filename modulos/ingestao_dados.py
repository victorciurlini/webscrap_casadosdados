import boto3
import pandas as pd
from datetime import datetime


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
    # Converte o DataFrame em uma string no formato CSV
    csv_data = dataframe.to_csv(index=False)
    
    # Cria uma instância do cliente S3
    s3_client = boto3.client('s3')
    
    try:
        # Faz o upload do CSV para o bucket S3
        response = s3_client.put_object(Body=csv_data, Bucket=bucket_name, Key=s3_key)
        print("Arquivo CSV ingerido com sucesso no bucket S3!")
    except Exception as e:
        print("Falha ao realizar a ingestão do arquivo CSV:", e)

if __name__ == '__main__':
    file_path = 'dados/informacoes_cnpj_sem_cargos.csv'
    bucket_arn = 'bucketdatabasecasadosdados'
    timestamp = datetime.now().strftime("%Y%m%d")
    file_name = f"{timestamp}_informacoes_cnpj_sem_cargos.csv"

    ingest_csv_to_s3(file_path, bucket_arn, file_name)