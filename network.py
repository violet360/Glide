import socket
import pickle

class Network:
	def __init__(self): #constructor
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server = socket.gethostname()
		self.port = 5555
		self.addr = (self.server, self.port)
		self.LIST= self.Connect() #self.LIST = [player1, peg]
		self.p = self.LIST[0]
		self.peg = self.LIST[1]

	def getP(self):
		return self.p

	def getPeg(self):
		return self.peg

	def Connect(self): 
		try:
			self.client.connect(self.addr) #connects with the server
			print("mark")
			return pickle.loads(self.client.recv(2048)) #receives a list of player1 object and peg from the server
		except:
			print("************")
			pass

	def send(self, data):
		try:
			self.client.send(pickle.dumps(data)) #sends the [player1, peg] to the server
			return pickle.loads(self.client.recv(2048)) # receives [player2, peg]
		except socket.error as e:
			print(e)
