import requests
url = input("enter the url of the site you want to GET:")
proxies = {
        'http':'socks5://127.0.0.1:9050',
        'https':'socks5://127.0.0.1:9050'
        }
get = requests.get(url,proxies = proxies)
get = get.text
if "You are not using Tor." in get:
    print("you are not using tor")
else:
    print("you are using tor")