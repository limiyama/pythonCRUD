import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase


cred = credentials.Certificate('./ServiceAccount.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
firebase = firebase.FirebaseApplication('https://pythoncrud-3ef17-default-rtdb.firebaseio.com/', None)

#post, cria
def create():
    db.collection('pessoa').document('id').set(
      {
        'name': 'Milleny',
      }
    )

create()