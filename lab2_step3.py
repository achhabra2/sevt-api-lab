import json
import requests

myToken="Bearer YOUR TOKEN"
myRoomName="YOUR ROOM NAME"



def post_createroom(mytoken,roomname):
   # The header is send to authenticate
   header = {'Authorization':mytoken, 'content-type':'application/json; charset=utf-8'}
   # NEW: Besides the header for authentication we want to specify the
   # name of the new room, that’s what we send in the payload.
   payload = {"title":roomname}
   # NEW: we want to create something: use POST instead of GET
   # Send POST request with above header+payload. Put result in ‘result’
   result = requests.post(url='https://api.ciscospark.com/v1/rooms', headers=header,json=payload)
   print(result.text)
   # Return POST request status, turned into a string ‘str(xx)’
   #    status ‘200’ means ‘succesful’.
   return str(result)



# Step 3
# Execute post_createroom and put result in ‘SparkResult’
SparkResult = post_createroom(myToken, myRoomName)
# # print result
print ("--- Room creation response code:", SparkResult)
