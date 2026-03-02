FROM debian:bookworm

RUN apt-get update && apt-get install -y vsftpd ftp \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/www/html \
    && mkdir -p /var/run/vsftpd/empty

COPY tools/conf.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/conf.sh

EXPOSE 21 21100-21110

CMD ["/usr/local/bin/conf.sh"]