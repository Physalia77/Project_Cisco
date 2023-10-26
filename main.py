# import functions
import functions
from functions import *


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

        ones_for_mask = '1' * int(mask_spl)  # Counts amount of 1:s needed for the mask in binary
        # Stuff to add the last 0:s that's missing to the mask
        num_ones = str(ones_for_mask).count("1")  # Counts the amount of ones in the subnet mask
        num_zeros = 32 - int(num_ones)  # calculate the amount of zeros needed by taking 32-the amount of ones in subnet
        # mask
        subnet_mask_binary = ones_for_mask + num_zeros * "0"  # adds the zeros to the subnet mask, so we got a real SM
        print()

        mask_zero_str = calculate_subnet_mask(subnet_mask_binary).count("0")
        num_hosts = int(2 ** int(mask_zero_str))

        # PRINTS
        print(f"Binary: {calculate_ip_binary(ip_spl)}")  # Converts ip to binary and prints it
        print(f"Mask:   {calculate_subnet_mask(subnet_mask_binary)}")  # prints the mask in binary
        print(f"\nNumber of Hosts: {num_hosts}")
        print(f"Number of Usable Hosts: {(int(num_hosts - 2))}")

        """BROADCAST"""
        ip_spl, mask_spl = ip.split("/", 1)
        ip_binary = ''.join([bin(int(x) + 256)[3:] for x in ip_spl.split('.')])

        # Calculate the inverted subnet mask
        inverted_mask_binary = ''.join('1' if bit == '0' else '0' for bit in ''.join(
            [bin(int(x) + 256)[3:] for x in ('255.255.255.255' if mask_spl == '32' else '255.255.255.0').split('.')]))

        # Calculate broadcast IP address
        broadcast_ip_binary = calculate_broadcast_ip(ip_binary, subnet_mask_binary)

        """SUB ID & BROADCAST IP"""
        subnet_id = calculate_subnet_id(ip_binary, ''.join(subnet_mask_binary))
        # broadcast_ip_decimal = '.'.join([broadcast_ip_binary[i:i + 8] for i in range(0, len(broadcast_ip_binary), 8)])
        broadcast_ip_dec = '.'.join(
            [str(int(broadcast_ip_binary[i:i + 8], 2)) for i in range(0, len(broadcast_ip_binary), 8)])
        # Output the broadcast IP address
        print("Subnet ID:", subnet_id, f"\nBroadcast IP: {broadcast_ip_dec}")

        """IP RANGE"""
        ip_range = [calculate_subnet_id(ip_binary, ''.join(subnet_mask_binary)),
                    calculate_broadcast_ip(ip_binary, inverted_mask_binary)]  # Calculate the IP range
        ip_range[0] = ip_range[0].split('.')  # Split the IP range into two lists
        ip_range[1] = ip_range[1].split('.')  # Split the IP range into two lists
        ip_range[0][3] = str(int(ip_range[0][3]) + 1)  # Increment the starting IP address by 1
        ip_range[0] = '.'.join(ip_range[0])  # Join the starting IP address back together
        ip_range[1] = '.'.join(ip_range[1])  # Join the ending IP address back together

        last_available_ip_binary = calculate_last_available_ip(ip_binary.replace('.', ''),
                                                               subnet_mask_binary.replace('.', ''))

        last_available_ip_decimal = '.'.join(
            [str(int(last_available_ip_binary[i:i + 8], 2)) for i in range(0, len(last_available_ip_binary), 8)])

        print(f"IP range: {ip_range[0]} - {last_available_ip_decimal}\n")  # Output the IP range

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

