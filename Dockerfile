FROM python:3.10 AS builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt
FROM python:3.10-slim
WORKDIR /code
COPY --from=builder /root/.local /root/.local
COPY ./bot.py .
ENV PATH=/root/.local:$PATH
CMD [ "python", "-u", "./brovkov_lab_3.py" ]