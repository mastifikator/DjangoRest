FROM python:3.9-alpine as builder
LABEL maintainer="N1k0"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HTTP_PROXY="http://bproxy.msk.mts.ru:3128"
ENV HTTPS_PROXY="http://bproxy.msk.mts.ru:3128"
ENV VENV="/venv"
ENV PATH="${VENV}/bin:${PATH}"

RUN apk update \
    && apk add --no-cache make gcc \
    && pip install --upgrade pip \
    && apk add --no-cache bash

COPY requirements.txt .
RUN python -m venv ${VENV} \
    && pip install --no-cache-dir -r requirements.txt \
    && mkdir /site

FROM python:3.9-alpine
ENV VENV="/venv"
ENV PATH="${VENV}/bin:${PATH}"
COPY --from=builder ${VENV} ${VENV}

WORKDIR /site
COPY . .

#for development
#ENTRYPOINT [ "python", "manage.py"]
#CMD ["runserver", "0.0.0.0:8001"]

EXPOSE 8002
CMD ["gunicorn"  , "-b", "0.0.0.0:8002", "multiplication.wsgi:application"]