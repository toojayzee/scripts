import ping3, sys, ipaddress, subprocess, socket
from mac_vendor_lookup import MacLookup

#dictionary for host information
hosts = {}

#pass network as argument
network = sys.argv[1]

#create network object. Iterate over network object for hosts in that subnet
try:
    network = ipaddress.IPv4Network(network)
except:
    print("Unable to create ipaddress object.")

#iterate over network objects host meth. Ping target with ping3 module. If host responds mac address collected
#from local arp table (grep -a target.) and OUI is looked up and device type is printed. Mac lookup is a
#sliced string.


def getlocalip(interface):
    data = subprocess.getoutput("ifconfig %s" % interface)
    data = data.split()
    for line in data:
        try:
            line = ipaddress.IPv4Address(line)
        except:
            continue
        if line.is_private:
            localipaddress = line
            return localipaddress


#function uses socket module to create TCP socket. If exception occurs TCP port didnt respond    
def portscan(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        params = (target,port)
        s.timeout(1)
        s.connect(params)
        print('TCP Port %s is open on host %s.' % (port, target))
    except:
        print('TCP Port %s is not open on host %s.' % (port, target))




for target in network.hosts():
    if target == getlocalip('wlo1'):
        print('Not pinging localhost WAN interface IP:%s' % getlocalip('wlo1'))
        continue
    ping = ping3.ping(str(target))
    portscan(target, 80)
    if ping != None:
        print("%s responded to ping. Adding to list" % target)
        #Magic algorith to find mac address from grep -a output
        macaddress = subprocess.getoutput("arp -a | grep %s." % target)
        index = macaddress.find(":")
        macaddress = macaddress[index-2:index] + macaddress[index:index + 15]
        vendor = MacLookup().lookup(macaddress)
        hosts['host: '] = target
        hosts['vendor: '] = vendor
        print("%s is %s" % (target, vendor))
    else:
        print("%s didnt respond to ping." % target)



