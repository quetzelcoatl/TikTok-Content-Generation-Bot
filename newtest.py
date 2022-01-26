import time

class renderr():
    import socket

# Create a s ocket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection
s.close()


     file = open("progressbar.txt", "w")
     file.write("10\n")
     file.close()
     time.sleep(1)
     file = open("progressbar.txt", "w")
     file.write("10\n")
     file.close()
     time.sleep(1)
     file = open("progressbar.txt", "w")
     file.write("10\n")
     file.close()
     time.sleep(1)
     file = open("progressbar.txt", "w")
     file.write("10\n")
     file.close()
     time.sleep(1)
     file = open("progressbar.txt", "w")
     file.write("10\n")
     file.close()
     time.sleep(1)
     file = open("progressbar.txt", "w")
     file.write("EOF")
     file.close()

renderr()
