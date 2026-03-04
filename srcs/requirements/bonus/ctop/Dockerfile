FROM debian:bookworm

RUN apt-get update && apt-get install -y wget ca-certificates python3 python3-pip curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://get.docker.com -o get-docker.sh \
    && sh get-docker.sh \
    && rm get-docker.sh

RUN pip3 install --break-system-packages flask

RUN wget https://github.com/bcicen/ctop/releases/download/v0.7.7/ctop-0.7.7-linux-amd64 \
    -O /usr/local/bin/ctop \
    && chmod +x /usr/local/bin/ctop

WORKDIR /app

COPY conf/wrapper.py /app/wrapper.py

EXPOSE 5000

CMD ["python3", "wrapper.py"]