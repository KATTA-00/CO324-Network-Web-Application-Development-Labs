# import modules
from urllib import request

# GET request 
with request.urlopen("https://www.duckduckgo.com/?q=University+of+Peradeniya&format=json&pretty=1") as query:

    body = query.read()
    # print body
    print(body)