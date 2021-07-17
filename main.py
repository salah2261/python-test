import datetime
import requests, json

if __name__ == '__main__':
	# print(datetime.datetime.now())
	url = "https://api.github.com/users/%(username)s" % dict(username="salah2261")
	res = requests.get(url)

	loadeddata = json.loads(res.text)

	print(json.dumps(loadeddata, indent=4, sort_keys=True))