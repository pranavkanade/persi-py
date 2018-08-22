import urllib2
import re
url ="http://python.org"
#connect to a URL
website = urllib2.urlopen(url)

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

print links

"""
In Python 3 ----->
#The urllib2 module has been split across several modules in Python 3 named urllib.request
#and urllib.error
#So you should instead be saying--->

from urllib.request import urlopen
html = urlopen("http://www.google.com/")
print(html)
"""
