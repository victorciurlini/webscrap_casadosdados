Contextualização e relevância do tema

Qual a importância da coleta e ingestão de dados em nuvem, particularmente no contexto da análise de mercado e tomada de decisão orientada por dados?
Por que a extração de dados cadastrais de CNPJs é importante?
Como essas informações podem ser úteis para organizações?
2. Problema de pesquisa

Qual é o problema específico que você está abordando com a sua arquitetura de solução em nuvem?
Isso pode ser um problema que você identificou na literatura existente, ou uma necessidade que você percebeu no campo.
3. Objetivo do trabalho

Qual é o objetivo principal do seu projeto?
Em outras palavras, o que você espera conseguir com o desenvolvimento e implementação desta arquitetura de solução em nuvem?
4. Metodologia

Uma breve descrição das técnicas e ferramentas que você planeja usar no seu projeto (neste caso, AWS, Python, Docker, DevOps, Git, S3, RDS MySQL e PowerBI). Detalhes mais profundos sobre como essas tecnologias foram usadas serão discutidos mais adiante em sua monografia.
5. Estrutura do trabalho

Um breve resumo dos capítulos subsequentes do seu trabalho para que os leitores saibam o que esperar.



## 1. Contextualização e relevância do tema

Suponha que você está escrevendo a monografia para defender o título de uma pós graduação em uma universidade federal brasileira.
O tema que será desenvolvido é a extração de dados cadastrais de CNPJs brasileiros, utilizando uma arquitetura de solução em nuvem.
Abaixo, você encontra um exemplo de como foi escrita a introdução do seu trabalho.
Nos próximos passos eu irei fornecer as informações que já desenvolvemos juntos, você deverá esperar até que eu diga que finalizei
de apresentar as informações para você para realmente começar a escrever. Até que isso aconteça, você responderá com a frase "ok"
e eu direi a frase "terminei de apresentar os dados" para informar que podemos começar a conversa.
Confirme essa solicitação com um OK.
Irei apresentar tudo o que foi desenvolvido e juntos desenvolvermos os próximos capítulos dessa monografia.

## Introdução:
    A importância dos dados e sua análise nas organizações é um tema de crescente interesse na pesquisa acadêmica e prática empresarial. A era do Big Data, onde bilhões de dados são gerados e coletados diariamente, tem incentivado empresas a investirem em tecnologias e práticas analíticas para converter esses dados em insights acionáveis, que possam auxiliar na tomada de decisões estratégicas \cite{mayer2013big}.

    Especificamente, no cenário de empresas que atuam no segmento B2B (Business to Business), a extração de dados cadastrais de CNPJs pode proporcionar uma visão abrangente do mercado, possibilitando a identificação de tendências e oportunidades \cite{russom2011big}. Com essas informações organizadas e disponíveis, tais empresas podem direcionar seus serviços de maneira mais eficaz, desenvolvendo estratégias baseadas em dados concretos e atualizados, contribuindo para o sucesso de seus negócios \cite{chen2012business}.

    Entretanto, para transformar esses dados brutos em informações úteis, é necessária uma série de operações complexas, muitas vezes resumidas no processo de Extração, Transformação e Carga (ETL). Este processo envolve a coleta de dados de várias fontes, a transformação desses dados para um formato adequado para análise, e, finalmente, a ingestão dos dados transformados em um sistema de destino para fácil acesso e análise \cite{vassiliadis2002conceptual}.

    Com o advento da computação em nuvem, as organizações têm à sua disposição uma infraestrutura flexível, escalável e eficiente para a coleta, processamento e armazenamento de grandes volumes de dados \cite{mell2011nist}. A arquitetura de solução em nuvem é caracterizada pela sua natureza on-demand, o que permite às empresas reduzirem significativamente os custos operacionais e de infraestrutura. Além disso, o tempo para obtenção de insights a partir dos dados é consideravelmente acelerado \cite{armbrust2010view}.

    Nesse contexto, este trabalho apresenta o desenvolvimento de uma arquitetura de solução em nuvem para a coleta e ingestão de dados cadastrais de CNPJs brasileiros. A escolha da arquitetura em nuvem para este projeto se baseia na necessidade de uma solução com baixo custo, alta eficiência e praticidade, capaz de lidar com grandes volumes de dados e proporcionar uma visão analítica para tomada de decisões estratégicas mais eficazes.

## Resumo:
    ETL (extract transform and load)  ́e uma t ́ecnica amplamente utilizada na  ́area de
    dados, visando unificar diversas fontes de informac ̧  ̃oes e dados em um local, de forma
    organizada e perform ́atica para tomada de decis ̃oes orientadas a dados. Este processo
    permite a criac ̧  ̃ao de pain ́eis e treinamento de modelos de aprendizado de m ́aquina em
    empresas que buscam otimizar a tomada de decis ̃oes, usando essas tecnologias para em-
    basamento nessas decis ̃oes. Para a construc ̧  ̃ao dessa soluc ̧  ̃ao,  ́e necess ́ario considerar a
    linguagem escolhida para o seu desenvolvimento, quais tecnologias ser ̃ao utilizadas para
    sustentar esse servic ̧o e como ser ́a realizada a disponibilizac ̧  ̃ao desses dados para con-
    sumo dos analistas e respons ́aveis pela tomada de decis ̃ao. Esta monografia apresenta
    o desenvolvimento de uma arquitetura de soluc ̧  ̃ao em nuvem para coleta e ingest ̃ao dos
    dados em um banco de dados relacional de dados cadastrais de CNPJs brasileiros. Esses
    dados s ̃ao utilizados para construc ̧  ̃ao de pain ́eis e dashboards, utilizados para a tomada
    de decis ̃oes estrat ́egicas orientadas a dados. O Documento abordar ́a a contextualizac ̧  ̃ao
    do problema, descrevendo qual  ́e necessidade atendida pela soluc ̧  ̃ao, apresentac ̧  ̃ao de
    uma soluc ̧  ̃ao, descric ̧  ̃ao das tecnologias utilizadas, descric ̧  ̃ao da implantac ̧  ̃ao da soluc ̧  ̃ao e
    apresentac ̧  ̃ao dos resultados obtidos.
    Palavras-chave: AWS; Python; Docker; DevOps; Ingest ̃ao de Dados; An ́alise de
    Dados; Tomada de Decis ̃ao Baseada em Dados; CNPJ.

## Contextualização:
    A importância dos dados e sua análise nas organizações é um tema de crescente interesse na pesquisa acadêmica e prática empresarial. A era do Big Data, onde bilhões de dados são gerados e coletados diariamente, tem incentivado empresas a investirem em tecnologias e práticas analíticas para converter esses dados em insights acionáveis, que possam auxiliar na tomada de decisões estratégicas \cite{mayer2013big}.
    Especificamente, no cenário de empresas que atuam no segmento B2B (Business to Business), a extração de dados cadastrais de CNPJs pode proporcionar uma visão abrangente do mercado, possibilitando a identificação de tendências e oportunidades \cite{russom2011big}. Com essas informações organizadas e disponíveis, tais empresas podem direcionar seus serviços de maneira mais eficaz, desenvolvendo estratégias baseadas em dados concretos e atualizados, contribuindo para o sucesso de seus negócios \cite{chen2012business}.
    Entretanto, para transformar esses dados brutos em informações úteis, é necessária uma série de operações complexas, muitas vezes resumidas no processo de Extração, Transformação e Carga (ETL). Este processo envolve a coleta de dados de várias fontes, a transformação desses dados para um formato adequado para análise, e, finalmente, a ingestão dos dados transformados em um sistema de destino para fácil acesso e análise \cite{vassiliadis2002conceptual}.
    Com o advento da computação em nuvem, as organizações têm à sua disposição uma infraestrutura flexível, escalável e eficiente para a coleta, processamento e armazenamento de grandes volumes de dados \cite{mell2011nist}. A arquitetura de solução em nuvem é caracterizada pela sua natureza on-demand, o que permite às empresas reduzirem significativamente os custos operacionais e de infraestrutura. Além disso, o tempo para obtenção de insights a partir dos dados é consideravelmente acelerado \cite{armbrust2010view}.
    Nesse contexto, este trabalho apresenta o desenvolvimento de uma arquitetura de solução em nuvem para a coleta e ingestão de dados cadastrais de CNPJs brasileiros. A escolha da arquitetura em nuvem para este projeto se baseia na necessidade de uma solução com baixo custo, alta eficiência e praticidade, capaz de lidar com grandes volumes de dados e proporcionar uma visão analítica para tomada de decisões estratégicas mais eficazes.


    Sendo este uma monografia, é necessário que toda a informação tenha embasamento teórico/científico, então certifique-se de utilizar
    as referências bibliográficas adequadas para cada informação que você apresentar.


    Contexto e Empresa:
        Qual é a natureza do negócio da empresa?
        Qual é o seu tamanho e localização?
        Qual é o contexto em que a empresa está inserida?
        Como a empresa gerencia seus dados atualmente?

    A empresa em questão é uma provedora de internet, que atua no mercado B2B (Business to Business), ou seja, atende outras empresas.
    A empresa possui cerca de 100 funcionários, e está localizada na cidade de São Paulo. Atualmente a empresa utiliza as informações
    do site da Receita Federal para obter os dados cadastrais dos CNPJs que são abertos no Brasil. Essa informação é utilizada para que
    o time de prospecção do cliente possa realizar o primeiro contato, o mais rápido possível para oferecer os serviços da empresa. Atualmente,
    os dados dessa empresa são disponibilizados em um servidor onpremisse, onde um time realiza a extração dos dados do site da receita federal
    e disponibiliza em um arquivo excel, que é compartilhado com os times de prospecção do cliente e análise de dados através desse servidor.
    Boa parte desse processo exige a atuação humana, o que torna o processo lento e suscetível a erros. As construções dos paineis do time
    de análise também se baseiam nesses arquivos Excels, então por muitas vezes quando ocorre a atualização erronea desse arquivo, os painéis
    tendem a apresentar informações incorretas, ou até mesmo apresentar erro na própria ferramenta. Além disso, a informação não é estruturada
    da maneira correta, o que dificulta a análise dos dados e a tomada de decisão. Por fim, a informação não é atualizada com tempo hábil para
    prospecção do cliente, dando uma desvantagem competitiva para a empresa.


    Problema e Motivação:
        Qual é a situação atual que você deseja abordar em seu estudo de caso?
        Como os dados cadastrais dos CNPJs são utilizados atualmente na empresa?
        Existem problemas ou limitações que este trabalho visa resolver?

    Atualmente, essa forma de compartilhamento de dados dentro da empresa não é a mais eficiente, pois a informação não é atualizada
    com tempo hábil para prospecção do cliente e a inconsistência da informação prejudicam a análise de mercado para tomada de decisões,
    resultando em uma desvantagem competitiva para a empresa. Por fim, a informação não é estruturada, dificultando a análise dos dados
    e a tomada de decisão. Portanto, este trabalho visa resolver esses problemas, através da construção de uma arquitetura de solução em nuvem
    que busca automatizar a extração dos dados e a disponibilização da informação, para que o time de prospecção possa atuar com mais
    eficiência e o time de análise de dados possuam uma fonte de dados de forma mais consistente, estruturada e atualizada, para que possam
    realizar a análise de mercado e a tomada de decisão estratégica de forma mais eficaz.

    Objetivos do Estudo de Caso:
        O que você deseja alcançar com a implementação da arquitetura de solução em nuvem?
        Como essa solução vai melhorar a situação atual?

    Ao fim do projeto, é esperado que a empresa possa ter acesso a informação de forma rápida e estruturada, disponibilizando as informações
    necessárias para que o time de prospecção possa realizar o primeiro contato com o cliente, ganhando vantagem estratégica no mercado pela
    velocidade de atuação. Espera-se também que essa arquitetura forneça os dados de maneira mais consistente, estruturada e atualizada para
    que o time de análise de dados possa realizar a análise de mercado, e a tomada de decisão estratégica de forma mais eficaz. Espera-se que
    a arquitetura esteja desenhada de forma a ser escalável, para que possa atender a demanda de crescimento da empresa, sem a necessidade de
    alteração da solução. Essa solução deverá ter seu custo o menor possível comparado a solução atual da empresa, permitindo a flexibilidade
    de crescimento da empresa sem a necessidade de investimento em infraestrutura.


    As plataformas em nuvem fornecem uma infraestrutura flexível, escalável e eficiente para a coleta, processamento e armazenamento de dados.
    A arquitetura de solução em nuvem é caracterizada pela sua natureza on-demand, o que permite às empresas reduzirem significativamente os
    custos operacionais e de infraestrutura. Portanto, a implementação de uma arquitetura de solução em nuvem para a coleta e ingestão de dados
    cadastrais de CNPJs brasileiros tornará possível realizar todo o processo de ETL de forma automatizada, com baixo custo, alta eficiência
    e praticidade, o armazenamento em um banco de dados estruturados permitirá a construção de painéis e dashboards de forma mais consistente para
    a tomada de decisões estratégicas. A trasmissão da informação entre os times permitirá que a informação seja atualizada com tempo hábil
    para prospecção do cliente, dando uma vantagem competitiva para a empresa.



    Proposta de Solução:
        Quais são as tecnologias e ferramentas que você propõe para implementar a solução em nuvem?
        Por que você escolheu essas tecnologias e como elas serão utilizadas na solução?


    A escolha da arquitetura em nuvem para este projeto se baseia na necessidade de uma solução com baixo custo, alta eficiência. 
    Foi escolhido o AWS como provedor de nuvem, pelo seu custo reduzido comparado a um serviço on-premisse e levando em consideração
    aos custos de outros provedores de nuvem, como Azure. A familiaridade com a plataforma também influênciou na decisão, pois a equipe
    de desenvolvimento já possui conhecimento prévio da plataforma. Para a coleta dos dados, foi escolhido o Python, por ser uma linguagem
    de programação de alto nível e de fácil aprendizado, além de possuir uma grande comunidade de desenvolvedores e uma grande quantidade de
    bibliotecas para manipulação de dados. Para o armazenamento dos dados, foi escolhido o RDS MySQL, por ser um banco de dados relacional,
    que permite a estruturação dos dados, facilitando a análise dos dados e a tomada de decisão.
    Para a construção dos painéis e dashboards, foi escolhido o PowerBI, por ser uma ferramenta já utilizada na empresa. Como repositório
    de backup dos dados extraidos, foi escolhido o S3, por ser um serviço de armazenamento de objetos, que permite o armazenamento de grandes
    volumes de dados, com alta disponibilidade e durabilidade. Para a produtização da solução desenvolvida em python, foi escolhido o Docker,
    permitindo o versionamento da solução e o enclausuramento das dependências, facilitando a implantação da solução em qualquer ambiente.
    Aplicando as melhores práticas de DevOps, os códigos serão versionados em um repositório do GITHUB, permitindo o versionamento e a colaboração
    entre os desenvolvedores. Bem como a melhor gestão do projeto como um todo, seguindo a metodologia gitflow para o desenvolvimento do projeto.
    Foi usado a ferramenta da AWS LAMBDA para a execução do código python, pois a ferramenta permite a execução de um container, gerado a partir 
    de uma imagem Docker do projeto, bem como um código em python inserido diretamente na ferramenta. O lambda também opera sem a necessidade de um servidor, e a cobrança é feita por tempo de execução, 
    o que reduz os custos de infraestrutura. Para a orquestração da solução, foi usado o cloudwatch, que permite a execução de um código python
    em um intervalo de tempo pré-definido. Para a extração dos dados, foi usado o site da receita federal, que possui uma API para extração dos
    dados cadastrais de CNPJs brasileiros. Para a ingestão dos dados, foi usado o RDS MySQL, que permite a estruturação dos dados.
    Em suma, as tecnologias utilizadas foram: AWS, Python, Docker, DevOps, Git, S3, RDS MySQL e PowerBI.



    Melhores práticas:
        Quais são as melhores práticas no campo de ETL e análise de dados que podem ser aplicadas ao seu estudo de caso?
        Como essas práticas podem melhorar a eficiência e eficácia da solução proposta?

    As melhores práticas no campo de ETL e análise de dados que podem ser aplicadas ao estudo de caso são: a utilização de uma linguagem de
    programação de alto nível, com uma sintaxe simples e de fácil aprendizado, a utilização de um banco de dados relacional, que permite a
    estruturação dos dados, facilitando a análise dos dados e a tomada de decisão, a utilização de uma ferramenta de fácil utilização e já
    utilizada na empresa, a utilização de um serviço de armazenamento de objetos, que permite o armazenamento de grandes volumes de dados, com
    alta disponibilidade e durabilidade, a utilização de uma ferramenta para a produtização da solução desenvolvida em python, permitindo o
    versionamento da solução e o enclausuramento das dependências, facilitando a implantação da solução em qualquer ambiente, a utilização de
    uma ferramenta para a orquestração da solução, que permite a execução de um código python em um intervalo de tempo pré-definido. Isso tudo
    constroi um ambiente totalmente automatizado, alheio a interferência humana, que reduz os custos operacionais e de infraestrutura, facilitando
    a manutenção do ambiente e a escalabilidade da solução. Além disso, o tempo para obtenção de insights a partir dos dados é consideravelmente
    acelerado, o que permite a tomada de decisões estratégicas mais eficazes, bem como ganhar a vantagem estratégica no mercado pela velocidade
    de prospecção do cliente.

    Desenvolvimento do Estudo de Caso:
        Como será o desenvolvimento da solução em nuvem?

    Escolhida as ferramentas a serem utilizadas no projeto, é necessário agora a arquitetura da solução e como será construído
    cada um dos módulos do projeto. Após definido a arquitetura da solução e definido as entradas e saídas esperadas de cada uma das
    etapas, é necessário identificar os possíveis impedimentos e desafios que podem ser encontrados durante o desenvolvimento individual
    das etapas. Após identificado os desafios, é necessário mapear as soluções possíveis e o plano de ação para a execução da resolução
    desses impedimentos.

    Com o a arquitetura de solução e o mapeamento dos desafios, é possível iniciar o desenvolvimento da solução. Para o desenvolvimento
    da solução, é necessário seguir as melhores práticas de DevOps, que consiste em um conjunto de práticas e ferramentas que visam a
    melhor gestão do projeto, realizando o versionamento do código e a clareza no repositório como um todo, utilizando a Metodologia Gitflow.
    Seguindo essa metodologia, o desenvolvimento do projeto é realizado utilizando um sistema de ramificações de código, tornando mais claro 
    o que está sendo desenvolvido individualmente, sem que uma solução interfira em outra, possibilitando o desenvolvimento de várias funções
    e módulos com mais segurança. Ao terminar o desenvolvimento de uma função ou módulo da solução, é realizado a integração do código com a 
    ramificação de desenvolvimento principal, chamada develop. Após essa integração, é realizado um teste do projeto como um todo com a nova
    alteração, para verificar o seu funcionamento. Após a verificação do funcionamento, é realizado o merge da ramificação de desenvolvimento
    com a ramificação principal, chamada master. Após o merge, é realizado o deploy da solução. 



    # Que etapas estão envolvidas?
        Quais são os desafios esperados e como você planeja superá-los?



    # Resultados Esperados:
        Quais são os resultados esperados após a implementação da solução?

    Ao concluído o projeto, espera-se um ambiente totalmente automatizado, em nuvem e alheio a interferência humana. O projeto deverá ter o seu custo
    o menor possível, não ultrapassando o custo da solução atual da empresa, que é a transferência dos arquivos via servidor on-premisse. Espera-se
    que os analistas e time comercial possa ter acesso a informação de forma rápida e estruturada, para que possam atuar na prospecção do cliente
    e na tomada de decisão estratégica. Espera-se que a informação esteja armazenada em um banco de dados relacional, que permita a estruturação
    e organização dos dados, tornando o processo seguro e performático. Os códigos deverão estar versionados em um repositório do GITHUB e seguindo
    a metodologia gitflow, para que o projeto possa ser mantido e atualizado com facilidade. Espera-se que a solução seja desenvolvida de forma 
    abrangente tratando-se de sistemas, para que possa ser implantada em qualquer ambiente, sem a necessidade de instalação de dependências.
    A solução deverá alimentar a base diariamente, com as informações de todos os CNPJs que são abertos diariamente no Brasil para que os times
    de prospecção de clientes possam ter acesso a informação atualizada e com tempo hábil para prospecção do cliente e para o time de análise de dados
    um melhor entendimento sobre o mercado e a concorrência. Espera-se que a solução seja escalável, para que possa atender a demanda de crescimento
    da empresa, sem a necessidade de alteração da solução.


    Como eles serão medidos?
        Quais são as implicações desses resultados para a empresa?


Capítulo 2: Embasamento Teórico
    2.1 Computação em Nuvem
        A computação em nuvem tornou-se um pilar central da tecnologia da informação nos últimos anos. Ela permite que empresas e indivíduos armazenem e gerenciem dados em servidores remotos, proporcionando flexibilidade, escalabilidade e custo-efetividade significativos (Armbrust et al., 2010). Conforme o estudo realizado por Morais et al. (2019), as soluções em nuvem, especialmente aquelas fornecidas por gigantes da tecnologia como a AWS, estão transformando a maneira como as empresas operam, permitindo a elas uma maior capacidade de adaptar-se a demandas variáveis e implementar soluções de TI eficazes.

    2.2 Extração, Transformação e Carregamento de Dados (ETL)
        A Extração, Transformação e Carregamento (ETL) é uma prática crucial em ciência de dados que envolve a obtenção de dados de diversas fontes, transformando-os para adequação aos requisitos de negócios e carregando-os em um sistema de destino para análise (Kimball & Caserta, 2004). De acordo com o trabalho de Carvalho et al. (2021), as técnicas de ETL são particularmente importantes para lidar com grandes volumes de dados, como aqueles que estão envolvidos neste projeto.

    2.3 Mineração de Dados
        A mineração de dados é uma disciplina que se concentra em descobrir padrões e insights significativos em grandes conjuntos de dados. Maimon & Rokach (2010) afirmam que ela se tornou um componente chave da análise de dados moderna, permitindo que as empresas descubram correlações e tendências que podem ser usadas para informar a tomada de decisões estratégicas. O estudo de Lima et al. (2020) também enfatiza a importância da mineração de dados, especialmente quando combinada com técnicas de aprendizado de máquina, para extrair valor de grandes conjuntos de dados.

    2.4 DevOps
        O DevOps é um conjunto de práticas que visa a integração de desenvolvimento de software e operações de TI. Ele promove a comunicação e a colaboração entre essas duas funções, o que leva a ciclos de desenvolvimento mais rápidos e a produtos de maior qualidade (Loukides, 2012). A pesquisa de Oliveira et al. (2018) destaca o valor do DevOps na entrega rápida e eficaz de software e soluções de TI, o que é essencial para a implementação efetiva deste projeto.

    2.5 Aprendizado de Máquina
        O aprendizado de máquina é um subcampo da inteligência artificial que se concentra no desenvolvimento de algoritmos que permitem que os computadores aprendam com e tomem decisões ou previsões com base em dados (Samuel, 1959). O trabalho de Almeida et al. (2019) destaca a utilidade do aprendizado de máquina na análise de grandes conjuntos de dados, particularmente em tarefas como classificação e previsão.


Para este capítilo, será abordada como foi desenvolvida 