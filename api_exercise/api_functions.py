import httplib
import json

def make_request(city):
    connection = httplib.HTTPSConnection('www.triposo.com', 443)
    authentication = '&account=PWE7UQ9X&token=933zftq6hh6xg7axq3ttfes2vywk3ywh'

    connection.request('GET',
                       '/api/20180223/location.json?id=' + city + '&fields=id,name,intro,country_id,coordinates' + authentication)
    response = connection.getresponse()
    response_data = json.loads(response.read())
    return response_data