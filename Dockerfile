FROM ubuntu:18.04

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update
RUN apt-get install -y fortune fortunes
RUN apt-get install -y cowsay
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt

COPY app.py app.py

ENV PATH=$PATH:/usr/games
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
