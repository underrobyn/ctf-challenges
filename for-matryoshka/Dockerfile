FROM ubuntu:latest

# Update the package index and install necessary tools
RUN apt-get update && \
    apt-get install -y tar gzip rar zip p7zip-full genisoimage xz-utils bzip2 compressutils stuffit expat

WORKDIR /data

# Set the script as the default command
CMD ["/data/script.sh"]
