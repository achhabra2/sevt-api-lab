import json
import requests


myToken="Bearer TOKEN"
myRoom="ROOM"
myRoomName="Aman API Test"
myEmail="EMAIL"
myMessage="Test API Message"


def get_rooms(mytoken):
   # The header is send to authenticate
   header = {'Authorization':mytoken, 'content-type':'application/json; charset=utf8'}
   # Send GET request with above header, put result in ‘result’
   result = requests.get(url='https://api.ciscospark.com/v1/rooms',headers=header)
   # Encode ‘result’ as JSON
   JSONresponse = result.json()
   # Create an Array for all rooms: ('room1','room2','room3')
   roomlist_array = []
   # For each item in the JSON data
   for EachRoom in JSONresponse['items']:
       # add the ‘title’ to the roomlist_array
       roomlist_array.append(EachRoom.get('title'))
   # Return the list of members
   return roomlist_array


# Execute get_rooms and put result in ‘SparkResult’
SparkResult = get_rooms(myToken)
# Loop through the ‘SparkResult’ array
for room in SparkResult:
    # print room name
    print ("> Room:", room)
# Print the number of rooms (length of SparkResult array)
print ("----- TOTAL Room Count:", len(SparkResult))
