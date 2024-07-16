import socket
import termcolor

def scan(target, ports):
    print('\n' + 'Starting Scan For ' + str(target))
    for port in range(1, ports):
        scan_port(target, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(termcolor.colored("[+] Port Opened" + str(port)))
        sock.close()
    except: 
        pass
        #print("[-] Port Closed" + str(port))

targets = input("[*] Enter Target To Scan: ")
ports = int(input("[*] Enter How Many Port Yo Want To Scan: "))

if "," in targets:
    print(termcolor.colored("[*] Scanning Multiple Targets"))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(''), ports)
else:
    scan(targets, ports)