FROM python:3.11-alpine
WORKDIR /app
COPY . /app
RUN pip install flask mysql-connector-python
EXPOSE 8085
CMD ["python", "app.py"]
