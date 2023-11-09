from urllib import request
import json

def last_modified(url):

    '''Returns the Last-modified header for the URL or None if it doesn’t exist.'''


    with request.urlopen(url) as query:

        headers = query.headers.items()

        for i in headers:
            if i[0] == "Last-Modified":
                print(i)
                break
        else:
            return None



last_modified("https://www.geeksforgeeks.org/http-headers-last-modified")