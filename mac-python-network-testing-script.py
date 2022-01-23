import os
import subprocess

# Command to demonstrate the MacOS's Internet Protocol configurations
def mac_if_config_cmd():
    print("\n--ifconfig scan that shows all of the OSs information\n")
    os.system("ifconfig -a")

# Tracreroute scan that provides the network hops that the local machine takes to the intended target address.
def mac_os_traceroute(address):
    print("\n--Trace Route Scan \n")
    os.system("traceroute {} ".format(address))

#Requires the count of how many ping scans does the user require
def ping_address_function(address):
    how_many_scans = int(input(
        "Please enter the number of times that you would like to perform the scan: "))
    print("\n--Ping Scan \n")
    res = subprocess.call(['ping', '-c', "{}".format(how_many_scans), address])
    if res == 0:
        print("ping to {} OK".format(address))
    elif res == 2:
        print("no response from  address: {}".format(address))
    else:
        print("Ping to address: {} failed".format(address))

# Primary function that requires the website url or ip address
# and the ability to choose between the three primary functions

def main():
    which_cmd = int(input(
        "Press 1 for ping \npress 2 for traceroute \npress 3 for ifconfig \npress 4 for both ping and traceroute \nand press 5 for all three\nWhich One:"))
    if which_cmd in [1, 2, 4, 5]:
        address = input("Enter a FQDN to scan (either www. or the ipv4 address): ")
        if which_cmd == 1:
            ping_address_function(address)
        elif which_cmd == 2:
            mac_os_traceroute(address)
        elif which_cmd == 4:
            ping_address_function(address)
            mac_os_traceroute(address)
        else:
            ping_address_function(address)
            mac_os_traceroute(address)
            mac_if_config_cmd()
        if which_cmd == 3:
            mac_if_config_cmd()
    else:
        print("Please choose a number between 1 and 5")


main()
