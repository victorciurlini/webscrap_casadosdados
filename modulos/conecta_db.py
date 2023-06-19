# import mariadb
# import sys
# import re
# import pandas as pd
# from modulos.funcoes_aux import read_yaml
# import boto3

# def connect_db(LOGGER_OBJ):
#     LOGGER_OBJ.info('Conectando ao banco de dados')
#     cred = read_yaml('config/db_access.yaml')
#     try:
#         conn = mariadb.connect(
#             user=cred['DB']['USER'],
#             password=cred['DB']['PSSWRD'],
#             host="localhost",
#             port=3306,
#             database="ALBION"
#         )
#         LOGGER_OBJ.info("Conexão estabelecida")
#     except mariadb.Error as e:
#         LOGGER_OBJ.error(f"Falha na conexão: {e}")
#         sys.exit(1)

#     cur = conn.cursor()

#     return conn, cur



# def ingest_data(df_ingest, table, conn, cur, LOGGER_OBJ):
#     LOGGER_OBJ.info(f"Realizando ingestão de dados da tabela {table}")
#     cols = "`,`".join([str(i) for i in df_ingest.columns.tolist()])

#     try:
#         values = df_ingest.to_numpy().tolist()
#         placeholders = ",".join(["%s"] * len(df_ingest.columns))
#         sql = f"INSERT INTO {table} (`{cols}`) VALUES ({placeholders})"
#         cur.executemany(sql, values)
#         conn.commit()
#         LOGGER_OBJ.info("Ingestão realizada com sucesso")
#     except Exception as e:
#         LOGGER_OBJ.error(f"Falha ao realizar ingestão de dados: {e}")

# def read_data(table, conn, cur, LOGGER_OBJ):
#     LOGGER_OBJ.info(f"Realizando a leitura de dados da tabela {table}")
#     try:
#         df = pd.read_sql(f"SELECT  * FROM {table}", conn)
#         LOGGER_OBJ.info("Leitura realizada com sucesso")
#     except Exception as e:
#         LOGGER_OBJ.error(f"Falha ao realizar ingestão de dados: {e}")
#     return df

