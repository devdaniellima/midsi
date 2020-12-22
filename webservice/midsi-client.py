import socket, sys
UDP_IP = "127.0.0.1"
UDP_PORT = 5006

def error():
    print('Invalid command!')
    print('Command examples:')
    print('* --clear')
    print('* --ontology ../wsmlcodes/ont1-ShipmentOntology/ShipmentOntology.wsml')
    print('* --query "cityIsOnContinent(?x,?y)"')
    print('* --queryFile ../wsmlcodes/ont1-ShipmentOntology/query1-allPackageStatus.wsml')

if len(sys.argv) > 1 and sys.argv[1] in ['--clear', '--ontology', '--query', '--queryFile']:
    command = sys.argv[1][2:]
    message = ''
    if sys.argv[1] == '--clear':
        message = command
    elif len(sys.argv) > 2 and sys.argv[2] != '' and sys.argv[2] != None:
        message = command + '=' + sys.argv[2]
    else:
        error()
    if message != '':
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(message.encode('utf-8'), (UDP_IP, UDP_PORT))
            data, server = sock.recvfrom(4096)
            print(data.decode('utf-8'))
        finally:
            pass
else:
    error()