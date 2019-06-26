from flask import jsonify
from database import db
import json

class Tourist_Places(db.Model):
	__tablename__ = 'tourist_places'
	id = db.Column('id', db.Integer, primary_key=True)
	title = db.Column('title', db.String(80), nullable=False)
	description = db.Column('description', db.String(100), nullable=False)
	image_url = db.Column('image_url', db.String(100), nullable=False)

	def __init__(self, title, description, image_url):
	   self.title = title
	   self.description = description
	   self.image_url = image_url

	def json(self):
		try:
			return { "id": self.id, "title": self.title, "description": self.description, "image_url": self.image_url}
		except:
			return {"error" : True, "message": "Item does not exist"}

	def add_place(data):
		try:
			new_place = Tourist_Places(data['title'], data['description'], data['image_url'])
			db.session.add(new_place)
			db.session.commit()
			return {"error" : False, "message": "Item added successfully"}
		except:
			return {"error" : True, "message": "Could not insert Item"}

	def get_all_places():
		return [Tourist_Places.json(place) for place in Tourist_Places.query.all()]

	def get_place(id):
		return Tourist_Places.json(Tourist_Places.query.filter_by(id=id).first())

	def delete_place(id):
		try:
			Tourist_Places.query.filter_by(id=id).delete()
			db.session.commit()
			return {"error" : False, "message": "Item deleted successfully"}
		except:
			return {"error" : True, "message": "Could not delete Item"}

	def update_placeTitle(id, data):
		try:
			place_to_update = Tourist_Places.query.filter_by(id=id).first()
			place_to_update.title = data['title']
			db.session.commit()
			return {"error" : False, "message": "Item updated successfully"}
		except:
			return {"error" : True, "message": "Could not update Item"}

	def __repr__(self):
		place_object = {
			'id' : self.id,
			'title' : self.title,
			'description' :self.description,
			'image_url' : self.image_url
		}
		return json.dumps(place_object)