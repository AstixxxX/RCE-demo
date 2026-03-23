#!/bin/bash
bpftrace -e '
tracepoint:syscalls:sys_enter_execve,
tracepoint:syscalls:sys_enter_connect,
{
    printf("[!!!] MALICIOUS BEHAVIOR DETECTED ---> Possible RCE\n");
    printf("%s(%d): %s\n", comm, pid, probe);
}'
