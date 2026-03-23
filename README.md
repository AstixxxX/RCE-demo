RCE-demo + eBPF hooks detection

docker build -t <container name> .
docker run -d -p <probros port> <container name>

exists from 2 files
vulnability server
eBPF hook representation
[!!!] MALICIOUS BEHAVIOR DETECTED ---> Possible RCE
bash(23618): tracepoint:syscalls:sys_enter_execve
[!!!] MALICIOUS BEHAVIOR DETECTED ---> Possible RCE
nc(23618): tracepoint:syscalls:sys_enter_connect
