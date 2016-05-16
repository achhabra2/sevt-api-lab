import json
import requests

myToken="Bearer TOKEN"
myRoom="ROOM"
myRoomName="Aman API Test"
myEmail="EMAIL"
myMessage="Test API Message"

def post_message(mytoken,roomid,text):
   # The header is send to authenticate
   header = {'Authorization':mytoken, 'content-type':'application/json'}
   # NEW: we have to include the room and message text
   payload = {'roomId':roomid,'text':text }
   # NEW: we want to create something: use POST instead of GET
   # Send POST request with above header+payload. Put result in ‘result’
   result = requests.post(url='https://api.ciscospark.com/v1/messages', headers=header,json=payload)
   # Return POST request status, turned into a string ‘str(xx)’
   #    status ‘200’ means ‘succesful’.
   return str(result.status_code)


# Step 5
# Execute post_message and put result in ‘SparkResult’
SparkResult = post_message(myToken, myRoom, myMessage)
# print result
print ("--- Message post response code:", SparkResult)