import pymongo


#gets you the handler on the mongo client
client = pymongo.MongoClient()
#choose the data base
db = client.Surveys
#choose the collection
collection = db.usersurveystemp
#example code
def InsertDummyRecords():
	collection.insert({"driverID" : "JohnD@example.com", "start_long" : "33.2991"})

def InsertNameEmail(username, email, surveyResponse, dropdown, textarea):
	collection.insert({"username" : username, "email" : email, "surveyResponse": surveyResponse,
		"dropdown": dropdown, "textarea": textarea})

def display():
	return collection
# if __name__ == "__main__":
# 	InsertDummyRecords()
