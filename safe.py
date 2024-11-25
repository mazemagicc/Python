import time
import random
import os
def main():
    code = "1234"
    userin = input("[!] Enter Safe Code: ")
    if userin == code:
        print("[+] Success")
        time.sleep(0.5)
        print("+------------------+")
        print("| [1] Check money  |")
        print("| [2] Manage Safe  |")
        print("+------------------+")
        option = input("[!] Select option: ")
        if option == "1":
            clear_cli()
            time.sleep(0.2)
            print("[+] Balance:", random.randrange(100, 1000))
        elif option == "2":
            clear_cli()
            time.sleep(0.2)
            storage()
    else:
        print("[-] Try again")

def storage():
    items = []
    while True:
        print("+------------------+")
        print("| [1] Add Item     |")
        print("| [2] Remove Item  |")
        print("| [3] See Storage  |")
        print("| [4] Exit         |")
        print("+------------------+")
        arg = input("[!] Select option: ")

        if arg == "1":
            item = input("[!] Item name: ")
            items.append(item)
            print("[+] Item added")
            time.sleep(1.5)
            clear_cli()
        
        elif arg == "2":
            item = input("[+] Select item to remove: ")
            if item in items:
                items.remove(item)
                print("[+]", item, "removed")
                time.sleep(1.5)
                clear_cli()
            else:
                print("[-] Item not in list")    
    
        elif arg == "3":
            print("[+] Storage: ")
            display_items_in_box(items)
            input("\n[!] Press enter to return")
            clear_cli()

        elif arg == "4":
            print("[+] Exiting")
            time.sleep(0.1)
            break

def display_items_in_box(items):
    if not items:
        print("+------------------+")
        print("|   No items found |")
        print("+------------------+")
    else:
        max_length = max(len(item) for item in items)
        print("+" + "-" * (max_length + 2) + "+")
        
        for item in items:
            print(f"| {item.ljust(max_length)} |")
        
        print("+" + "-" * (max_length + 2) + "+")

def clear_cli():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    main()
