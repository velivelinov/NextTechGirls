import api_functions

# Ask the user for input for what city to search for
city =

response_data = api_functions.make_request(city)

# Ask the user for what information they'd like to find out
print('Would you like to find out: ')
print('1. Information about the city')
print('2. Coordinates of the city')
print('3. The country the city is in')
choice =

# Use the response_data dictionary in order to get the information needed!
# If the user's choice is 1 - use the 'intro' value
# If the user's choice is 2 - use the 'coordinates' value
# If the user's choice is 3 - use the 'country_id' value