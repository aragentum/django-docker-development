FROM python:3.8

ARG APP_NAME=web
ARG WORKDIR=/usr/src/app
ARG POETRY_VERSION=1.0.8

WORKDIR ${WORKDIR}

# copy sources
COPY ./${APP_NAME} ./${APP_NAME}
COPY manage.py entrypoint.sh poetry.lock pyproject.toml pytest.ini ./

# apply requirements
RUN chmod +x ./entrypoint.sh
RUN pip install "poetry==$POETRY_VERSION"
RUN poetry install

EXPOSE 8000
