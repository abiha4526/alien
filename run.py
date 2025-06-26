import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear_screen()
    print("\033[1;32m")
    print("██████╗ ██████╗  ██████╗ ")
    print("██╔══██╗██╔═══██╗██╔════╝ ")
    print("██████╔╝██║   ██║██║  ███╗")
    print("██╔═══╝ ██║   ██║██║   ██║")
    print("██║     ╚██████╔╝╚██████╔╝")
    print("╚═╝      ╚═════╝  ╚═════╝ ")
    print()
    print("Author       : Malik Habib")
    print("WhatsApp     : +923434571018")
    print("\033[0m")
    print("="*50)
    print()

banner()
