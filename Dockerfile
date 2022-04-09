FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt
RUN pip install docker
COPY . /src/

CMD [ "python", "./bot.py" ]