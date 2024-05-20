FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y --no-install-recommends git curl wget build-essential librdkafka-dev \
    && python -m pip install --upgrade pip

RUN useradd -ms /bin/bash python && \
    chown -R python:python /var/log

USER python

WORKDIR /home/python/app

ENV PYTHONPATH=${PYTHONPATH}/home/python/app
ENV PATH=${PATH}:/home/python/.local/bin

CMD ["tail", "-f", "/dev/null"]
