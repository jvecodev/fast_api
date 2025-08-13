# ---- Base ----
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.8.3 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

# Instala dependências do sistema (opcional, mas útil)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential && \
    rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN pip install "poetry==${POETRY_VERSION}"

# Copia manifestos primeiro p/ cache eficiente
COPY pyproject.toml poetry.lock* ./

# Instala somente dependências de runtime
RUN poetry install --only main

# Copia o restante do código
COPY . .

# Porta do Uvicorn
EXPOSE 8000

# Comando padrão (modo dev; Compose vai sobrescrever se quiser)
CMD ["poetry", "run", "uvicorn", "fast_api.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
