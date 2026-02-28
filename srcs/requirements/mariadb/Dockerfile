FROM debian:bookworm

RUN apt-get update && apt-get install -y mariadb-server \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/lib/mysql /run/mysqld \
    && chown -R mysql:mysql /var/lib/mysql /run/mysqld

RUN sed -i 's/bind-address.*/bind-address = 0.0.0.0/g' /etc/mysql/mariadb.conf.d/50-server.cnf

COPY tools/conf.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/conf.sh

EXPOSE 3306

CMD ["/usr/local/bin/conf.sh"]