# Imagem base com o Python 3.10.4
FROM python:3.10.4

# Define o diretório de trabalho
WORKDIR /app

# Instala as dependências do sistema
RUN apt-get update && apt-get install -y libc6-dev

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Atualiza o pip para a versão mais recente
RUN pip install --no-cache-dir --upgrade pip

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos e pastas para dentro da imagem
COPY dados/ /app/dados/
COPY logger/ /app/logger/
COPY modulos/ /app/modulos/
COPY config/ /app/config/
COPY lambda_function.py /app/

# Altera as permissões do diretório de destino
# RUN chmod 777 /app/dados/
# Define o usuário padrão como root
USER root


# Define o comando padrão para executar a aplicação
# CMD ["/bin/bash"]
CMD [ "python", "lambda_function.py" ]
