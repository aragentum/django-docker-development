ARG APP_NAME=web
ARG WORKDIR=/usr/src/app
ARG REQUIREMENTS=${APP_NAME}/requirements/development.txt

FROM python:3.7
ARG APP_NAME
ARG WORKDIR
ARG REQUIREMENTS

WORKDIR ${WORKDIR}

COPY ./${APP_NAME} ./${APP_NAME}
COPY ./manage.py ./
COPY ./entrypoint.sh ./

RUN chmod +x ./entrypoint.sh
RUN pip install -r ${REQUIREMENTS}

EXPOSE 8000
