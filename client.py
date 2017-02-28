import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    socClnt = socket.socket()
    socClnt.connect((host, port))
    msg = raw_input("=>")
    while msg != 'q':
        socClnt.send(msg)
        data = socClnt.recv(1024)
        print "recieved from server: " + str(data)
        msg = raw_input("=>")

    socClnt.close()



if __name__ == '__main__':
    Main()
