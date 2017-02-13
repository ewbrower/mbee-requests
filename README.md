# mbee-requests

If you would like to pull down an element with id MMS_1486950811965_07307863-33d9-455d-81db-480dc27021f7
Run these commands in the mbee-requests directory in Jupyter

from talker import Talker
t = Talker("127.0.0.1","20082")
t.saveElementById("restful","MMS_1486950811965_07307863-33d9-455d-81db-480dc27021f7", "outfile.json")

If you would like to push your edits back to the server, run the following command
outfile.json contains the json you have edited

t.postElementsFromFile("outfile.json")
