from urllib import request

with request.urlopen("https://duckduckgo.com/?q=Rocco%27s+basilisk") as query:

    body = query.read()

    print(body)