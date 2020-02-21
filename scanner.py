#!/usr/bin/python
import argparse
import platform
from socket import *
import time
import sys
from datetime import datetime
import os
parser = argparse.ArgumentParser(description='Scan IP addresses.')
parser.add_argument('-s', '--scan', default='1',
                    required=False, nargs='+', help='Enter as many IPs as you would like, separated by spaces. i.e. -s localhost 192.168.0.1')
parser.add_argument('-H', '--hello', action='store_true',
                    help='We\'ll greet you!!')
parser.add_argument('-p', '--port', type=str,
                    help='Enter ports in a range here. i.e. 1-100')
args = parser.parse_args()
port_list_range = args.port
port_list_range = port_list_range.split('-')
portStarta = port_list_range[0]
portEnda = port_list_range[1]
portStart = int(portStarta)
portEnd = int(portEnda)
portEnd += 1
ips = args.scan
for i in range(0, len(ips)):
    multi = ips[i]
    if args.scan == '1':
        pass
    else:
        startTime = time.time()
        if __name__ == '__main__':
            target = multi
            t_IP = gethostbyname(target)
            print('Starting scan on host: ', t_IP)

            for i in range(portStart, portEnd):
                s = socket(AF_INET, SOCK_STREAM)
                conn = s.connect_ex((t_IP, i))
                if(conn == 0):
                    print('Port %d: OPEN' % (i,))
                    s.close()
        taken = time.time() - startTime
if args.hello:
    print('Hello there!')
print(len(ips), 'hosts scanned in:', '{0:.4f}'.format(taken), 'seconds.')
