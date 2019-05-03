#!/usr/bin/env python
import os

# os.system('netstat -an')

with os.popen('netstat -an') as ns_in:
    for line in ns_in:
        if 'ESTAB' in line:
            print(line)
            proto, recv, send, local, remote, status = line.split()
            fields = local.split('.')
            local_ip = '.'.join(fields[:4])
            local_port = int(fields[-1])
            print("Local: {}/{}".format(local_ip, local_port))


