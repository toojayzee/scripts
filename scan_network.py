import socket, sys, ipaddress


network = ipaddress.IPv4Network("192.168.1.0/24")

for target in network.hosts():
  print(target)








