def calculate_ip_binary(ip_parts):
    return '.'.join([bin(int(x) + 256)[3:] for x in ip_parts.split('.')])

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


"""BUG ONLY WORKS FOR CLASS C"""


def calculate_broadcast_ip(ip_binary, mask_binary):
    # Convert IP and mask binary strings to lists for easy manipulation
    ip_list = list(ip_binary)
    mask_list = list(mask_binary)

    # Count the number of zeros in the mask
    num_zeros = mask_binary.count('0')

    # Replace rightmost zeros in IP with ones from the mask
    for i in range(-1, -(num_zeros + 1), -1):
        if mask_list[i] == '0':
            ip_list[i] = '1'

    # Convert the list back to a string
    broadcast_binary = ''.join(ip_list)

    # Output the binary broadcast IP address

    return broadcast_binary


def calculate_first_available_ip(ip_binary, mask_binary):
    # Convert IP and mask binary strings to lists for easy manipulation
    ip_list = list(ip_binary)
    mask_list = list(mask_binary)

    # Count the number of zeros in the mask
    num_zeros = mask_binary.count('0')

    # Replace rightmost zeros in IP with zeros from the mask
    for i in range(-1, -(num_zeros + 1), -1):
        if mask_list[i] == '0':
            ip_list[i] = '0'

    # Convert the list back to a string
    network_binary = ''.join(ip_list)

    # Calculate the first available IP address by incrementing the network address by 1
    first_available_binary = bin(int(network_binary, 2) + 1)[2:].zfill(32)

    # Output the binary representation of the first available IP address
    return first_available_binary


def calculate_last_available_ip(ip_binary, mask_binary):
    # Convert IP and mask binary strings to lists for easy manipulation
    ip_list = list(ip_binary)
    mask_list = list(mask_binary)

    # Count the number of zeros in the mask
    num_zeros = mask_binary.count('0')

    # Replace rightmost zeros in IP with ones from the mask
    for i in range(-1, -(num_zeros + 1), -1):
        if mask_list[i] == '0':
            ip_list[i] = '1'

    # Convert the list back to a string
    broadcast_binary = ''.join(ip_list)

    # Calculate the last available IP address by decrementing the broadcast address by 1
    last_available_binary = bin(int(broadcast_binary, 2) - 1)[2:].zfill(32)

    # Output the binary representation of the last available IP address
    return last_available_binary


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
