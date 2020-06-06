FROM python:3.7

ARG APP_NAME=web
ARG WORKDIR=/usr/src/app
ARG REQUIREMENTS=requirements/development.txt

WORKDIR ${WORKDIR}

# copy sources
COPY ./${APP_NAME} ./${APP_NAME}
COPY manage.py entrypoint.sh ./

# apply requirements
COPY ${REQUIREMENTS} ./requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000
