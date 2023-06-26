import boto3
import csv
import pymysql
import os

def read_csv_from_s3(s3_bucket, s3_key):
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
    csv_content = response['Body'].read().decode('utf-8')
    csv_data = csv.reader(csv_content.splitlines(), delimiter='|')
    header = next(csv_data)  # Obter o cabeçalho das colunas do CSV
    data = list(csv_data)  # Obter os dados do CSV como uma lista
    return header, data

def move_object_between_buckets(source_bucket, destination_bucket, source_key, destination_key):
    s3_client = boto3.client('s3')
    copy_source = {'Bucket': source_bucket, 'Key': source_key}
    s3_client.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=destination_key)
    s3_client.delete_object(Bucket=source_bucket, Key=source_key)

def ingest_data(header, data, table, conn):
    cur = conn.cursor()
    try:
        cols = "`,`".join([str(i) for i in header])  # usando a variável header

        for row in data:  # iterando sobre a variável data
            sql = f"INSERT INTO dev."+table+" (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
            cur.execute(sql, tuple(row))
        conn.commit()
        print("Ingestão realizada com sucesso")
    except Exception as e:
        print(f"Falha ao realizar ingestão de dados: {e}")


def lambda_handler(event, context):
    # Configurações do S3
    source_bucket = 'casadosdadostemp'
    destination_bucket = 'bucketdatabasecasadosdados'

    # Configurações do RDS MySQL
    RDS_HOST = os.environ['RDS_HOST']
    USERNAME = os.environ['USERNAME']
    PASSWORD = os.environ['PASSWORD']
    DB_NAME = os.environ['DB_NAME']
    try:
        print(f"Conectando no bucket s3: {source_bucket}")
        s3_client = boto3.client('s3')
        bucket_list = s3_client.list_objects_v2(Bucket=source_bucket)
        print("Bucket conectado com sucesso")

    except Exception as e:
        return {
        'statusCode': 400,
        'body': f'Erro ao contectar ao buckets3: {e}'
    }
    
    try:
        print("Conectando no banco de dados:")
        conn = pymysql.connect(host=RDS_HOST, user=USERNAME, password=PASSWORD, db=DB_NAME, connect_timeout=5)
        print("Conectado com sucesso")
    
        for obj in bucket_list['Contents']:
            source_key = obj['Key']
            print(f"Lendo arquivo CSV: {source_key}")
            header, data = read_csv_from_s3(source_bucket, source_key)
    
            try:
                ingest_data(header, data, 'flat_table', conn)
    
            except Exception as e:
                # Tratamento de erros (opcional)
                return {
                    'statusCode': 401,
                    'body': f'lista de arquivos: {bucket_list}'
                }
                conn.rollback()
    
            try:
                print(f"Movendo os arquivos para o bucket {destination_bucket}")
                # Mover o arquivo para o bucket de destino
                destination_key = source_key  # Pode ser ajustado conforme necessário
                move_object_between_buckets(source_bucket, destination_bucket, source_key, destination_key)
            
            except Exception as e:
                return {
                    'statusCode': 402,
                    'body': f'Não foi possível mover os arquivos: {e}, {source_key}'
                }
    

        conn.close()
    except Exception as e:
        return {
        'statusCode': 402,
        'body': f'Erro na ingestão de dados: {e}'
        }

    return {
    'statusCode': 200,
    'body': f'Pipeline executada com sucesso'
}