import requests
import sys
import json
from talker import Talker
from IPython.display import HTML, display

class Parser(object):
	"""This class makes many get requests and parses the data"""
	def __init__(self, talker, site):
		super(Parser, self).__init__()
		self.talker = talker
		self.site = site

	def getElement(self, idd):
		return self.talker.getElementById(self.site, idd)

	def getTable(self, idd):
		# tableJSON = self.talker.getElementById(self.site, idd)
		table = self.talker.getElementById(self.site, idd)
		table = json.dumps(table)
		data = json.loads(table)

		#categories = data["elements"][0]["documentation"][50]
		#this is where I would print category names but right now it's just one long string
		#so going to find a more efficient means of parsing

		itemArray = data["elements"][0]["specialization"]["displayedElements"]
		itemArray.pop() #because the last element is a reference to the table itself

		numValueList = []
		titleValueList = []
		for item in itemArray:
		    value = self.talker.getElementById(self.site, item)
		    value = json.dumps(value)
		    valueData = json.loads(value)
		    valueData1 = Value(valueData)#this is jenk and inefficient but will fix later
		    if valueData1.isNumeric():
		        numValueList.append(Number(valueData))
		    else:
		        titleValueList.append(Title(valueData))

		#this is where it gets very hard coded to this case
		sortedTitles = sorted(titleValueList, key = lambda title: title.iD)
		sortedNums = sorted(numValueList, key = lambda num: num.iD)

		place = 0

		# for title in sortedTitles:
		# 	print(title.title, ' - ', sortedNums[place].num, ' - ', sortedNums[place + 1].num)
		# 	place = place + 2

		tableHTML = "<table>"
		col = '</td><td>'
		for title in sortedTitles:
			tableHTML+='<tr><td>' + title.title + col + str(sortedNums[place].num) + col 
				+ str(sortedNums[place + 1].num) + '</td></tr>'
		tableHTML += '</table>'
		display(HTML(tableHTML))


		# display(HTML(
		# 	'<table><tr>{}</tr></table>'.format(
		# 		'</tr><tr>'.join(
		# 			'<td>{}</td>'.format('</td><td>'.join(str(_) for _ in title)) for title in sortedTitles)
		# 		)
		# 	))

class Value(object):
    def __init__(self, arg):
        self.value = arg
    #this may not be fair to assume that lengths will always be 3 or 5, but worked in this case
    def isNumeric(self):
        return len(self.value["elements"][0]["specialization"]) > 3
    def isName(self):
        return len(self.value["elements"][0]["specialization"]) < 5
    #gets name or number depending on type based on above assumptions
    def getName(self):
        return self.value["elements"][0]["name"]
    def getNumber(self):
        return self.value["elements"][0]["specialization"]["value"][0]["double"]

class Number(object):
    iD = ""
    num = 0

    def __init__(self, arg):
        self.iD = arg["elements"][0]["sysmlid"]
        self.num = arg["elements"][0]["specialization"]["value"][0]["double"]

class Title(object):
    iD = ""
    title = ""

    def __init__(self, arg):
        self.iD = arg["elements"][0]["sysmlid"]
        self.title = arg["elements"][0]["name"]

class Line(object):
    title = ""
    column1 = ""
    column2 = ""

    def __init__(self, title, column1, column2):
        self.title = title
        self.column1 = column1
        self.column2 = column2
