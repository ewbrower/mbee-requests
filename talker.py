import requests
import sys
import json
from getpass import getpass

class MBEESession(requests.Session):
	'''This is a requests Session object built for connecting to MBEE'''

	def __init__(self, host, port = None):
		super(MBEESession, self).__init__()
		print('Running with Python ' + str(sys.version_info.major) 
			+ '.' + str(sys.version_info.minor) + '\n')
		# establish the baseURL for this (don't need port all the time, always host)
		self.baseURL = 'http://' + host + (':' + port if port else '') + '/alfresco/service'
		# establish authentication for the session
		print('Please enter your username and password')
		username = input('Username: ')
		self.auth = requests.auth.HTTPBasicAuth(username, getpass('Password: '))
		self.headers.update({'content-type' : 'application/json'})

	def getBaseURL(self):
		return self.baseURL

class Talker(MBEESession):
	'''This is the class that combines read and write to database methods'''
	def __init__(self, host, port= None):
		super(Talker, self).__init__(host, port)

	def help(self):
		print('Here are the functions available:\ngetElementById(site, id)'
			+ '\nsaveElementById(site, id, file)\npostElementFromFile(id, file)')

	def getElementById(self, site, idd):
		# construct URL use requests to send it over
		url = self.getBaseURL() + '/workspaces/master/sites/' + site + '/elements/' + idd
		print(url)
		response = self.get(url)
		return response.json()

	def saveElementById(self, site, idd, filename):
		data = self.getElementById(site, idd)
		with open(filename, 'w') as outFile:
			json.dump(data, outFile, indent=4)

	def postElementsFromFile(self, filename, idd = None):
		# this function isn't going to work for more than one result
		with open(filename, 'r') as inputFile:
			data = json.load(inputFile)
		site = self.findElementSite(data['elements'][0])
		return self.postElementById(site, data)

	def postElementById(self, site, payload):
		url = self.getBaseURL() + '/workspaces/master/sites/' + site + '/elements'
		response = self.post(url, data=json.dumps(payload))
		return response

	def findElementSite(self, jData):
		site = jData['siteCharacterizationId']
		return site



