import sys
import socket

class Client():

    def __init__(self):
        self.client_socket = socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM,
                    socket.IPPROTO_IP)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    def run(self, message):
        #self.server_socket.bind((socket.gethostbyname(socket.gethostname()), 50000))
        self.client_socket.connect(("127.0.0.1", 5000))
        message.encode('utf-8')
        self.client_socket.sendall(message)
        self.client_socket.shutdown(socket.SHUT_WR)
        data_receive = ""
        while 1:
            data = self.client_socket.recv(32)
            data_receive = data_receive + data
            if len(data) < 32:
                return data_receive
                break
        print data_receive
        self.client_socket.close()
        #return data_receive#.decode('utf-8')

if __name__=="__main__":
    client=Client()
    print client.run("GET {} HTTP/1.1\r\n\r\n".format("/edit/2"))