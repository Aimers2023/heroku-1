# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore, db
# from math import cos, asin, sqrt, pi

# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://locationfinder-1144b-default-rtdb.firebaseio.com/'
# })

# ref = db.reference('Contacts')

# lati1 = 41.1234567
# long1 = -73.0987654
# req_distance = 60
# limit = 4


# def distance(lat1, lon1, lat2, lon2):
#     p = pi/180
#     a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
#     return (12742 * asin(sqrt(a)))


# cont = ref.order_by_child("lati").get()
# for i in cont.items():
#     a = (i[1]['lati'])
#     b = (i[1]['longi'])

#     cal_dist = distance(lati1, long1, a, b)

#     if (cal_dist <= req_distance):
#         print(i[1]['name'], i[1]['Contact'], int(cal_dist))
#         limit -= 1

#     if (limit == 0):
#         break
