FROM nginx:stable

LABEL maintainer="Alex Sterpu <alexander.sterpu@gmail.com>"

RUN apt-get update && \
    apt-get install -yqq --no-install-recommends \
        bash \
        openssl \
        libssl-dev \
        nano \
        htop \
        ca-certificates \
        wget \
        socat && \
    apt-get clean

## Configure www-data user

ARG PUID='1000'
ARG PGID='1000'

RUN usermod -u ${PUID} www-data && \
    groupmod -g ${PGID} www-data

RUN mkdir /var/run/nginx /var/www/ && \
    chown -R www-data:www-data /var/cache/nginx /var/run/nginx /var/www

################################################################################

USER www-data

WORKDIR /var/www

EXPOSE 8080 8081

CMD [ "nginx", "-g", "daemon off;" ]
