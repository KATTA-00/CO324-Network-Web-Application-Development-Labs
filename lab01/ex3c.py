from urllib import request

def last_modified(url):
    '''Returns the Last-modified header for the URL or None if it doesn’t exist.'''
    
    # Make a HEAD request to the URL
    with request.urlopen(request.Request(url, method="HEAD")) as response:
        headers = response.headers
        
        # Iterate over the headers
        for key, value in headers.items():
            # Check if the header is "Last-Modified"
            if key == "Last-Modified":
                # Print the Last-Modified header and break the loop
                print(key, value)
                break
        else:
            return None

last_modified("https://en.wikipedia.org/wiki/Sri_Lanka")
