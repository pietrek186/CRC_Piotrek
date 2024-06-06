FROM python:3.12
WORKDIR /app
# Kopiowanie zawartości bieżącego katalogu do katalogu roboczego w kontenerze
COPY . .
# Instalacja zależności bezpośrednio w Dockerfile
RUN pip install --no-cache-dir sqlalchemy psycopg2-binary fastapi uvicorn
# Uruchomienie aplikacji za pomocą Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]