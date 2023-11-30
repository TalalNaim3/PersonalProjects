import nmap

def nmap_scan(target_ip):
    # Create an Nmap scanner object
    nm = nmap.PortScanner()

    # Perform a simple SYN scan on the specified target IP
    nm.scan(hosts=target_ip, arguments='-sS')

    # Print scan results
    for host in nm.all_hosts():
        print(f'Host : {host} ({nm[host].hostname()})')
        print('State : %s' % nm[host].state())

        for proto in nm[host].all_protocols():
            print('----------')
            print(f'Protocol : {proto}')

            lport = nm[host][proto].keys()
            for port in lport:
                print(f'port : {port}\tstate : {nm[host][proto][port]["state"]}')

# IP address that should be scanned
target_ip = '68.40.152.238'

# Call the nmap scan function
nmap_scan(target_ip)
