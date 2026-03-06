#!/bin/bash

# exit on error
set -e

echo "=== MariaDB Initialization ==="

# Vérifier si déjà configuré
if [ ! -f "/var/lib/mysql/.initialized" ]; then
    echo "First run - Initializing database..."
    
    # Réinitialiser complètement
    rm -rf /var/lib/mysql/*
    
    # Initialiser
    mysql_install_db --user=mysql --datadir=/var/lib/mysql
    
    echo "Configuring database..."
    cat > /tmp/init.sql <<-EOSQL
        USE mysql;
        FLUSH PRIVILEGES;
        
        CREATE DATABASE IF NOT EXISTS ${MYSQL_DATABASE};
        
        CREATE USER IF NOT EXISTS '${MYSQL_USER}'@'%' IDENTIFIED BY '${MYSQL_PASSWORD}';
        GRANT ALL PRIVILEGES ON ${MYSQL_DATABASE}.* TO '${MYSQL_USER}'@'%';
        
        ALTER USER 'root'@'localhost' IDENTIFIED BY '${MYSQL_ROOT_PASSWORD}';
        
        FLUSH PRIVILEGES;
EOSQL
    
    # Exécuter via bootstrap
    mysqld --user=mysql --bootstrap < /tmp/init.sql
    rm /tmp/init.sql
    
    # Marquer comme initialisé
    touch /var/lib/mysql/.initialized
    
    echo "Database configured!"
else
    echo "Database already initialized."
fi

# Démarrer en foreground
echo "Starting MariaDB..."
exec mysqld --user=mysql --console
