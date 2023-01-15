#! /bin/python3

import requests, json

url = "https://social-scanner.p.rapidapi.com/social-scan/"

u = input("Enter Username:")
t = int(input("Enter target count 1-25:"))

print ("_________________________________________")
payload = "username={}&target_count={}".format(u, t)
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "488fbe0951msha2ad26556913035p18f2b7jsna8a5a9eb1c9b",
	"X-RapidAPI-Host": "social-scanner.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)


jsonFile = open("data.json", "w")
jsonFile.write(respnse.text)
jsonFile.close()

jsonFile = open("data.json", "r")

values = json.load(jsonFile)

for i in value['detected']:
	print(i['link'])
	
print ("_________________________________________")
website = "http://"+u+".com"

def website_check(website)
	try:
		get = requests.get(website)
		if get.status_code == 200:
			print(website,"is a hit.")
		else:
			print(website, "is not a website.")
	except requests.ConnectionError as e:
		print(website, "is not a website.")
			
website_check(website)
