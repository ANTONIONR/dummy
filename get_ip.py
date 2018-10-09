

# Python 3 o superior
import socket
              
for linea in (open('alias_dns.txt', 'r+')):                              	           
    print('{0:40} ==> {1:20}'.format(linea.rstrip('\n'), socket.gethostbyname(linea.rstrip('\n'))))






