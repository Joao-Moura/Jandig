# FROM jandigarte/requirements:latest
FROM python:3.10-slim-bullseye

RUN apt --allow-releaseinfo-change update && \
    apt install -y --no-install-recommends \
    gettext \
    docutils-common \
    curl

RUN mkdir -p /ARte
WORKDIR /ARte
COPY docs/ /ARte/docs/
COPY ./src/ARte /ARte/src/ARte/
COPY ./locale/ /ARte/locale/
COPY ./tasks.py /ARte/tasks.py
COPY ./run.sh /ARte/run.sh
COPY ./etc/ /ARte/etc/
COPY ./pyproject.toml /ARte/pyproject.toml

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
ENV PATH "${PATH}:/root/.poetry/bin"
RUN poetry install

RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
