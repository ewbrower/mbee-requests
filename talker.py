import requests
import sys
import json
from getpass import getpass

class MBEESession(requests.Session):
	"""This is a requests Session object built for connecting to MBEE"""

	def __init__(self, host, port = None):
		super(MBEESession, self).__init__()
		print("Running with Python " + str(sys.version_info.major) 
			+ "." + str(sys.version_info.minor) + "\n")
		# establish the baseURL for this (don't need port all the time, always host)
		self.baseURL = host + ":" + port if port else host
		# store the user auth for use in the get and post functions
		self.authenticate()

	def authenticate(self):
		print("Please enter your username and password")
		username = input("Username: ")
		password = getpass("Password: ")
		self.auth = (username, password)

	def getBaseURL(self):
		return self.baseURL

# class Master(object):
# 	"""This is the master class that holds the connection to the MBEE server"""
# 	def __init__(self, host, port):
# 		self.host = host
# 		self.port = port
# 		print("Running with Python " + str(sys.version_info.major) 
# 			+ "." + str(sys.version_info.minor) + "\n")
# 		self.sesh = requests.Session()
# 		self.sesh.auth = self.authenticate()
# 		print("did it: " + str(self.sesh.auth))
# 		self.connect()

# 	def authenticate(self):
# 		print("Please enter username and password")
# 		username = input("Username: ")
# 		password = getpass.getpass("Password: ")
# 		return (username, password)

# 	def connect(self):
# 		print("Connecting user " + self.sesh.auth[0] + " to database.")

# 	def getBaseURL(self):
# 		return "http://" + self.host + ":" + self.port + "/alfresco/service"

class Talker(MBEESession):
	"""This is the class that combines read and write to database methods"""
	def __init__(self, host, port= None):
		super(Talker, self).__init__(host, port)

	def help(self):
		print("Here are the functions available:\ngetElementById(site, id)"
			+ "\nsaveElementById(site, id, file)\npostElementFromFile(id, file)")

	def getElementById(self, site, idd):
		# print(idd)
		# construct URL
		# use requests to send it over
		url = self.getBaseURL() + "/workspaces/master/sites/" + site + "/elements/" + idd
		return url

	def saveElementById(self, site, idd, filename):
		url = self.getElementById(site, idd)
		return url

	def postElementFromFile(self, idd, filename):
		print(filename)





