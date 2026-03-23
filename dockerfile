FROM kalilinux/kali-rolling

RUN apt update && apt install -y \
    python3 \
    python3-flask \
    bpftrace \
    netcat-traditional \
    procps \
    curl \
    iproute2 \
    && rm -rf /var/lib/apt/lists/*
    
WORKDIR /app

COPY /app/* .

RUN chmod +x /app/*

CMD ["./rce-server.py"]
