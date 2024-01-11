FROM python:3.10
RUN apt-get -y update
RUN pip install --upgrade pip
WORKDIR /api-app
COPY . .
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
