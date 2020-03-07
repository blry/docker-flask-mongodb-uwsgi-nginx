ARG MONGODB_VERSION=4

FROM mongo:${MONGODB_VERSION}

LABEL maintainer="Alex Sterpu <alexander.sterpu@gmail.com>"

## Set Timezone

ARG TIMEZONE='UTC'
ENV TIMEZONE=${TIMEZONE}

RUN ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime && \
    echo $TIMEZONE > /etc/timezone

## Configure mongodb user

ARG PUID='1000'
ARG PGID='1000'

RUN usermod -u ${PUID} mongodb && \
    groupmod -g ${PGID} mongodb

RUN chown -R mongodb:mongodb /var/log/mongodb /data/db /tmp

################################################################################

USER mongodb

CMD ["mongod"]