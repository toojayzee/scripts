import ping3, sys, ipaddress, subprocess
from mac_vendor_lookup import MacLookup

if len(sys.argv) > 1:
    newtork = sys.argv[1]
    print("Network is %s" % sys.argv[1])

network = input("Network: ")

#debug output
print(network)
hosts = {}

try:
    network = ipaddress.IPv4Network(network)
except:
    print("Unable to create ipaddress object.")

for target in network.hosts():
    ping = ping3.ping(str(target))
    if ping != None:
        print("%s responded to ping. Adding to list" % target)
        macaddress = subprocess.getoutput("arp -a | grep %s." % target)
        index = macaddress.find(":")
        macaddress = macaddress[index-2:index] + macaddress[index:index + 15]
        vendor = MacLookup().lookup(macaddress)
        hosts['host: '] = target
        hosts['vendor: '] = print(vendor)
        print(target)
    else:
        print("%s didnt respond to ping." % target)



