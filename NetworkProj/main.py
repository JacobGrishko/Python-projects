from server import server_main
from client import create_client


def start():
    print("Hello, welcome to the network.")
    print("1. Create new server")
    print("2. Connect as a client")
    print("3. exit.")
    choice = input(">")

    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            server_main()
        elif choice == 2:
            print("To what ip would you like to connect?")
            ip = input(">")
            create_client(ip)
        elif choice == 3:
            exit()
        else:
            print("Choose one of the presented options please.")
            start()
    else:
        print("Incorrect input, please try again")
        start()


start()
