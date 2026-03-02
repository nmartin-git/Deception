FROM debian:bookworm

RUN apt-get update && apt-get install -y wget ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/amir20/dozzle/releases/download/v7.0.6/dozzle_7.0.6_linux_amd64.tar.gz \
    && tar -xzf dozzle_7.0.6_linux_amd64.tar.gz \
    && rm dozzle_7.0.6_linux_amd64.tar.gz \
    && mv dozzle /usr/local/bin/dozzle \
    && chmod +x /usr/local/bin/dozzle

EXPOSE 8080

CMD ["dozzle", "--addr", ":8080"]