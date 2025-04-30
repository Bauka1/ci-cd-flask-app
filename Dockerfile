FROM python:3.8-slim
# Добавление непривилегированного пользователя
RUN adduser --disabled-password --gecos '' appuser
USER appuser
RUN pip install --upgrade pip && pip install -r requirements.txt
