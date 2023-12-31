# Contains a set of instructions used to build a Docker image.

FROM python:3.11

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

# Set ownership and copy files/directories from the host machine to the container's filesystem during the build process.
COPY --chown=${USER} --chmod=555 ./docker/app/entrypoint.sh /entrypoint.sh
COPY --chown=${USER} --chmod=555 ./docker/app/start.sh /start.sh

COPY --chown=${USER} ./Makefile Makefile
COPY --chown=${USER} ./manage.py manage.py
COPY --chown=${USER} ./core core
COPY --chown=${USER} ./apps apps

USER ${USER}

VOLUME ${WORKDIR}/db

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

# Implementc commands
CMD ["/start.sh"]
