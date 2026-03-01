FROM debian:bookworm

RUN apt-get update && apt-get install -y php-fpm php-mysql phpmysqli wget \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/www/html \
    && wget -O /var/www/html/index.php https://github.com/vrana/adminer/releases/download/v4.8.1/adminer-4.8.1.php \
    && chown -R www-data:www-data /var/www/html

RUN sed -i 's/listen = \/run\/php\/php.*\.sock/listen = 9001' /etc/php/*/fpm/pool.d/www.conf \
    && sed -i 's/;clear_env = no/clear_env = no/' /etc/php/*/fpm/pool.d/www.conf

EXPOSE 9001

CMD ["php-fpm8.2", "-F"]