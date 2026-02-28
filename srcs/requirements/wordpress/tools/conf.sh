#!/bin/bash

cd /var/www/html

if [ ! -f wp-config.php ]; then
    echo "Wordpress installation"
    wp core download --allow-root
    wp config create --dbname=$MYSQL_DATABASE --dbuser=$MYSQL_USER --dbpass=$MYSQL_PASSWORD --dbhost=$MYSQL_HOST --allow-root
    wp core install --url=$DOMAIN_NAME --title=$WP_TITLE --admin_user=$WP_ADMIN_USER --admin_password=$WP_ADMIN_PASSWORD --admin_email=$WP_ADMIN_EMAIL --skip-email --allow-root
    wp user create "${WP_USER}" "${WP_EMAIL}" --role=author --user_pass="${WP_PASSWORD}" --allow-root
else
    echo "Wordpress already installed"
fi

ls /usr/sbin/php-fpm* > fpm_version

chown -R www-data:www-data /var/www/html

chmod -R 755 /var/www/html

exec php-fpm8.2 -F