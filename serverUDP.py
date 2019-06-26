from socket import *
import time
import struct
import sys

def startServer(serverPort):
    # AF_INET: using IPv4
    # SOCK_DGRAM: for UDP, SOCK_STREAM: for TCP
    serverSocket = socket(AF_INET, SOCK_DGRAM)

    serverSocket.bind(('', serverPort))

    print(f"Server running on port {serverPort}")

    while 1:
        message, clientAddress = serverSocket.recvfrom(2000)

# > Input arguments function

def invalidInputArgs():
    print(f"Usage: {sys.argv[0]} -p <server-port>")
    exit(1)

def getInputArgValue(key, argName):
    try:
        return sys.argv[sys.argv.index(key)+1]
    except (ValueError, IndexError) as error:
        print("Missing argument:", argName)
        invalidInputArgs()

def getInputArgs():
    args = {}
    argKeys = {
        "-p": "server port",
    }
    
    for key, name in argKeys.items():
        args[key] = getInputArgValue(key, name)

    # Convert 'port' from String to Int
    args["-p"] = int(args["-p"])
    
    return args

if __name__ == "__main__":
    args = getInputArgs()
    startServer(serverPort = args["-p"])