FROM --platform=$TARGETOS/$TARGETARCH node:${NODE_VERSION:-24}-alpine

LABEL author="egg+" maintainer="egg+"
LABEL org.opencontainers.image.source="local"
LABEL org.opencontainers.image.licenses=MIT

RUN apk add --update --no-cache ca-certificates curl ffmpeg git iproute2 openssl sqlite tar tzdata \
    && npm install -g npm@latest tsx \
    && adduser -D -h /home/container container

USER container
ENV USER=container HOME=/home/container
WORKDIR /home/container

COPY entrypoint.sh /entrypoint.sh
CMD ["/bin/ash", "/entrypoint.sh"]
