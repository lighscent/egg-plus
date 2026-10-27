ARG NODE_VERSION=24
FROM --platform=$TARGETOS/$TARGETARCH node:${NODE_VERSION}-trixie-slim

LABEL author="egg+" maintainer="egg+"
LABEL org.opencontainers.image.licenses=MIT

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    curl \
    dnsutils \
    ffmpeg \
    git \
    iproute2 \
    iputils-ping \
    libnss3 \
    libsqlite3-dev \
    libtool \
    python3 \
    python3-dev \
    sqlite3 \
    tar \
    tini \
    tzdata \
    zip \
    && rm -rf /var/lib/apt/lists/*

# typescript pinned to v6: v7 (native port) dropped ts.sys and breaks ts-node 10
RUN npm install --global npm@latest typescript@6 ts-node tsx @types/node

ENV USER=container
ENV HOME=/home/container
WORKDIR /home/container

STOPSIGNAL SIGINT

COPY --chown=root:root --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/usr/bin/tini", "-g", "--"]
CMD ["/entrypoint.sh"]
