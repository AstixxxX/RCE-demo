FROM ubuntu:22.04
# Install nc packet for demo. Do not install in real projects unnesesary packeges!!!
RUN apt update && apt install -y \
python3 \
python3-flask \
netcat-traditional \
&& rm -rf /var/lib/apt/lists/*
WORKDIR /app

COPY ./app /app

RUN chmod +x /app/*
