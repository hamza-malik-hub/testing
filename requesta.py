import requests
url="https://anvil.works/learn/examples/simple-website-guide"
response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
