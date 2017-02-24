class Parser(object):
	"""This class makes many get requests and parses the data"""
	def __init__(self, talker, site):
		super(Parser, self).__init__()
		self.talker = talker
		self.site = site

	def getElement(self, idd):
		return self.talker.getElementById(self.site, idd)

	def getTable(self, idd, site = 'restful'):
		tableJSON = self.talker.getElementById(self.site, idd)
