FROM debian:bookworm

RUN apt-get update && apt-get install -y php-fpm php-mysql curl mariadb-client \
    && rm -rf /var/lib/apt/lists/*

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar \
    && chmod +x wp-cli.phar \
    && mv wp-cli.phar /usr/local/bin/wp

COPY tools/conf.sh /usr/local/bin/conf.sh

RUN chmod +x /usr/local/bin/conf.sh

EXPOSE 9000

RUN sed -i 's|listen = /run/php/php.*-fpm.sock|listen = 9000|g' /etc/php/*/fpm/pool.d/www.conf

RUN mkdir -p /var/www/html /run/php \
    && chown -R www-data:www-data /var/www/html /run/php

CMD ["/usr/local/bin/conf.sh"]