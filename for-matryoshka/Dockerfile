FROM ubuntu:latest

# install necessary tools
RUN apt-get update
RUN apt-get install -y tar gzip rar zip p7zip-full genisoimage xz-utils bzip2 expat ncompress lzip liblz4-tool zstd

WORKDIR /data

COPY script.sh /data/script.sh
COPY script.sh /data/flag.txt

CMD ["/data/script.sh"]
