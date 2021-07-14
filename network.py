import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 5555
        self.server = socket.gethostname()
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def getpos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))

        except:
            pass

    def send(self, data):
        try:
            msg = pickle.dumps(data)

            return self.client.send(msg)

        except socket.error as e:
            print(e)


