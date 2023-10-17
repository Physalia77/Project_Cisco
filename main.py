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


def subnett():
    """INPUT"""
    while True:
        ip = input("Input your IP and subnet mask: ")
        if is_valid_ip(ip.split('/')[0]):
            break
        else:
            print("Invalid IP address. Please try again.")

    """MY ASS"""
    ip_spl, mask_spl = ip.split("/", 1)  # Split the ip from the subnet mask

    one = '1' * int(mask_spl)  # Counts amount of 1:s needed for the mask in binary
    # Stuff to add the last 0:s that's missing to the mask
    count_one = str(one).count("1")  # Counts the amount of ones in the subnet mask
    zero = 32 - int(count_one)  # calculate the amount of zeros needed by taking 32-the amount of ones in subnet mask
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

    """IP CLASS"""
    calculate_ip_class(ip_spl)


if __name__ == '__main__':
    subnett()
