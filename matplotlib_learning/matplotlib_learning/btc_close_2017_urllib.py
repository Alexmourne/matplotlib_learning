from __future__ import (absolute_import, division, 
                        print_function, unicode_literals)

try:
    #python 2.x
    from urllib2 import urlopen
except ImportError:
    # Python 3.x
    from urllib.request import urlopen
import json

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)
#
req = response.read()
#
with open('btc_close_2017_urllib.json', 'wb') as f:
    f.write(req)
#
file_urllib = json.loads(req)
print(file_urllib)
