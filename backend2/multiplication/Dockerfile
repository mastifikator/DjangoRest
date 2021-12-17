FROM python:3
LABEL maintainer="N1k0"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV HTTP_PROXY="http://bproxy.msk.mts.ru:3128"
ENV HTTPS_PROXY="http://bproxy.msk.mts.ru:3128"
RUN echo 'Acquire::http::Proxy "http://bproxy.msk.mts.ru:3128";' > /etc/apt/apt.conf.d/proxy

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

RUN mkdir /site
COPY . /site
WORKDIR /site

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

#for development
#ENTRYPOINT [ "python", "manage.py"]
#CMD ["runserver", "0.0.0.0:8002"]

CMD ["gunicorn"  , "-b", "0.0.0.0:8002", "multiplication.wsgi:application"]