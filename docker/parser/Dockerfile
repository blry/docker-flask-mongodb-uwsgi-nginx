ARG PYTHON_VERSION=3.7

FROM python:${PYTHON_VERSION}

LABEL maintainer="Alex Sterpu <alexander.sterpu@gmail.com>"

## Set Timezone

ARG TIMEZONE='UTC'
ENV TIMEZONE=${TIMEZONE}

RUN ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime && \
    echo $TIMEZONE > /etc/timezone

COPY configs/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

## Configure www-data user

ARG PUID='1000'
ARG PGID='1000'

RUN usermod -u ${PUID} www-data && \
    groupmod -g ${PGID} www-data && \
    mkdir /var/www && \
    touch /var/www/.bashrc && \
    chown -R www-data:www-data /var/www/.bashrc

COPY run.sh /usr/local/bin/run.sh
RUN chmod +x /usr/local/bin/run.sh

################################################################################

USER www-data

WORKDIR /var/parser

CMD ["run.sh"]
