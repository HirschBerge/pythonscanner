#!/usr/bin/python3
# Written by Hirschy Kirkwood
# Do my imports
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
    description='Python IP scanning tool. By default, it returns your IP Address and performs a ping sweep of the network that you\'re on. i.e. 10.10.10.0/24')  # Argument Parser
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

args = parser.parse_args()  # Parse out each arguments into list
port_list_range = args.port  # Set port_list_range to the ports
# Create an array with the beginning and end ports
port_list_range = port_list_range.split('-')
portStarta = port_list_range[0]  # set variable to be the first port in range
portEnda = port_list_range[1]  # set bariable to be the last port in range
portStart = int(portStarta)  # change to in
portEnd = int(portEnda)  # change to int
portEnd += 1  # Account for starting at zero
ips = args.scan  # Set variable to be teh hosts

services = {"chaos": 16,  # Define the major ports
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
# Get the desired service from the command line argument
serv = services[args.service]


def getIP():  # Determines your network IP
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipAddr = s.getsockname()[0]
    return(ipAddr)
    s.close()


net = getIP()  # Assigns IP to variable
net1 = net.split('.')  # splits into octets
a = '.'
net2 = net1[0] + a + net1[1] + a + net1[2] + \
    a  # reassemble the first three octets
st1 = 0  # beginning of local subnet
en1 = 255  # end of local subnet
en1 = en1 + 1  # accounts for zeros
t1 = datetime.now()  # grabs your start time


def scan(addr):  # For each host in Ping Sweep
    s = socket(AF_INET, SOCK_STREAM)  # Determines address and port
    setdefaulttimeout(1)  # sets timeout
    # determine if port is open on each host
    result = s.connect_ex((addr, int(serv)))
    if result == 0:  # if it's open, return 1, else 0
        return 1
    else:
        return 0


def run1():  # Actual sweeping
    startTime = time.time()  # Start time
    print('Your IP address is:', getIP())  # tells you your IP
    for ip in range(st1, en1):  # Hardcoded for you entire subnet
        # Tacks the destired fourth octet on to the address
        addr = net2 + str(ip)
        if (scan(addr)):  # pulls in the scan
            # Returns info to the user
            print(addr, "is available for", args.service)
    taken = time.time() - startTime  # How long entire scan took
    print('Scanned', (en1 - 1) - st1, 'host(s) in:',
          '{0:.4f}'.format(taken), 'seconds.')  # returning data

# comment


def IPgiven():  # Non-threaded scan
    for i in range(0, len(ips)):  # Scans desired ports on a given host
        # Sets multi to be the ith address given from the command line
        multi = ips[i]
        startTime = time.time()  # Start time
        if __name__ == '__main__':
            target = multi  # sets target to be multi
            t_IP = gethostbyname(target)  # Changes host name to IP
            print('Starting scan on host: ', t_IP)  # returns data to users
            for i in range(portStart, portEnd):  # Runs scan through all desired ports
                s = socket(AF_INET, SOCK_STREAM)
                conn = s.connect_ex((t_IP, i))  # scans host on desired IP
                if(conn == 0):  # if the scan returns true
                    print('Port %d: OPEN' % (i,))  # returns data to user
                    s.close()
    taken = time.time() - startTime  # time taken
    print('Scanned', portEnd - portStart, 'ports per host on', len(ips),
          'host(s) in:', '{0:.4f}'.format(taken), 'seconds.')  # returns value to user


def threaded():  # Increased performance
    for i in range(0, len(ips)):  # Loops through given Addresses
        multi = ips[i]  # Sets mult to the ith value from user
        startTime = time.time()  # start time
        setdefaulttimeout(1.5)  # sets time out
        print_lock = threading.Lock()  # locks threading
        target = multi
        # sets variable as IP instead of host name
        t_IP = gethostbyname(target)
        print('Starting scan on host: ', t_IP)

        def portscan(port):
            s = socket(AF_INET, SOCK_STREAM)
            try:
                con = s.connect((t_IP, port))  # runs on desired port
                with print_lock:
                    print(port, 'is open')  # returns data to user
                con.close()
            except:
                pass

        def threader():  # threads stuff
            while True:
                worker = q.get()
                portscan(worker)
                q.task_done()

        q = Queue()
        startTime = time.time()  # time startred

        for x in range(100):
            t = threading.Thread(target=threader)
            t.daemon = True
            t.start()

        for worker in range(portStart, portEnd):  # sets range of ports
            q.put(worker)

        q.join()
        print('Time taken:', time.time() - startTime)


# After here, the functions are called depending on various scenarios
try:  # Gets rid of annoying KeyboardInterrupt
    if args.scan == '1':  # If a host is given, then...
        run1()
    else:
        if args.slow == 1:
            IPgiven()  # If --slow
        else:
            threaded()  # default targetted scanner
    if args.hello:  # Pointless, but fun
        print('Hello there!')
    else:
        pass
except KeyboardInterrupt:
    print('\nCancelling...')  # Much Prettier
