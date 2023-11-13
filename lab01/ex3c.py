from urllib import request
import requests

def last_modified(url):

    '''Returns the Last-modified header for the URL or None if it doesn’t exist.'''

    # Make a request to the URL using HEAD method
    with requests.head(url) as query:
        headers = query.headers

        # Iterate over the headers
        for i in headers:
            # Check if the header is "Last-Modified"
            if i[0] == "Last-Modified":
                # Print the Last-Modified header and break the loop
                print(i)
                break
        else:
            return None


last_modified("https://en.wikipedia.org/wiki/Sri_Lanka")