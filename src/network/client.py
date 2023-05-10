import requests

session_id = -1

def connect():
	url = "http://127.0.0.1:5000/connect"
	req = requests.get(url=url)
	if(req.ok):
		global session_id 
		session_id = req.json()['session_id']

def draw_card():
	url = "http://127.0.0.1:5000/drawcard"
	req = requests.post(url=url, json={'session' : session_id})
	if(req.ok):
		return req.json()['card']

#Test
print("test connect")
print(draw_card())
connect()
print(session_id)
print("tets draw_card")
print(draw_card())

