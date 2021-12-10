'''PythonSockets.py:
This program utilizes python sockets and threading to execute a simple server-client connection.
The overrall purpose is to simply show how a basic connection can be utilized. 
'''

import socket
import threading


def repeater():
    '''Create a simple client that multiplies a number by itself'''

    # Setup client socket and connect to server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 7777))
    
    # Define default iterator value for while loop
    iterator = 2

    # Keep looping until the iterator value is greater that 10000000
    while iterator < 10000000:

        # Send simple data with the current value of iterator
        client.sendall(bytes('Iterator: {}\n'.format(iterator), 'utf-8'))

        # Multiplie iterator by itself and reassign it to the new value
        iterator *= iterator

 # Define the main function that will execute the server.
def main():
    # Setup server socket and bind it on local host using port 7777
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 7777))

    # Setup server listener before execute client
    server.listen()
    
    # Run client function as a thread so it can run in the background while the server waits.
    execute_client = threading.Thread(target=repeater(), daemon=True)
    execute_client.start()
    
    # Accept the connection from the client
    conn, addr = server.accept()
   
    # Keep displaying the data to the screen as a string, until there is no more data
    while True:
        data = conn.recv(1024)
        print(data.decode()) # Decode it to remove the b'' part of the output
        
        # Leave the loop once there is no more data being sent.
        if data == b'':
            break
    # Wait to ensure the client thread closes before ending the application.
    execute_client.join()
    # Close the socket before closing the application.
    server.close()

if __name__ == '__main__':
    main()