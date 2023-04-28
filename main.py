
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from fastapi import FastAPI
from pydantic import BaseModel
import googlemaps

app = FastAPI()

cred = credentials.Certificate("admin-24882-firebase-adminsdk-mvtlj-d91a9c6b50.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://admin-24882-default-rtdb.firebaseio.com'
})
gmaps = googlemaps.Client(key='AIzaSyCMBI0WFadrI9Pk7v8aK4qWbbtNQ4aMZmw')

ref = db.reference('volunteers')

class Parameters(BaseModel):
    lat: float
    longi: float
    dist: int
    limit: int

def myFunc(e):
  return e['Distance']

@app.post("/getPreferences")
def getPreferences(parameter: Parameters):

    list =[]
    cont = ref.order_by_child('address').get()
    print(cont)
    for i in cont.items():
        print(i)
        volunteer = (i[1]['address']['lat'],i[1]['address']['lang'])
        origin = (parameter.lat, parameter.longi)
        
        #distance calculation function using live location coordinates and database
        my_dist = gmaps.distance_matrix(origin, volunteer, mode='driving')['rows'][0]['elements'][0]
        distance = my_dist['distance']['text'].split()[0]
        
        result ={}
        if (float(distance) <= parameter.dist):
            result['Name'] = i[1]['personal_detail']['name']
            result['Contact'] = (i[1]['personal_detail']['mobile'])
            result['Distance'] = float(distance)
            
            list.append(result)
            
    list.sort(key=myFunc)
    print(list[:parameter.limit])
    return list[:parameter.limit]
