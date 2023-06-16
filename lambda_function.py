from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer

from modulos.conecta_db import *
from modulos.funcoes_aux import *
from modulos.crawlers import *
from modulos.ingestao_dados import *
from modulos.crawlers import URL_PAGES


warnings.filterwarnings("ignore", category=FutureWarning)


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

    configure_logging()
    runner = CrawlerRunner()

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(ScrapyURLs)
        yield runner.crawl(ScrapyInformations, start_urls = URL_PAGES)
        reactor.stop()
    crawl()
    reactor.run()

    file_path = 'dados/informacoes_cnpj_sem_cargos.csv'
    bucket_arn = 'bucketdatabasecasadosdados'
    timestamp = datetime.now().strftime("%Y%m%d")
    file_name = f"{bucket_arn}/{timestamp}_informacoes_cnpj_sem_cargos.csv"

    # ingest_dataframe_to_s3(df_saida, bucket_arn, file_name)
    ingest_csv_to_s3(file_path, bucket_arn, file_name)