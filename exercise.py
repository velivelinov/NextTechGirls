import httplib
import json


# Ask the user for input for what city to search for
city = raw_input("What city would you like to find information about? ")

connection = httplib.HTTPSConnection('www.triposo.com', 443)
authentication = '&account=PWE7UQ9X&token=933zftq6hh6xg7axq3ttfes2vywk3ywh'

connection.request('GET', '/api/20180223/location.json?id=' + city + '&fields=id,name,snippet,country_id,coordinates' + authentication)
response = connection.getresponse()
response_data = json.loads(response.read())

# Ask the user for what information they'd like to find out
information_required = raw_input("Would you like to see the country that city is in (1) or information about that city (2)? ")

# Make a decision based on the choice
if information_required == '1':
    print(response_data['results'][0]['country_id'])
elif information_required == '2':
    print(response_data['results'][0]['coordinates'])
else:
    print(response_data['results'][0]['snippet'])

connection.close()
