import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Configure Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Create new data in Firestore
def create_data():
  doc_ref = db.collection(u'users').document(u'user1')
  doc_ref.set({
      u'first_name': u'John',
      u'last_name': u'Doe',
      u'age': 30
  })
  print(doc_ref.id)

# Read data from Firestore
def read_data():
  docs = db.collection(u'users').get()
  for doc in docs:
      print(u'{} => {}'.format(doc.id, doc.to_dict()))

# Update data in Firestore
def update_data():
  doc_ref = db.collection(u'users').document(u'user1')
  doc_ref.update({
      u'age': 31
  })

# Delete data from Firestore
def delete_data():
  doc_ref = db.collection(u'users').document(u'user1')
  doc_ref.delete()
create_data()