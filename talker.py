import sys
import json

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

class Reader(Master):
	"""This class reads information from the port"""
	def __init__(self, host, port):
		super(Reader, self).__init__(host, port)

	def getElementById(self, id):
		print(id)
		# construct URL
		# use requests to send it over

	def saveElementById(self, id, filename):
		print(id)
		print(filename)

	# def readFile(self, file):
	# 	print(file)
	# 	js = open(file, 'r')

	# 	jsonStr = ""
	# 	for line in js.readlines():
	# 		jsonStr+=line.strip()

	# 	return self.readString(jsonStr)

	# def readString(self, jsonStr):
	# 	data = json.loads(jsonStr)
	# 	return data

class Writer(Master):
	"""This class sends information over to the server"""
	def __init__(self, host, port):
		super(Writer, self).__init__(host, port)

	def postElementFromFile(self, filename):
		print(filename)

if __name__ == '__main__':
	reader = Reader("host", "port")
	reader.getElementById("1800")
	reader.saveElementById("1800", "sample.json")

	writer = Writer("host", "port")
	writer.postElementFromFile("sample.json")





