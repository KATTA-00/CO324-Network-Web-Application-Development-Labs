from urllib import request

with request.urlopen("https://www.duckduckgo.com/?q=කණිෂ්ක") as query:

    headers = query.headers.items()

    body = query.read()

    print(body)