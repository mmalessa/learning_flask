ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ARG DEVELOPER_NAME=developer
ARG WORKDIR=/app
ENV POETRY_HOME="/home/${DEVELOPER_NAME}/.local/"
ENV PATH="${PATH}:/home/${DEVELOPER_NAME}/.local/bin/"
ENV PYTHONPATH="$WORKDIR:${PYTHONPATH}"

RUN apt update && apt install -y gcc curl git && rm -rf /var/lib/apt/lists/*
RUN python -m pip install --upgrade pip


ARG DEVELOPER_UID
RUN useradd -m -s /bin/bash -u ${DEVELOPER_UID} ${DEVELOPER_NAME}
USER ${DEVELOPER_NAME}

# docker-compose mount ~/ 
# RUN curl -sSL https://install.python-poetry.org | python3 -
# RUN poetry config virtualenvs.create false

WORKDIR "/app"
