import datetime

MOCK_USERS = [{"email": "test@example.com", "salt":"456", "hashed": "ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413"}]

MOCK_TABLES = [{"__id":"1", "number": "1", "owner":"test@example.com","url":"mockurl"}]

MOCK_REQUESTS = [{"__id":"1", "table_number":"1", "table_id" : "1", "time" : datetime.datetime.now()}]

class MockDBHelper:
	def get_user(serlf, email):
	  user = [ x for x in MOCK_USERS if x.get("email") == email]
	  if user:
		return user[0]
	  return None

	def add_user(self, email, salt, hashed):
		MOCK_USERS.append({"email": email, "salt": salt, "hashed": hashed})


	def add_table(self, number, owner):
		MOCK_TABLES.append({"__id":number, "number":number, "owner":owner})
		return number 
	
	def update_table(self, __id, url):
		print (url, __id)
		for table in MOCK_TABLES:
			if table.get("__id") == __id :
				table["url"] = url
		   		break

	def get_tables(self, owner_id):
		return MOCK_TABLES

	def delete_table(self, table_id):
		for i, table in enumerate(MOCK_TABLES):
			if table.get("__id") == table_id:
				del MOCK_TABLES[i]
				break


	def get_requests(self, owner_id):
		return MOCK_REQUESTS

	def delete_request(self, request_id):
		for i, request in enumerate(MOCK_REQUESTS):
			if request.get("__id") == request_id:
				del MOCK_REQUESTS[i]
				break


	def add_request(self, table_id, time):
		table = self.get_table(table_id)
	 	try:
			self.db.requests.insert({"owner": table['owner'], "table_number": table['number'], "table_id": table_id, "time": time})
			return True
	 	except pymongo.errors.DuplicateKeyError:
			return False

	def add_table(self, number, owner):
		MOCK_TABLES.append({"__id":str(number), "number":number, "owner":owner})
		return number 
	

