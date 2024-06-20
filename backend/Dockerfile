FROM python:3.11

WORKDIR /app
COPY . .

ENV VIRTUAL_ENV=/app/.venv_blondies_webpage

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python3.11 -m venv $VIRTUAL_ENV

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt


# Lanzar el Backend - "--env prod" es para lanzarlo a producción - "--backend-only" es para lanzar solo el backend
# "[ -d alembic ] && reflex db migrate" verifica si existe el directorio "alembic" (indicando la presencia de scripts de migración de Alembic).
# Si lo hace, ejecuta el comando reflex db migrate para aplicar cualquier migración de base de datos pendiente.
ENTRYPOINT [ -d alembic ] && reflex db migrate; reflex run --env prod --backend-only

# AL publbicar en "railway", se debe configurar una variable de entorno llamada "PORT" con valor de "8000".
# Esto para definir el puerto a usar

# Colocar un custom domain apuntando con nombre "api" apuntando a un nombre proporcionado por railway