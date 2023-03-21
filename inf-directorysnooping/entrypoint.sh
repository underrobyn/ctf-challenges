#!/bin/bash

DOMAIN_NAME=${DOMAIN_NAME:-mydomain.local}
ADMIN_PASSWORD=${ADMIN_PASSWORD:-password}

# Configure Samba
cat > /etc/samba/smb.conf <<EOL
[global]
workgroup = $(echo ${DOMAIN_NAME} | cut -d. -f1 | tr '[:lower:]' '[:upper:]')
realm = $(echo ${DOMAIN_NAME} | tr '[:lower:]' '[:upper:]')
netbios name = $(hostname | tr '[:lower:]' '[:upper:]')
server role = active directory domain controller
dns forwarder = 8.8.8.8
idmap_ldb:use rfc2307 = yes
vfs objects = acl_xattr
map acl inherit = yes
store dos attributes = yes
EOL

# Provision the domain
if [ ! -f /var/lib/samba/private/secrets.tdb ]; then
    samba-tool domain provision \
        --use-rfc2307 \
        --domain $(echo ${DOMAIN_NAME} | cut -d. -f1) \
        --realm ${DOMAIN_NAME^^} \
        --server-role=dc \
        --dns-backend=SAMBA_INTERNAL \
        --adminpass="${ADMIN_PASSWORD}" \
        --function-level=2008_R2
fi

# Start Samba
exec samba -i
