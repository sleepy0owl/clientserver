import socket

def Main():

    host = '127.0.0.1'
    port = 5000
    socServ = socket.socket()
    socServ.bind((host, port))

    socServ.listen(1)
    c, addr = socServ.accept()

    print "connected with the client "

    while True:
        data = c.recv(1024)
        if not data:
            break
        data = str(data).upper()
        print "sending: " + str(data)
        c.send(data)

    c.close()



if __name__ == '__main__':
    Main()
