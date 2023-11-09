from urllib import request
import json

def ddg_query(search_term, nr_results):
    '''Extracts the top ‘nr_result’ number of URLs from the response.

    Returns extracted URLs as a list.'''

    query = search_term.replace(" ", "+")

    with request.urlopen("https://www.duckduckgo.com/?q=" + query + "&format=json&pretty=1") as query:
        body = query.read()

        jsonBody = json.loads(body)

        arr = []

        if len(jsonBody["Results"]) < nr_results:
            nr_results = len(jsonBody["Results"])

        for i in range(nr_results):
            arr.append(jsonBody["Results"][i]["FirstURL"])

        return arr


print(ddg_query("University of Peradeniya", 1))