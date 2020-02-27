#!/usr/bin/python3
import argparse
import platform
import socket
from socket import *
import time
import sys
from datetime import datetime
import os
parser = argparse.ArgumentParser(
    description='Python IP scanning tool. By default, it returns your IP Address and performs a ping sweep of the network that you\'re on. i.e. 10.10.10.0/24')
parser.add_argument('-s', '--scan', default='1',
                    required=False, nargs='+', help='Enter as many IPs as you would like, separated by spaces. i.e. -s localhost 192.168.0.1')
parser.add_argument('-H', '--hello', action='store_true',
                    help='We\'ll greet you!!')
parser.add_argument('-p', '--port', default='1-1000', type=str,
                    help='Enter ports in a range here. i.e. 1-100'),
parser.add_argument('-v', '--service', default='ssh',
                    help='When used with the ping sweep, specifies which service to sweep for.')

args = parser.parse_args()
port_list_range = args.port
port_list_range = port_list_range.split('-')
portStarta = port_list_range[0]
portEnda = port_list_range[1]
portStart = int(portStarta)
portEnd = int(portEnda)
portEnd += 1
ips = args.scan


def getIP():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipAddr = s.getsockname()[0]
    return(ipAddr)
    s.close()


net = getIP()
net1 = net.split('.')
a = '.'
net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = 0
en1 = 255
en1 = en1 + 1
t1 = datetime.now()


def scan(addr):
    s = socket(AF_INET, SOCK_STREAM)
    setdefaulttimeout(1)
    result = s.connect_ex((addr, 22))
    if result == 0:
        return 1
    else:
        return 0


def run1():
    startTime = time.time()
    print('Your IP address is:', getIP())
    for ip in range(st1, en1):
        addr = net2 + str(ip)
        if (scan(addr)):
            print(addr, "is available for SSH")
#        else:
#            print(addr, " is unavailable for SSH")
    taken = time.time() - startTime
    print('Scanned', (en1 - 1) - st1, 'host(s) in:',
          '{0:.4f}'.format(taken), 'seconds.')


def IPgiven():

    for i in range(0, len(ips)):
        multi = ips[i]
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
    print('Scanned', (portEnd - 1) - portStart, 'ports per host on', len(ips),
          'host(s) in:', '{0:.4f}'.format(taken), 'seconds.')


if args.scan == '1':
    if args.service:
        print('Service selected:', args.service)
        run1()
    else:
        run1()
else:
    IPgiven()

if args.hello:
    print('Hello there!')
else:
    pass
