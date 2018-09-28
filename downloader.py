import urllib.request
import time

def download(url):
    name="bild"
    full_name=str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)
url=input("Bitte die URL eingeben:")
print("...")
time.sleep(4)
download(url)

