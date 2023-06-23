import scrapy
import os
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess
import ast
import json
import re
import pandas as pd
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from datetime import datetime

URL_PAGES = []
LISTA_DICT = []

class ScrapyURLs(scrapy.Spider):
    name = "ScrapyURLs"
    # allowed_domains = ["casadosdados.com.br"]
    url= "https://api.casadosdados.com.br/v2/public/cnpj/search"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)",
        # "User-Agent": "Mozilla/5.0 Edg/114.0.1823.37",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
        "Content-Type":"application/json",
    }
    # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37
    urls = []
    url_list = []
    
    def start_requests(self):
        self.log(f"\n\nIniciando a aranha:{self.name}")
        datas = []
        requests = []
        datas = self.create_list_data()
        for data in datas:
            requests.append(scrapy.FormRequest(url=self.url, method="POST",headers = self.HEADERS, body=json.dumps(data), callback=self.parse))
        return requests

    def create_list_data(self):
        query = {
            "termo":[],
            'atividade_principal':['6204000'],
            "natureza_juridica":[],
            "uf":[],
            "municipio":[],
            "situacao_cadastral":"ATIVA",
            "cep":[],
            "ddd":[]
            }
        
        range_query= {
        "data_abertura":{
                        "lte":None,
                        # "gte":datetime.now().strftime('%Y-%m-%d')},
                        "gte":"2023-06-05"},
        }

        datas = []
        for i in range(1, 51):
            datas.append({"query": query, "range_query": range_query, "page": i})
        
        return datas

    def parse(self, response):
        global URL_PAGES
        mydata = ast.literal_eval(response.text.replace(":false", ":False").replace(":true", ":True"))     
        cnpjs, names =  self.return_cnpjs(mydata)
        names = self.name_processing(names)
        self.cnpjs = cnpjs
        self.names = names
        self.log("Lista Criada com sucesso")
        urls = self.create_urls()
        for url in urls:
            self.urls.append(url)
            # URL_PAGES.append(url)
        URL_PAGES.extend(self.urls)

    def return_cnpjs(self, mydata):
        self.log("Lendo todos os CNPJs")
        try:
            list_cadastros = mydata["data"]["cnpj"]
        except Exception as e:
            self.log(f"Erro ao ler os CNPJs:\nmydata: {mydata}\nErro: {e}\n")
            list_cadastros = []
        cnpjs = []
        names = []
        for cadastro in list_cadastros:
            cnpjs.append(cadastro["cnpj"])
            names.append(cadastro["razao_social"])

        return cnpjs, names
    
    def name_processing(self, names):
        names = list(map(str.lower, names))
        names = [re.sub("[^A-Za-z0-9]+", " ", nome) for nome in names]
        names= [re.sub("\s", "-", nome) for nome in names]
        
        return names

    def create_urls(self):
        urls = [f"https://casadosdados.com.br/solucao/cnpj/{nome}-{cnpj}" for nome, cnpj in zip(self.names, self.cnpjs)]

        return urls

class ScrapyInformations(scrapy.Spider):
    name = "ScrapyInformations"
    

    def __init__(self, final_dicts, *args, **kwargs):
        super(ScrapyInformations, self).__init__(*args, **kwargs)
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
        "Content-Type":"text/html"}
        self.dict_infos = {"CNPJ": "NaoConsta",
                "Razão Social": "NaoConsta",
                "Nome Fantasia": "NaoConsta",
                "Tipo": "NaoConsta",
                "Data Abertura": "NaoConsta",
                "Situação Cadastral": "NaoConsta",
                "Data da Situação Cadastral": "NaoConsta",
                "Capital Social": "NaoConsta",
                "Natureza Jurídica": "NaoConsta",
                "Empresa MEI": "NaoConsta",
                "Logradouro": "NaoConsta",
                "Número": "NaoConsta",
                "Complemento": "NaoConsta",
                "CEP": "NaoConsta",
                "Bairro": "NaoConsta",
                "Município": "NaoConsta",
                "UF": "NaoConsta",
                "Telefone": "NaoConsta",
                "E-MAIL": "NaoConsta",
                "Quadro Societário": "NaoConsta"}
        self.final_dicts = final_dicts
    
    def start_requests(self):
        self.log(f"\n\nIniciando a aranha: {self.name}\n\n")
        # datas = []
        # requests = []

        for url in self.start_urls:
            yield scrapy.Request(url=url, method="GET", headers = self.headers, callback=self.parse)

    
    def parse(self, response):
        global LISTA_DICT
        self.log(f"\n\nBuscando dados da empresa: {response.url}\n\n")
        PAGES = '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]'
        PAGE_TEXT = ".//text()"
        PATH_TO_PAGES = response.xpath(PAGES)
        TEXT_FROM_PAGES = []
        [TEXT_FROM_PAGES.append(pages.extract().replace("\n", "").strip()) for pages in PATH_TO_PAGES.xpath(PAGE_TEXT)]
        new_list = self.remove_blank_elements(TEXT_FROM_PAGES)
        
        telefone_concatenate = self.concat_telefones(new_list)
        partners_concatenate = self.concat_partners(telefone_concatenate)
        final_list = self.check_missing_data(partners_concatenate)
        final_dict = self.generate_info_dict(final_list)
        final_list = []
        self.log(f"\n\nDicionário Final: {final_dict}\n\n")
        self.final_dicts.append(final_dict.copy())
        final_dict = self.dict_infos

    def remove_blank_elements(self, list_info):
        new_list = [x for x in list_info if x != ""]
        new_list = [re.sub("[,]+", "", informacoes) for informacoes in new_list]
    
        return new_list

    def concat_telefones(self, new_list):
        telefones = []
        telefone = []
        telefones_idx = []
        concatenate_telefones = new_list
        
        for index, value in enumerate(concatenate_telefones):
            if "Telefone" in value:
                telefone_index = index+1

                for idx, numero in enumerate(concatenate_telefones[telefone_index::]):
                    if numero != "E-MAIL":
                        telefone.append(numero)
                        concatenate_telefones.pop(telefone_index)
                    else:
                        break

                telefones = " ou ". join(telefone)
                concatenate_telefones.insert(telefone_index, telefones)
                
        return concatenate_telefones

    def concat_partners(self, telefone_concatenate):
        concatenate_partners = telefone_concatenate
        people_role = []
        if concatenate_partners[-1] in "Quadro Societário":
            concatenate_partners.append("naoHaSocios")
            
        else:
            for index, value in enumerate(concatenate_partners):
                if "Quadro Societário" in value:
                    partners_index = index+1
                    temp_partners = concatenate_partners[partners_index::]

                    for pessoa, cargo in zip(temp_partners[::2], temp_partners[1::2]):
                        people_role.append(f"{pessoa}")
                        concatenate_partners.pop(partners_index)
                        concatenate_partners.pop(partners_index)

                    partners = " e ". join(people_role)
                    concatenate_partners.insert(partners_index, partners)
        
        return concatenate_partners

    def check_missing_data(self, final_list):
        for index, value in enumerate(final_list):
            if "E-MAIL" in value:
                EMAIL_INDEX = index+1
                if final_list[EMAIL_INDEX] == 'Quadro Societário':
                    final_list.insert(EMAIL_INDEX, "NaoConsta")
            if "Complemento" in value:
                comp_index = index+1
                if final_list[comp_index] == 'CEP':
                    final_list.insert(comp_index, "NaoConsta")

        return final_list

    def generate_info_dict(self, final_list):
        for key, value in self.dict_infos.items():
            for index, infos in enumerate(final_list):
                if key == infos:
                    info = final_list[index+1]
                    self.dict_infos[key] = info

        return self.dict_infos


if __name__ == "__main__":
    URL_PAGES = []
    URL_TEST = ["https://casadosdados.com.br/solucao/cnpj/luana-costa-gomes-47675542000128",
                "https://casadosdados.com.br/solucao/cnpj/a3-data-consultoria-s-a--07105493000173",
                "https://casadosdados.com.br/solucao/cnpj/vr-consultoria-de-sistemas-ltda-14374209000120"]
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