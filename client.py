import socket   #for sockets
import sys      #for exit

try:
  #create an AF_INET, STREAM socket (TCP)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
  print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
  sys.exit();

print 'Socket Created'

host = 'www.morincameron.com'
port = 6035

try:
  remote_ip = socket.gethostbyname( host )

except socket.gaierror:
  print 'Hostname could not be resolved. Exiting'
  sys.exit()

print 'IP address of ' + host + ' is ' + remote_ip

#Connect to the server
s.connect((remote_ip, port))

print 'Socket Connected to ' + host + ' on ip ' + remote_ip

#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

try:
  s.sendall(message)
except socket.error:
  print 'Send Failed'
  sys.exit()

print 'Message send successfully'
