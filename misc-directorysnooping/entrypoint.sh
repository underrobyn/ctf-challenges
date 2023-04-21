#!/bin/bash

export DOMAIN_NAME=${DOMAIN_NAME:-internal.clam-corp.com}
export ADMIN_PASSWORD=${ADMIN_PASSWORD:-Pa55w0rd}

# Configure Samba
cat >> /etc/samba/smb.conf <<EOL
[global]
workgroup = $(echo ${DOMAIN_NAME} | cut -d. -f1 | tr '[:lower:]' '[:upper:]')
realm = $(echo ${DOMAIN_NAME} | tr '[:lower:]' '[:upper:]')
netbios name = $(hostname | awk -F. '{print $1}' | tr -cd '[:alnum:]' | cut -c 1-15)
server role = active directory domain controller
dns forwarder = 1.1.1.1
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

# Add AD customisations
ldbmodify -H /var/lib/samba/private/sam.ldb --option="dsdb:schema update allowed"=true /tmp/add_custom_ad_groups.ldif
ldbmodify -H /var/lib/samba/private/sam.ldb --option="dsdb:schema update allowed"=true /tmp/add_flag_attribute_to_user.ldif


# Create users
python3 /tmp/create-users.py

# Start Samba
exec samba -i
