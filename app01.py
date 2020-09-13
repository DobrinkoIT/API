import requests
# pip install requests
# Dobija se odziv od API endpoint-a
response = requests.get('http://api.open-notify.org/astros.json')
data = response.json()
# Broj ljudi koji su trenutno u svemiru
print(data['number'])
print(data)


# Dobija se odziv od API endpoint-a
response = requests.get('https://dog.ceo/api/breeds/list/all')
data = response.json()
print(data)
