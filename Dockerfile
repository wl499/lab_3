FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY brovkov_lab_3.py .
CMD ["python", "brovkov_lab_3.py"]