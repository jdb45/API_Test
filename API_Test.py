import json, requests

# getting the user for the movie
try:
    url = "http://www.omdbapi.com/?t=star wars"

except ConnectionError:
    print("Website unreachable")
# getting the response
omdbResponse = requests.get(url)
# getting the text from the request
rating = json.loads(omdbResponse.text)
# printing the results
print("Rating for Star Wars", rating['imdbRating'])