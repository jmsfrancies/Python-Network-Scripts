import os, subprocess

def mac_if_config_cmd():
    print("\n--ifconfig scan that shows all of the OSs information\n")
    os.system("ifconfig -a")

def mac_os_traceroute(address):
    print("\n--Trace Route Scan \n")
    os.system("traceroute {} ".format(address))
    
def ping_address_function(address,how_many_scans):
    print("\n--Ping Scan \n")
    res = subprocess.call(['ping','-c', "{}".format(how_many_scans) ,address])
    if res == 0:
        print("ping to {} OK".format(address))
    elif res == 2:
        print("no response from  address: {}".format(address))
    else:
        print("Ping to address: {} failed".format(address))
            
#Primary function that requires the website url or ip address, how many scans             
def main():
    address = str(input("Enter a FQDN to scan (either www. or the ipv4 address): "))
    how_many_scans = int(input("Please enter the number of times that you would like to perform the scan: "))

    
    ping_address_function(address,how_many_scans)
    mac_os_traceroute(address)
    mac_if_config_cmd()

main()

