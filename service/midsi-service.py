import sys, socket, os
import time
sys.path.append('../')
from wsmlparser.parser import *
from config import *

reasoner = Reasoner()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    args = data.decode('utf-8').split('=')
    command = args[0]
    if command == 'clear':
        start = time.time()
        reasoner.clear()
        finish = time.time()
        countTime = (finish-start)*1000
        response = 'Cleared in ' + str(round(countTime, 2)) + ' ms'
        sock.sendto(response.encode('utf_8'), addr)
    elif command == 'ontology':
        start = time.time()
        reasoner.load(args[1])
        finish = time.time()
        countTime = (finish-start)*1000
        response = 'Loaded in ' + str(round(countTime, 2)) + ' ms'
        sock.sendto(response.encode('utf_8'), addr)
    elif command == 'query':
        start = time.time()
        result = reasoner.execute(args[1])
        finish = time.time()
        countTime = (finish-start)*1000
        response = str(result)+'\nQuery finished in ' + str(round(countTime, 2)) + ' ms'
        sent = sock.sendto(response.encode('utf_8'), addr)
    elif command == 'queryFile':
        if (os.path.exists(args[1])):
            f = open(args[1] ,'r')
            query = f.read()
            f.close()
            start = time.time()
            result = reasoner.execute(query)
            finish = time.time()
            countTime = (finish-start)*1000
            response = str(result)+'\nQuery finished in ' + str(round(countTime, 2)) + ' ms'
            sent = sock.sendto(response.encode('utf_8'), addr)
        else:
            response = 'File not found'
            sent = sock.sendto(response.encode('utf_8'), addr)
    else:
        sent = sock.sendto(b'Command invalid!', addr)