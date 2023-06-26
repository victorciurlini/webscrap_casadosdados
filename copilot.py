def connect_mariadb():
    try:
        print("Conectando no banco de dados:")
        conn = pymysql.connect(host=RDS_HOST, user=USERNAME, password=PASSWORD, db=DB_NAME, connect_timeout=5)
        print("Conectado com sucesso")
        return conn
    except Exception as e:
        return {
        'statusCode': 402,
        'body': f'Erro na ingestão de dados: {e}'
        }

def read_csv_from_s3(source_bucket, source_key):
    try:
        s3_client = boto3.client('s3')
        obj = s3_client.get_object(Bucket=source_bucket, Key=source_key)
        data = obj['Body'].read().decode('utf-8')
        header = data.split('\n')[0]
        data = data.split('\n')[1:]
        return header, data
    except Exception as e:
        return {
        'statusCode': 400,
        'body': f'Erro ao contectar ao buckets3: {e}'
    }