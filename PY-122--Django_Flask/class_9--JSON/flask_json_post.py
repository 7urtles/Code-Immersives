import requests

def get_some_json():
	request_url = 'http://136.34.32.221:5007/'
	argument = 'charles/post'
	response = requests.post(request_url+argument).json()
	return response

post_response = get_some_json()
print(post_response)