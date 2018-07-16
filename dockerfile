FROM python:2.7


CMD ["/bin/bash"]


RUN mkdir /config
ADD requirements.txt /config
RUN pip install -r /config/requirements.txt

RUN mkdir /src
RUN mkdir /src/ncart
RUN mkdir /src/ncart_app
RUN mkdir /src/users

WORKDIR /src

EXPOSE 8000

