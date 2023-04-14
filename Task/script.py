import urllib.request
import urllib2
url = 'http://bit.ly'


fetcher = urllib2.urlopen('https://clck.ru/--?url='+url)
print(fetcher.read())
'''https://clck.ru/8JM'''