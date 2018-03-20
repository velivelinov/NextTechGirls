import api_functions

# Ask the user for input for what city to search for
city = raw_input("What city would you like to find information about? ")

response_data = api_functions.make_request(city)

# Ask the user for what information they'd like to find out
print('Would you like to find out: ')
print('1. Information about the city')
print('2. Coordinates of the city')
print('3. The country the city is in')
choice = raw_input("What option have you chosen? ")

# Make a decision based on the choice
if choice == '1':
    print(response_data['results'][0]['intro'])
elif choice == '2':
    print(response_data['results'][0]['coordinates'])
elif choice == '3':
    print(response_data['results'][0]['country_id'])
else:
    print('You have not entered a correct menu option.')
