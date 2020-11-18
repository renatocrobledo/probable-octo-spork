import requests


def get_url(url):
    return requests.get(url).json()


response = get_url('https://reqres.in/api/users')

for n in response['data']:
    print(n['first_name'])


