import sys
import json

class Reader():
	"""This thing parses json"""

	def readFile(self, file):
		print("Opening file: " + str(file))
		js = open(file, 'r')

		jsonStr = ""
		for line in js.readlines():
			jsonStr+=line.strip()

		return self.readString(jsonStr)

	def readString(self, string):
		data = json.loads(string)
		return data

class Parser(object):
	"""This thing parses MBEE Elements"""

	def __init__(self, arg):
		self.element = arg

	def getSlotValue(self):
		return self.element["specialization"]["value"][0]["double"]
		

if __name__ == '__main__':
	print("Running on Python " + str(sys.version_info.major) 
		+ "." + str(sys.version_info.minor))
	reader = Reader()
	jsonData = reader.readFile("sample.json")
	element = jsonData["elements"][0]

	parser = Parser(element)
	slotValue = parser.getSlotValue()
	print(slotValue)

