import json
import requests

myToken="Bearer TOKEN"
myRoom="ROOM"
myRoomName="Aman API Test"
myEmail="EMAIL"
myMessage="Test API Message"

def post_membership(mytoken,roomid,email,Moderator=False):
   # The header is send to authenticate
   header = {'Authorization':mytoken, 'content-type':'application/json'}
   # NEW: we have to include the email address and room moderator status
   payload = {'roomId':roomid,'personEmail':email,'isModerator':Moderator}
   # NEW: we want to create something: use POST instead of GET
   # Send POST request with above header+payload. Put result in ‘result’
   result = requests.post(url='https://api.ciscospark.com/v1/memberships',headers=header,json=payload)
   print (result.text)
   # Return POST request status, turned into a string ‘str(xx)’
   #    status ‘200’ means ‘succesful’.
   return str(result.status_code)

# Step 4
# Execute post_membership and put result in ‘SparkResult’
SparkResult = post_membership(myToken, myRoom, myEmail)
# print result
print ("--- Member add response code:", SparkResult)