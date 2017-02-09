import sys
import requests

class Master(object):
	"""This is the master class that holds the connection to the MBEE server"""

	def __init__(self, host, port):
		self.host = host
		self.port = port
		print(str(sys.version_info.major) + "." + str(sys.version_info.minor))
		self.authenticate()

	def authenticate(self):
		print("Please enter username and password")

	def connect(self):
		print("connecting")

if __name__ == '__main__':
	m = Master("this", "that")
	print("running")