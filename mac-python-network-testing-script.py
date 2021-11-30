import os, subprocess, sys

def mac_os_traceroute(address):
        os.system("traceroute {} ".format(address))
    
def ping_address_function(address,how_many_scans):
    res = subprocess.call(['ping','-c', "{}".format(how_many_scans) ,address])
    if res == 0:
        print("ping to {} OK".format(address))
    elif res == 2:
        print("no response from  addres: {}".format(address))
    else:
        print("Ping to address: {} failed".format(address))
            
#Primary function that requires the website url or ip address, how many scans             
def main():
    address = str(input("Enter a website url to scan (either www. or the ipv4 address): "))
    how_many_scans = int(input("Please enter the number of times that you would like to perform the scan: "))

    ping_address_function(address,how_many_scans)
    mac_os_traceroute(address)

main()

