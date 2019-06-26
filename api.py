from flask import jsonify,request, Response, json
import jwt, datetime
from functools import wraps
from Models import Tourist_Places
from database import app

def token_required(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		token = request.args.get('token')
		try:
			jwt.decode(token, app.config['SECRET_KEY'])
			return f(*args, **kwargs)
		except:
			return jsonify({'error': 'Need a valid Token'}), 401
	return wrapper

@app.route('/login')
def getToken():
	expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
	token = jwt.encode({'exp': expiration_date, 'id': 1}, app.config['SECRET_KEY'], algorithm='HS256')
	return token

@app.route('/verify')
@token_required
def verifyToken():
	return jsonify('Hello')

@app.route('/')
def getPlaces():
	data = Tourist_Places.get_all_places()
	return jsonify(data)

@app.route('/<int:id>')
def getPlaceWithId(id):
	data = Tourist_Places.get_place(id)
	return jsonify(data)

@app.route('/', methods=['POST'])
def insertPlace():
	requestData = request.get_json()
	data = Tourist_Places.add_place(requestData)
	return jsonify(data)

@app.route('/<int:id>', methods=['DELETE'])
def deletePlace(id):
	data = Tourist_Places.delete_place(id)
	return jsonify(data)

@app.route('/<int:id>', methods=['PUT'])
def update_placeTitle(id):
	requestData = request.get_json()
	data = Tourist_Places.update_placeTitle(id, requestData)
	return jsonify(data)

app.run(port=5000)

