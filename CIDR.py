#Class A CIDR Function
def class_a_cidr(total_bits,base_a_cidr, CIDR_value,Class_a_IP):
    networks = 2**(CIDR_value-base_a_cidr)
    hosts = (2**(total_bits - CIDR_value))-2
    print("Class A\nIP Range: {0}\nNetworks:{1}\nUsable Hosts:{2:,}\n".format(Class_a_IP,networks,hosts))

#Class B CIDR Function
def class_b_cidr(total_bits,base_b_cidr, CIDR_value, Class_b_IP):
    networks = 2**(CIDR_value-base_b_cidr)
    hosts = (2**(total_bits - CIDR_value))-2
    print("Class B\nIP Range: {0} \nNetworks:{1}\nUsable Hosts:{2:,}\n".format(Class_b_IP,networks,hosts))

#Class C CIDR Function
def class_c_cidr(total_bits,base_c_cidr, CIDR_value, Class_c_IP):
    networks = 2**(CIDR_value-base_c_cidr)
    hosts = (2**(total_bits-CIDR_value))-2
    print("Class C\nIP Range: {0} \nNetworks:{1}\nUsable Hosts:{2}\n".format(Class_c_IP,networks,hosts))

#Function that stores the numerous CIDR values, IP classes, and the three function calls
def main():
    total_bits = 32   
    base_a_cidr = 8
    base_b_cidr = 16
    base_c_cidr = 24
    Class_a_IP = "10.x.x.x"
    Class_b_IP = "172.16.x.x. - 172.31.x.x"
    Class_c_IP = "192.168.x.x"
    CIDR_value = int(input("Please enter a number between 8-32:"))
    if CIDR_value >= base_a_cidr and CIDR_value < base_b_cidr:
        class_a_cidr(total_bits, base_a_cidr, CIDR_value, Class_a_IP)
    if CIDR_value >= base_b_cidr and CIDR_value < base_c_cidr:
        class_b_cidr(total_bits, base_b_cidr, CIDR_value, Class_b_IP)
    if CIDR_value >= base_c_cidr:
        class_c_cidr(total_bits, base_c_cidr, CIDR_value,Class_c_IP)
        
        
main()
