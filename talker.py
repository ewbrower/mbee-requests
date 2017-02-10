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

	def getBaseURL(self):
		return "http://" + self.host + ":" + self.port + "/alfresco/service/"

class Reader(Master):
	"""This class reads information from the port"""
	def __init__(self, host, port):
		super(Reader, self).__init__(host, port)

	def getElementById(self, site, idd):
		# print(idd)
		# construct URL
		# use requests to send it over
		url = self.getBaseURL() + "/workspaces/master/sites/" + site + "/elements/" + idd
		return url

	def saveElementById(self, site, idd, filename):
		url = self.getElementById(site, idd)
		return url


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
	print("work pls")
	print(reader.getElementById("master", "1800"))
	print(reader.saveElementById("master", "1800", "sample.json"))

	writer = Writer("host", "port")
	writer.postElementFromFile("sample.json")





