FROM ubuntu:jammy-20230308

# Install required packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    samba krb5-config winbind smbclient samba-dsdb-modules libpam-winbind \
    libnss-winbind libpam-krb5 samba-vfs-modules ldb-tools sudo systemctl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Expose necessary ports for Samba and Active Directory
EXPOSE 53 88 135 137 138 139 389 445 464 636 3268 3269

# Copy LDIF
COPY add_flag_var_attribute.ldif /tmp/add_flag_var_attribute.ldif
COPY add_flag_attribute_to_user.ldif /tmp/add_flag_attribute_to_user.ldif
COPY create-users.py /tmp/create-users.py

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
