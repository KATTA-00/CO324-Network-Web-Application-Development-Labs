from urllib import request

def last_modified(url):
    '''Returns the Last-modified header for the URL or None if it doesn’t exist.'''
    
    # Make a request to the URL
    with request.urlopen(url) as query:
        headers = query.headers.items()

        # Iterate over the headers
        for header in headers:
            # Check if the header is "Last-Modified"
            if header[0] == "Last-Modified":
                # Print the Last-Modified header and break the loop
                print(header)
                break
        else:
            # If no Last-Modified header is found, return None
            return None


last_modified("https://www.geeksforgeeks.org/http-headers-last-modified")
