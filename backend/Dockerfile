# Montando wheels das dependências 
FROM python:3.12-slim AS build-stage

COPY requirements.txt requirements.txt

# Dependencias necessárias para o processo de build da
# lib "mariadb"
RUN apt-get update && \
    apt-get install --no-install-recommends gcc libmariadb-dev -y

RUN pip wheel --no-cache-dir --no-deps --wheel-dir wheels -r requirements.txt

FROM python:3.12-slim AS production-stage

# Removendo apt/lists para diminuir o tamanho final da imagem
RUN apt-get update && \
    apt-get install --no-install-recommends libmariadb3 -y && \
    rm -rf /var/lib/apt/lists/*

COPY --from=build-stage /wheels /wheels
RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels

COPY /app /app

EXPOSE 8000

CMD [ "uvicorn", \
      "--factory", "app.main:create_app", \
      "--host", "0.0.0.0", \
      "--port", "8000" \
]