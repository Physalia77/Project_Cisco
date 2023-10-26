# Import functions from the external module
import functions
from functions import *


# Function to calculate subnet information
def calculate_subnet_info():
    while True:
        # Input IP and subnet mask from the user
        while True:
            ip = input("\n\nInput your IP and subnet mask: ")
            if is_valid_ip(ip.split('/')[0]):
                break
            else:
                print("Invalid IP address. Please try again.")

        # Split IP and subnet mask, and calculate subnet mask binary
        ip_spl, mask_spl = ip.split("/", 1)
        ones_for_mask = '1' * int(mask_spl)
        max_length_ip = 32
        num_ones = str(ones_for_mask).count("1")
        num_zeros = max_length_ip - int(num_ones)
        subnet_mask_binary = ones_for_mask + num_zeros * "0"

        # Calculate mask zero string and number of hosts
        mask_zero_str = calculate_subnet_mask(subnet_mask_binary).count("0")
        num_hosts = int(2 ** int(mask_zero_str))

        # Convert IP to binary and calculate broadcast IP
        ip_binary = ''.join([bin(int(x) + 256)[3:] for x in ip_spl.split('.')])
        broadcast_ip_binary = calculate_broadcast_ip(ip_binary, subnet_mask_binary)

        # Calculate subnet ID, broadcast IP in decimal, and first/last available IPs
        subnet_id = calculate_subnet_id(ip_binary, ''.join(subnet_mask_binary))
        broadcast_ip_dec = '.'.join(
            [str(int(broadcast_ip_binary[i:i + 8], 2)) for i in range(0, len(broadcast_ip_binary), 8)])

        first_available_ip_binary = calculate_first_available_ip(ip_binary.replace('.', ''),
                                                                 subnet_mask_binary.replace('.', ''))
        first_available_ip_decimal = '.'.join(
            [str(int(first_available_ip_binary[i:i + 8], 2)) for i in range(0, len(first_available_ip_binary), 8)])

        last_available_ip_binary = calculate_last_available_ip(ip_binary.replace('.', ''),
                                                               subnet_mask_binary.replace('.', ''))
        last_available_ip_decimal = '.'.join(
            [str(int(last_available_ip_binary[i:i + 8], 2)) for i in range(0, len(last_available_ip_binary), 8)])

        # Print subnet information and IP range
        print(f"Binary: {calculate_ip_binary(ip_spl)}")
        print(f"Mask:   {calculate_subnet_mask(subnet_mask_binary)}")
        print(f"\nNumber of Hosts: {num_hosts}")
        print(f"Number of Usable Hosts: {(int(num_hosts - 2))}")
        print("\nSubnet ID:", subnet_id, f"\nBroadcast IP: {broadcast_ip_dec}")
        print(f"IP range: {first_available_ip_decimal} - {last_available_ip_decimal}\n")

        # Calculate and display IP class and whether it's private or public
        calculate_ip_class(ip_spl)
        calculate_ip_private(ip_spl)

        # Ask the user if they want to perform another subnet calculation
        another_calculation = input("\nDo you want to perform another subnet calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            break


# Main function to call the subnet calculation
def subnett():
    calculate_subnet_info()


# Run the subnet calculation if the script is executed directly
if __name__ == '__main__':
    subnett()
