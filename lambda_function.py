import ast
import requests
import json
import re
import pandas as pd
import math
import boto3
import warnings
from modulos.crawlers import URL_PAGES

from time import sleep
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer
from scrapy.utils.project import get_project_settings

from modulos.conecta_db import *
from modulos.funcoes_aux import *
from modulos.crawlers import *
from logger.Logger import etlLogger

warnings.filterwarnings("ignore", category=FutureWarning)


def ingestao_DB():
    ingest = True
    nome_arquivo = 'dados/informacoes_cnpj_sem_cargos.csv'
    df = pd.read_csv(nome_arquivo, sep='|')
    LOGGER_OBJ = etlLogger(project_name='casa_dos_dados')

    conn, cur = connect_db(LOGGER_OBJ)
    df_dados_tratados = processa_dados(df)
    if ingest == True:
        ingest_data(df_dados_tratados, 'dev.flat_table', conn, cur, LOGGER_OBJ)
        ingest = False
    
    else:
        LOGGER_OBJ.info("Não há dados para ingestão")

    cur.close()
    conn.close()
    


if __name__ == "__main__":
    # URL_PAGES = []
    URL_TEST = ["https://casadosdados.com.br/solucao/cnpj/luana-costa-gomes-47675542000128"]
    url_testes = ["https://casadosdados.com.br/solucao/cnpj/a3-data-consultoria-s-a--07105493000173",
                  "https://casadosdados.com.br/solucao/cnpj/vr-consultoria-de-sistemas-ltda-14374209000120",
                  "https://casadosdados.com.br/solucao/cnpj/d-g-a-mitoso-31190635000122",
                  "https://casadosdados.com.br/solucao/cnpj/d-k-de-s-sacramento-eireli-33625143000148",
                  "https://casadosdados.com.br/solucao/cnpj/sonda-procwork-informatica-ltda-08733698001561",
                  "https://casadosdados.com.br/solucao/cnpj/mz-info-solucoes-ltda-18917581000196",
                  "https://casadosdados.com.br/solucao/cnpj/drz-geotecnologia-e-consultoria-ltda-04915134000193",
                  "https://casadosdados.com.br/solucao/cnpj/prisma-assessoria-e-consultoria-de-sistemas-ltda-07105502000126",
                  "https://casadosdados.com.br/solucao/cnpj/martins-tecnologia-ltda-04423827000169",
                  "https://casadosdados.com.br/solucao/cnpj/axxiom-solucoes-tecnologicas-s-a--09182985000198",
                  "https://casadosdados.com.br/solucao/cnpj/conecta-consultoria-e-informatica-ltda-12161075000133",
                  "https://casadosdados.com.br/solucao/cnpj/grupo-mindbr-marketing-inteligencia-e-negocios-digitais-eireli-36224708000173"]
    print("iniciando processo de scrapy")


    # crawler = CrawlerProcess()
    # # crawler.crawl(ScrapyURLs)
    # # print("Fim da primeira aranha")
    # crawler.crawl(ScrapyInformations, start_urls=URL_TEST)
    # crawler.start()
    # print("fim da execução")
    
    configure_logging()
    runner = CrawlerRunner()

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(ScrapyURLs)
        yield runner.crawl(ScrapyInformations, start_urls = URL_PAGES)
        reactor.stop()
    crawl()
    reactor.run()

    # @defer.inlineCallbacks
    # def crawl():
    #     yield runner.crawl(ScrapyURLs)
    #     yield runner.crawl(ScrapyInformations, start_urls=URL_PAGES)  # Passar a lista de URLs como argumento
    #     reactor.stop()

    # crawl()
    # reactor.run()



    