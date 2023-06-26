# import csv
# import boto3
# import mysql.connector

# class ETLProcess:
#     def __init__(self, s3_temp_bucket, s3_database_bucket, db_host, db_user, db_password, db_name, table_name):
#         self.s3_temp_bucket = s3_temp_bucket
#         self.s3_database_bucket = s3_database_bucket
#         self.db_host = db_host
#         self.db_user = db_user
#         self.db_password = db_password
#         self.db_name = db_name
#         self.table_name = table_name

#     def read_csv_from_s3(self, s3_bucket, s3_key):
#         s3_client = boto3.client('s3')
#         response = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
#         csv_content = response['Body'].read().decode('utf-8')
#         csv_data = csv.reader(csv_content.splitlines(), delimiter=',')
#         header = next(csv_data)  # Obter o cabeçalho das colunas do CSV
#         data = list(csv_data)  # Obter os dados do CSV como uma lista
#         return header, data

#     def create_table(self):
#         connection = mysql.connector.connect(
#             host=self.db_host,
#             user=self.db_user,
#             password=self.db_password,
#             database=self.db_name
#         )
#         print("Conectado ao banco de dados")
#         cursor = connection.cursor()
#         # Ler o conteúdo do arquivo de caminho: dados/dll_flat_table.sql
#         print("Criando tabela")
#         with open('dados/dll_flat_table.sql', 'r') as file:
#             create_table_query = file.read()

#         cursor.execute(create_table_query)
#         connection.commit()
#         cursor.close()
#         connection.close()

#     def insert_into_table(self, data):
#         connection = mysql.connector.connect(
#             host=self.db_host,
#             user=self.db_user,
#             password=self.db_password,
#             database=self.db_name
#         )
#         cursor = connection.cursor()
#         # Construir a declaração SQL para inserir os dados na tabela
#         insert_query = f"INSERT INTO {self.table_name} VALUES ({', '.join(['%s'] * len(data[0]))});"
#         cursor.executemany(insert_query, data)
#         connection.commit()
#         cursor.close()
#         connection.close()

#     def move_csv_to_database_bucket(self, s3_temp_key, s3_database_bucket):
#         s3_client = boto3.client('s3')
#         s3_client.copy_object(
#             Bucket=s3_database_bucket,
#             CopySource={'Bucket': self.s3_temp_bucket, 'Key': s3_temp_key},
#             Key=s3_temp_key
#         )
#         s3_client.delete_object(Bucket=self.s3_temp_bucket, Key=s3_temp_key)

#     def perform_etl(self):
#         s3_client = boto3.client('s3')
#         response = s3_client.list_objects_v2(Bucket=self.s3_temp_bucket)
#         if 'Contents' in response:
#             # Encontrou objetos no bucket temporário
#             for obj in response['Contents']:
#                 s3_temp_key = obj['Key']
#                 print(f"Lendo arquivo CSV: {s3_temp_key}")
#                 header, data = self.read_csv_from_s3(self.s3_temp_bucket, s3_temp_key)
#                 print(f"Criando tabela {self.table_name}")
#                 self.create_table()
#                 print(f"Inserindo dados na tabela {self.table_name}")
#                 self.insert_into_table(data)
#                 print(f"Movendo arquivo CSV para o bucket de banco de dados")
#                 self.move_csv_to_database_bucket(s3_temp_key, self.s3_database_bucket)
#                 print(f"ETL concluído para o arquivo CSV: {s3_temp_key}")
#         else:
#             print("Nenhum arquivo CSV encontrado no bucket temporário.")


# if __name__ == '__main__':
#     s3_temp_bucket = "casadosdadostemp"
#     s3_database_bucket = "bucketdatabasecasadosdados"
#     db_host = "casadosdados.cdu4kjqn6wpb.us-east-1.rds.amazonaws.com"
#     db_user = "admin"
#     db_password = "Casa2406!"
#     db_name = "dev"
#     table_name = "dev.flat_table"
#     vpc = "vpc-0237be23a12cfea4c"
#     subnet_group = "default-vpc-0237be23a12cfea4c"
#     subnets = ["subnet-0b81a4918f515ca12",
#             "subnet-051effe0937109b2f",
#             "subnet-02638fc4a4ca900c6",
#             "subnet-0481ceb60e808a19a",
#             "subnet-08296e86192de20c9",
#             "subnet-07a7d404747e1f52e"]

#     etl_process = ETLProcess(s3_temp_bucket, s3_database_bucket, db_host, db_user, db_password, db_name, table_name)
#     etl_process.perform_etl()
