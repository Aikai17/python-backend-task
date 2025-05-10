FROM python:3.13.3-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

ENV PYTHONPATH=/app
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8080"]
