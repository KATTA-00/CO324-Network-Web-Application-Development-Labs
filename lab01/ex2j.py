from urllib import request

# GET request 
with request.urlopen("https://duckduckgo.com/?q=Rocco%27s+basilisk") as query:

    body = query.read()
    
    # print body
    print(body)