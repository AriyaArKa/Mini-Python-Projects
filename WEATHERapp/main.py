import requests


city = input("enter the name of the city\n")

url = f""

r = requests.get(url)
print(r.text)