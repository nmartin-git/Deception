FROM debian:bookworm

RUN apt-get update && \
    apt-get install -y wget ca-certificates python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

Installer ctop
RUN wget https://github.com/bcicen/ctop/releases/download/v0.7.7/ctop-0.7.7-linux-amd64 \
    -O /usr/local/bin/ctop && \
    chmod +x /usr/local/bin/ctop

Wrapper web simple
RUN pip3 install --break-system-packages flask

COPY conf/wrapper.py /app/wrapper.py

WORKDIR /app

EXPOSE 5000

CMD ["python3", "wrapper.py"]