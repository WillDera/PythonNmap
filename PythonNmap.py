import os
import subprocess


def mainMenu():
    print("."*80)
    print("\t\t\t NMAP SECURITY SCANNER")
    print("."*80)
    print("\t\t\t1---> Host Discovery")
    print("\t\t\t2---> OS Discovery")
    print("\t\t\t3---> Port Discovery")
    print("\t\t\t4---> Port Discovery In Range")
    print("\t\t\t5---> Clear The Terminal")
    print("\t\t\t6---> Quit Program")
    print()
    choice = int(input("Select An Option: "))
    if choice == 1:
        Host_Discovery()
        mainMenu()
    elif choice == 2:
        Os_Discovery()
        mainMenu()
    elif choice == 3:
        Port_Discovery()
        mainMenu()
    elif choice == 4:
        Port_DiscoveryInRange()
        mainMenu()
    elif choice == 5:
        clear()
        mainMenu()
    elif choice == 6:
        clear()
        quit()
    else:
        print("Invalid Choice")
        mainMenu()


def Host_Discovery():
    host = input("[*] Enter Host Address: ")
    print("."*50)
    subprocess.check_call(['nmap', '-n', '-V', '-Pn', '-sn',
                           '-sL', '-PE', '-PP', host])
    print("."*50)


def Os_Discovery():
    os = input("[*] Enter Host Address to scan: ")
    print("."*50)
    subprocess.check_call(
        ['nmap', '-n', '-F', '-A', '-Pn', '-sS', '-O', '-oN', 'OS_Discovery.txt', os])
    print("."*50)


def Port_Discovery():
    port = input("[*] Enter Host Address to scan: ")
    print("."*50)
    subprocess.check_call(
        ['nmap', '-n', '-V', '-Pn', '-sV', '-oN', 'Port_Discovery.txt', port])
    print("."*50)


def Port_DiscoveryInRange():
    port_range = input("[*] Enter Host Address to scan: ")
    print("."*50)
    subprocess.check_call(['nmap', '-p', '1-100', '-oN',
                           'Port_DiscoveryInRange.txt', port_range])
    print("."*50)


def clear():
    os.system('cls||clear')


def quit():
    quit()


if __name__ == '__main__':
    mainMenu()
