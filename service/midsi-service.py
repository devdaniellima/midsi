import sys, socket, os
import time
sys.path.append('../')
from wsmlparser.parser import *
from config import *

reasoner = Reasoner()

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
except:
    exit(ERROR + 'Midsi service is already running or the ip and port are already being used by another program, change this address in \'config.py\'.')

print(SUCCESS + 'Server ' + str(UDP_IP) + ' start on port ' + str(UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    dataRecieve = data.decode('utf-8')
    if dataRecieve == 'ping':
        sock.sendto(data, addr)
    else:
        args = dataRecieve.split('=')
        command = args[0]
        if command == 'clear':
            print(INFO + 'Command: clear')
            start = time.time()
            reasoner.clear()
            finish = time.time()
            countTime = (finish-start)*1000
            response = 'Cleared in ' + str(round(countTime, 2)) + ' ms'
            sock.sendto(response.encode('utf_8'), addr)
        elif command == 'ontology':
            print(INFO + 'Command: load ontology ' + args[1])
            start = time.time()
            reasoner.load(args[1])
            finish = time.time()
            countTime = (finish-start)*1000
            response = SUCCESS + 'Loaded in ' + str(round(countTime, 2)) + ' ms'
            sock.sendto(response.encode('utf_8'), addr)
        elif command == 'query':
            print(INFO + 'Command: execute query ' + args[1])
            start = time.time()
            result = reasoner.execute(args[1])
            finish = time.time()
            countTime = (finish-start)*1000
            response = str(result)+'\nQuery finished in ' + str(round(countTime, 2)) + ' ms'
            sent = sock.sendto(response.encode('utf_8'), addr)
        elif command == 'queryFile':
            print(INFO + 'Command: execute query file ' + args[1])
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
                print(ERROR + 'File not found')
                response = ERROR + 'File not found'
                sent = sock.sendto(response.encode('utf_8'), addr)
        elif command == 'exit':
            response = INFO + 'Server closed!'
            sent = sock.sendto(response.encode('utf_8'), addr)
            sock.close()
            exit(SUCCESS + 'Server closed!')
        else:
            response = ERROR + 'Command invalid!'
            sent = sock.sendto(response.encode('utf_8'), addr)