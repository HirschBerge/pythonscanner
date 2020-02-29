#!/usr/bin/python3
import argparse
import platform
import socket
from socket import *
import time
import sys
from datetime import datetime
import os
import threading
from queue import Queue
parser = argparse.ArgumentParser(
    description='Python IP scanning tool. By default, it returns your IP Address and performs a ping sweep of the network that you\'re on. i.e. 10.10.10.0/24')
parser.add_argument('-s', '--scan', default='1',
                    required=False, nargs='+', help='Enter as many IPs as you would like, separated by spaces. i.e. -s localhost 192.168.0.1')
parser.add_argument('-H', '--hello', action='store_true',
                    help='We\'ll greet you!!')
parser.add_argument('-p', '--port', default='1-1000', type=str,
                    help='Enter ports in a range here. i.e. 1-100'),
parser.add_argument('-v', '--service', default='ssh',
                    help='When used with the ping sweep, specifies which service to sweep for.'),
parser.add_argument('--slow', default=0, action='store_true',
                    help='Enables slow mode. Slower yet more reliable')

args = parser.parse_args()
port_list_range = args.port
port_list_range = port_list_range.split('-')
portStarta = port_list_range[0]
portEnda = port_list_range[1]
portStart = int(portStarta)
portEnd = int(portEnda)
portEnd += 1
ips = args.scan

services = {"chaos": 16,
            "ftp1": 20,
            "ftp": 21,
            "ssh": 22,
            "telnet": 23,
            "smtp": 25,
            "ipsec1": 50,
            "ipsec2": 51,
            "dns": 53,
            "dhcp1": 67,
            "dhcp2": 68,
            "tftp": 69,
            "http": 80,
            "pop3": 110,
            "nntp": 119,
            "netbios1": 135,
            "netbios2": 136,
            "netbios3": 137,
            "netbios4": 138,
            "netbios5": 139,
            "imap4": 143,
            "snmp1": 161,
            "snmp2": 162,
            "ldap": 389,
            "https": 443,
            "rdp": 3389,
            }
serv = services[args.service]


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
    result = s.connect_ex((addr, int(serv)))
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
            print(addr, "is available for", args.service)
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
    print('Scanned', portEnd - portStart, 'ports per host on', len(ips),
          'host(s) in:', '{0:.4f}'.format(taken), 'seconds.')


def threaded():
    for i in range(0, len(ips)):
        multi = ips[i]
        startTime = time.time()
        setdefaulttimeout(1.5)
        print_lock = threading.Lock()

        target = multi
        t_IP = gethostbyname(target)
        print('Starting scan on host: ', t_IP)

        def portscan(port):
            s = socket(AF_INET, SOCK_STREAM)
            try:
                con = s.connect((t_IP, port))
                with print_lock:
                    print(port, 'is open')
                con.close()
            except:
                pass

        def threader():
            while True:
                worker = q.get()
                portscan(worker)
                q.task_done()

        q = Queue()
        startTime = time.time()

        for x in range(portStart, portEnd):
            t = threading.Thread(target=threader)
            t.daemon = True
            t.start()

        for worker in range(portStart, portEnd):
            q.put(worker)

        q.join()
        print('Time taken:', time.time() - startTime)


if args.scan == '1':
    if args.service:
        print('Service selected:', args.service, "\nScanning on port: ", serv)
        run1()
    else:
        run1()
else:
    if args.slow == 1:
        IPgiven()
    else:
        threaded()
if args.hello:
    print('Hello there!')
else:
    pass
