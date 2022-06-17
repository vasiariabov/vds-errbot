FROM ubuntu:20.04
LABEL Vasiliy Ryabov <vasiliy.ryabov@happytravel.tech>

ARG VDS_TOKEN
ARG TELEGRAM_ID
ARG TELEGRAM_TOKEN

ENV VDS_TOKEN=$VDS_TOKEN
ENV TELEGRAM_ID=$TELEGRAM_ID
ENV TELEGRAM_TOKEN=$TELEGRAM_TOKEN


COPY requirements.txt /err/
WORKDIR /err/
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install -r /err/requirements.txt 
RUN errbot --init

COPY config.py /err/
COPY vdsworker.py /err/plugins/err-example
COPY vdsworker.plug /err/plugins/err-example

#CMD ["errbot"] 
CMD ["/bin/bash"] 