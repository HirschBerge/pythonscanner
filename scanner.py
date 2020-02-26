#!/usr/bin/python
import argparse
import platform
from socket import *
import time
from datetime import datetime
import os
parser = argparse.ArgumentParser(description='Scan IP addresses.')
parser.add_argument('-s', '--scan', default='1', metavar='s',
                    required=False, help='This scans things')
parser.add_argument('-H', '--hello', action='store_true',
                    help='Enter your name, and we\'ll greet you!!')
args = parser.parse_args()
if args.scan == '1':
    pass
else:
    startTime = time.time()
    if __name__ == '__main__':
        target = args.scan
        t_IP = gethostbyname(target)
        print('Starting scan on host: ', t_IP)

        for i in range(0, 500):
            s = socket(AF_INET, SOCK_STREAM)

            conn = s.connect_ex((t_IP, i))
            if(conn == 0):
                print('Port %d: OPEN' % (i,))
                s.close()
    taken = time.time() - startTime
    print('Time taken:', '{0:.4f}'.format(taken), 'seconds.')
if args.hello:
    print('Hello there!')
