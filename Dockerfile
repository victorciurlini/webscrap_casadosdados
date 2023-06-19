# Imagem base com o Python 3.10.4
FROM python:3.10.4

# Define as variáveis de ambiente
# ARG AWS_ACCESS_KEY_ID
# ARG AWS_SECRET_ACCESS_KEY
# ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
# ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

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

# Define o comando padrão para executar a aplicação
CMD ["/bin/bash"]
# CMD [ "python", "lambda_function.py" ]
