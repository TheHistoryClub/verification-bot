FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN apt update && apt install -y gcc && apt full-upgrade
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
