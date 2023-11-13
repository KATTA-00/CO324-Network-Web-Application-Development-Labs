from urllib import request
import json

def ddg_query(search_term, nr_results):
    '''Extracts the top ‘nr_result’ number of URLs from the response.

    Returns extracted URLs as a list.'''

    # Replace spaces in the search term with '+'
    query = search_term.replace(" ", "+")

    # Make a request to the DuckDuckGo API with the formatted query
    with request.urlopen("https://www.duckduckgo.com/?q=" + query + "&format=json&pretty=1") as query:
        # Read the response body
        body = query.read()

        # Parse the response body as JSON
        jsonBody = json.loads(body)

        arr = []

        # Check if the number of results is less than nr_results
        if len(jsonBody["Results"]) < nr_results:
            nr_results = len(jsonBody["Results"])

        # Iterate over the top nr_results results and extract the URLs
        for i in range(nr_results):
            arr.append(jsonBody["Results"][i]["FirstURL"])

        return arr

# Search for "University of Peradeniya" and 1 URL
print(ddg_query("University of Peradeniya", 1))
