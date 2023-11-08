from urllib import request

with request.urlopen("https://www.duckduckgo.com/?q=University+of+Peradeniya&format=json&pretty=1") as query:

    headers = query.headers.items()

    body = query.read()

    print(body)