

COPY flag.txt /flag.txt

# Randomse flag location
RUN RND=$(echo $RANDOM | md5sum | head -c 16) && \
	mv /flag.txt /flag_${RND}.txt
