from urllib import request
import requests

def last_modified(url):

    '''Returns the Last-modified header for the URL or None if it doesn’t exist.'''


    with requests.head(url) as query:

        headers = query.headers

        for i in headers:
            if i[0] == "Last-Modified":
                print(i)
                break
        else:
            return None



last_modified("https://en.wikipedia.org/wiki/Sri_Lanka")