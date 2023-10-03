FROM python:slim

WORKDIR /app

COPY requirements.txt .
RUN apt install -y gcc
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
