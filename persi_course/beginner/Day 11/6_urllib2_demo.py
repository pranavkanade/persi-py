import urllib2
req = urllib2.Request('https://www.python.org/')
response = urllib2.urlopen(req)
the_page = response.read()
print the_page





"""

>set HTTP_proxy=http://ptbc1.persistent.co.in:8080/
>set HTTPS_proxy=https://ptbc1.persistent.co.in:8080/



set HTTP_PROXY=http://sakshi_jamgaonkar:password@ptbc1.persistent.co.in:8080







"""
