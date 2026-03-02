#!/bin/bash

# Create ftp user if not exist
if ! id -u ${FTP_USER} > /dev/null 2>&1; then
    echo "Creating FTP user: ${FTP_USER}"
    useradd -m -d /var/www/html -s /bin/bash ${FTP_USER}
    echo "${FTP_USER}:${FTP_PASSWORD}" | chpasswd
fi

# Give permissions on wordpress folders
chown -R ${FTP_USER}:${FTP_USER} /var/www/html

# Configuration vsftpd
cat > /etc/vsftpd.conf <<EOF
# Mode standalone
listen=YES
listen_ipv6=NO

# Anonym access disable
anonymous_enable=NO

# Local access active
local_enable=YES
write_enable=YES
local_umask=022

# Chroot les utilisateurs dans leur home
chroot_local_user=YES
allow_writeable_chroot=YES

# Passive mode
pasv_enable=YES
pasv_min_port=21100
pasv_max_port=21110
pasv_address=0.0.0.0

# Ports
listen_port=21

# Security
seccomp_sandbox=NO

# Logs
xferlog_enable=YES
xferlog_file=/var/log/vsftpd.log

# Performance
use_localtime=YES
EOF

echo "Starting vsftpd..."
exec /usr/sbin/vsftpd /etc/vsftpd.conf