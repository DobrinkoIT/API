import requests
# pip install requests
# Dobija se odziv od API endpoint-a


class APIError(Exception):
    """An API Error Exception"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: status={}".format(self.status)


resp = requests.get('https://jsonplaceholder.typicode.com/posts')
if resp.status_code != 200:
    # Ovo znaci da nesto nije kako treba
    raise APIError(resp.get('status'))
for post_stavka in resp.json():
    # stampaju se vrednosti polja id i title svih objekata dobijenih u odgovoru
    print('{} {}'.format(post_stavka['id'], post_stavka['title']))


example = {'title': 'Nas prvi primer',
           'body': 'Upravo smo postavili post zahtev'}
resp = requests.post(
    'https://jsonplaceholder.typicode.com/posts', json=example)
if resp.status_code != 201:
    # Ovo znaci da nesto nije kako treba
    raise APIError(resp.post('status'))
print('Zadatak kreiran. id: {}'.format(resp.json()['id']))
