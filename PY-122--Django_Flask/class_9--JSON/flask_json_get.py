import requests

def get_some_json():
	response = requests.get('http://136.34.32.221:5007/get_users').json()
	return response

get_response = get_some_json()
print(get_response)