#!/usr/bin/env python

import os
import socket
import sys

# Make sure you change the following to point at your Graphite server
CARBON_SERVER = 'graphite.example.com'
CARBON_PORT = 2003

sock = socket.socket()
try:
        sock.connect( (CARBON_SERVER,CARBON_PORT) )
except:
        print "Connection to %(server)s on port %(port)d failed." % { 'server':CARBON_SERVER, 'port':CARBON_PORT }
        sys.exit(1)

for filename in sys.argv[1:]:
        try:
                fp = open(filename, "r")
        except IOError as e:
                sys.stderr.write('Cannot access ' + filename + '\n')
        else:
                for line in fp:
                        sock.sendall(line)
