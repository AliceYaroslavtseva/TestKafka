FROM python:3.9

WORKDIR /kafka_example

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY consumer.py ./

CMD [ "python", "./consumer.py" ]
