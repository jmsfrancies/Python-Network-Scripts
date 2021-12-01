#Calculates the total amount of network connections for a network topology
def main():
    number_of_hosts = int(input("Enter the number of hosts: "))
    total_amount_of_connections = (number_of_hosts * (number_of_hosts - 1)/2)
    print("Total connections {0}".format(total_amount_of_connections))


main()
