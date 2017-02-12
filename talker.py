import requests
from requests.auth import AuthBase
import sys
import json
from getpass import getpass

class MBEEAuth(AuthBase):
	"""This is the authentication class for MBEE"""
	def __init__(self):
		super(MBEEAuth, self).__init__()
		self.authenticate()

	def authenticate(self):
		print("Please enter your username and password")
		self.username = input("Username: ")
		password = getpass("Password: ")
		self.auth = (self.username, password)

	def getUsername(self):
		return self.username

class MBEESession(requests.Session):
	"""This is a requests Session object built for connecting to MBEE"""

	def __init__(self, host, port = None):
		super(MBEESession, self).__init__()
		print("Running with Python " + str(sys.version_info.major) 
			+ "." + str(sys.version_info.minor) + "\n")
		# establish the baseURL for this (don't need port all the time, always host)
		self.baseURL = "http://" + host + (":" + port if port else None) + "/alfresco/service"
		# store custom authentication for use in the get and post functions
		self.auth = MBEEAuth()

	def connect(self):
		print("Connecting " + self.getUser() + " to " + self.getBaseURL())

	def getBaseURL(self):
		return self.baseURL

	def getUser(self):
		return self.auth.getUsername()

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



