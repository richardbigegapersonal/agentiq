FROM python:3.11

WORKDIR /app

COPY . .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["uvicorn", "api.inference_server:app", "--host", "0.0.0.0", "--port", "8000"]
