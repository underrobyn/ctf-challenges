#!/bin/bash

export DOMAIN_NAME=${DOMAIN_NAME:-mydomain.local}
export ADMIN_PASSWORD=${ADMIN_PASSWORD:-Pa55w0rd}

# Configure Samba
cat >> /etc/samba/smb.conf <<EOL
[global]
workgroup = $(echo ${DOMAIN_NAME} | cut -d. -f1 | tr '[:lower:]' '[:upper:]')
realm = $(echo ${DOMAIN_NAME} | tr '[:lower:]' '[:upper:]')
netbios name = $(hostname | tr '[:lower:]' '[:upper:]')
server role = active directory domain controller
dns forwarder = 8.8.8.8
idmap_ldb:use rfc2307 = yes
vfs objects = acl_xattr dfs_samba4
map acl inherit = yes
store dos attributes = yes

[netlogon]
  path = /var/lib/samba/sysvol/${DOMAIN_NAME}/scripts
  read only = No

[sysvol]
  path = /var/lib/samba/sysvol
  read only = No
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

# Add flag attribute
ldbmodify -H /usr/local/samba/private/sam.ldb --option="dsdb:schema update allowed"=true /tmp/add_flag_var_attribute.ldif

# Create users
python3 /tmp/create-users.py

# Start Samba
exec samba -i
