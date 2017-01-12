import json, requests

movieTitle = input("Enter a movie to search for:")

# getting the url for the movie
try:
    url = "http://www.omdbapi.com/?"

except ConnectionError:
    print("Website unreachable")


parameters = dict(
    t=movieTitle
)

omdbResponse = requests.get(url=url, params=parameters)
# getting the response

# getting the text from the request
rating = json.loads(omdbResponse.text)
# printing the results
print("Rating for", rating["Title"], rating['imdbRating'])
