import pyrebase
import requests
from django.conf import settings
from django.core.files.storage import Storage

class FirebaseStorage(Storage):
	def __init__(self):
		print(settings.FIREBASE_CONFIG)
		self.firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)

	def _save(self, name, content):
		storage = self.firebase.storage()
		storage.child(name)
		path = storage.path
		storage.path = None
		blob = storage.bucket.blob(path)
		blob.upload_from_file(file_obj=content, size=content.size)
		return str(name).replace('\\', '/')

	def delete(self, name):
		storage = self.firebase.storage()
		storage.delete_blob(name)

	def exists(self, name):
		url = self.url(name)
		r = requests.get(url, stream=True)
		return r.status_code == 200

	def listdir(self, path):
		storage = self.firebase.storage()
		storage.child(path).list_files()

	def url(self, name):
		storage = self.firebase.storage()
		return storage.child(name).get_url(token=False)
