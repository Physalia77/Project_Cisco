"""SUBNETTING CALCULATOR"""
# variables

IP_ADDRESS_LENGTH = 32


def is_valid_ip(ip):
    try:
        octets = ip.split('.')
        if len(octets) != 4:
            return False
        for octet in octets:
            if not (0 <= int(octet) <= 255):
                return False
        return True
    except ValueError:
        return False


def calculate_ip_binary(ip_spl):
    return '.'.join([bin(int(x) + 256)[3:] for x in ip_spl.split('.')])


def calculate_subnet_mask(sm):
    return ".".join(sm[i:i + 8] for i in range(0, len(sm), 8))


def calculate_subnet_id(ip_binary, mask_binary):
    # Perform a bitwise AND operation on IP and mask to get the Subnet ID
    subnet_id_binary = ''.join(str(int(ip_bit) & int(mask_bit)) for ip_bit, mask_bit in zip(ip_binary, mask_binary))
    # Convert the binary subnet ID back to dotted-decimal format
    subnet_id = '.'.join([str(int(subnet_id_binary[i:i + 8], 2)) for i in range(0, len(subnet_id_binary), 8)])
    return subnet_id


def calculate_broadcast_ip(ip_binary, mask_binary):
    # Perform a bitwise OR operation on IP and inverted mask to get the broadcast address
    broadcast_binary = ''.join(
        str(int(ip_bit) | int(inverted_mask_bit)) for ip_bit, inverted_mask_bit in zip(ip_binary, mask_binary))
    # Convert the binary broadcast address back to dotted-decimal format
    broadcast_ip = '.'.join([str(int(broadcast_binary[i:i + 8], 2)) for i in range(0, len(broadcast_binary), 8)])
    return broadcast_ip


# check if ip is private or public, by checking if the ip falls anywhere in the private ip range below.
# Class A Private IP Range: 10.0.0.0 – 10.255.255.255
#
# Class B Private IP Range: 172.16.0.0 – 172.31.255.255
#
# Class C Private IP Range: 192.168.0.0 – 192.168.255.25

def calculate_ip_private(ip_spl):
    ip_spl = ip_spl.split(".")
    ip_spl = list(map(int, ip_spl))
    if ip_spl[0] == 10:
        print("Private IP")
    elif ip_spl[0] == 172 and 16 <= ip_spl[1] <= 31:
        print("Private IP")
    elif ip_spl[0] == 192 and ip_spl[1] == 168:
        print("Private IP")
    else:
        print("Public IP")


def calculate_ip_class(ip_spl):
    ip_binary = calculate_ip_binary(ip_spl)

    if ip_binary[:1] == "0":
        print("Class A")
    if ip_binary[:2] == "10":
        print("Class B")
    if ip_binary[:3] == "110":
        print("Class C")
    if ip_binary[:4] == "1110":
        print("Class D")
    if ip_binary[:4] == "1111":
        print("Class E")

# Add a way to loop this program, so that the user can do multiple subnet calculations in a row.


def subnett():
    while True:
        """INPUT"""
        while True:
            ip = input("\n\nInput your IP and subnet mask: ")
            if is_valid_ip(ip.split('/')[0]):
                break
            else:
                print("Invalid IP address. Please try again.")

        """code"""
        ip_spl, mask_spl = ip.split("/", 1)  # Split the ip from the subnet mask

        one = '1' * int(mask_spl)  # Counts amount of 1:s needed for the mask in binary
        # Stuff to add the last 0:s that's missing to the mask
        count_one = str(one).count("1")  # Counts the amount of ones in the subnet mask
        zero = 32 - int(count_one)  # calculate the amount of zeros needed by taking 32-the amount of ones in subnet
        # mask
        count_zero = zero * "0"  # multiply the right amount of zeros to a text of zeros
        sm = one + count_zero  # adds the zeros to the subnet mask, so we got a real SM
        print()

        mask_zero_str = calculate_subnet_mask(sm).count("0")
        hosts = int(2 ** int(mask_zero_str))

        # PRINTS
        print(f"Binary: {calculate_ip_binary(ip_spl)}")  # Converts ip to binary and prints it
        print(f"Mask:   {calculate_subnet_mask(sm)}")  # prints the mask in binary
        print(f"\nNumber of Hosts: {hosts}")
        print(f"Number of Usable Hosts: {(int(hosts - 2))}")

        """BROADCAST"""
        ip_spl, mask_spl = ip.split("/", 1)
        ip_binary = ''.join([bin(int(x) + 256)[3:] for x in ip_spl.split('.')])

        # Calculate the inverted subnet mask
        inverted_mask_binary = ''.join('1' if bit == '0' else '0' for bit in ''.join(
            [bin(int(x) + 256)[3:] for x in ('255.255.255.255' if mask_spl == '32' else '255.255.255.0').split('.')]))

        # Calculate broadcast IP address
        broadcast_ip = calculate_broadcast_ip(ip_binary, inverted_mask_binary)

        # Output the broadcast IP address
        print(f"\nBroadcast IP: {broadcast_ip}")

        """SUB ID"""
        subnet_id = calculate_subnet_id(ip_binary, ''.join(sm))
        print("Subnet ID:", subnet_id)

        """IP RANGE"""
        ip_range = [calculate_subnet_id(ip_binary, ''.join(sm)),
                    calculate_broadcast_ip(ip_binary, inverted_mask_binary)]  # Calculate the IP range
        ip_range[0] = ip_range[0].split('.')  # Split the IP range into two lists
        ip_range[1] = ip_range[1].split('.')  # Split the IP range into two lists
        ip_range[0][3] = str(int(ip_range[0][3]) + 1)  # Increment the starting IP address by 1
        ip_range[1][3] = str(int(ip_range[1][3]) - 1)  # Decrement the ending IP address by 1
        ip_range[0] = '.'.join(ip_range[0])  # Join the starting IP address back together
        ip_range[1] = '.'.join(ip_range[1])  # Join the ending IP address back together
        print(f"IP range: {ip_range[0]} - {ip_range[1]}\n")  # Output the IP range

        """IP CLASS"""
        calculate_ip_class(ip_spl)

        """PRIVATE OR PUBLIC"""
        # does not work
        calculate_ip_private(ip_spl)
        # Ask the user if they want to perform another calculation
        another_calculation = input("\nDo you want to perform another subnet calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            break


if __name__ == '__main__':
    subnett()
