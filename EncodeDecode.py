                                        # hash Encoding and Decoding Tool
import hashlib
import base64
from colorama import Fore, Style, init
import os

# Initialize colorama
init(autoreset=True)

# ASCII banner with colors
def display_banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = f"""
{Fore.GREEN}{"="*45}
{Fore.CYAN}    HASH ENCODING AND DECODING TOOL v1.0
{Fore.GREEN}{"="*45}
{Style.RESET_ALL}
{Fore.YELLOW}    Created by: Shivansh Mishara
{Fore.BLUE}    GitHub: https://github.com/MishraShivansh24
{Fore.GREEN}{"="*45}{Style.RESET_ALL}
"""
    print(banner)


# Function to hash input data using hashlib algorithms
def hash_encode(input_string, algorithm):
    try:
        if algorithm == "md5":
            return hashlib.md5(input_string.encode()).hexdigest()
        elif algorithm == "sha1":
            return hashlib.sha1(input_string.encode()).hexdigest()
        elif algorithm == "sha256":
            return hashlib.sha256(input_string.encode()).hexdigest()
        elif algorithm == "sha512":
            return hashlib.sha512(input_string.encode()).hexdigest()
        elif algorithm == "base64":
            return base64.b64encode(input_string.encode()).decode()
        else:
            print(Fore.RED + "Invalid algorithm. Supported: md5, sha1, sha256, sha512, base64")
            return None
    except Exception as e:
        print(Fore.RED + f"Error in encoding: {e}")
        return None


# Function to decode Base64 (example of decoding)
def base64_decode(input_string):
    try:
        decoded_data = base64.b64decode(input_string).decode()
        return decoded_data
    except Exception as e:
        print(Fore.RED + f"Error in decoding Base64: {e}")
        return None


# Stylish menu with colors
def display_menu():
    print(Fore.CYAN + "Choose an option:")
    print(Fore.YELLOW + "1. " + Fore.GREEN + "Encode (Hash)")
    print(Fore.YELLOW + "2. " + Fore.GREEN + "Decode (Base64 Only)")
    print(Fore.YELLOW + "3. " + Fore.RED + "Exit")
    print(Fore.GREEN + "-" * 50)


# Main function with user options
def main():
    display_banner()
    while True:
        display_menu()
        choice = input(Fore.CYAN + "Enter your choice: ")

        if choice == "1":
            input_string = input(Fore.CYAN + "Enter the string to encode: " + Fore.WHITE)
            print(Fore.CYAN + "Available algorithms: " + Fore.YELLOW + "md5, sha1, sha256, sha512, base64")
            algorithm = input(Fore.CYAN + "Enter the algorithm to use: ").lower()
            result = hash_encode(input_string, algorithm)
            if result:
                print(Fore.GREEN + f"Encoded Result ({algorithm.upper()}): {Fore.WHITE}{result}")

        elif choice == "2":
            encoded_string = input(Fore.CYAN + "Enter the Base64 encoded string to decode: " + Fore.WHITE)
            result = base64_decode(encoded_string)
            if result:
                print(Fore.GREEN + f"Decoded Result: {Fore.WHITE}{result}")

        elif choice == "3":
            print(Fore.RED + "Exiting... Goodbye!")
            break

        else:
            print(Fore.RED + "Invalid choice. Please try again.")

        print(Fore.MAGENTA + "-" * 50)


if __name__ == "__main__":
    main()
