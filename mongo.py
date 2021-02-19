from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask import Flask,render_template

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'album'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/album'

mongo = PyMongo(app)

@app.route('/')
def index():
	return render_template('index.html')
		
@app.route('/Music/abc', methods=['GET'])
def get_abc():
  Music = mongo.db.Music
  abc = ({"name" : "abc"})
  output = []
  for s in Music.find(abc):
    output.append({'id':s['id'], 'name' : s['name'], 'duration' : s['duration'], 'time' : s['time']})
  return jsonify({'result' : output})

@app.route('/Music/pqr', methods=['GET'])
def get_pqr():
  Music = mongo.db.Music
  pqr = ({"name" : "pqr"})
  output = []
  for s in Music.find(pqr):
    output.append({'id':s['id'], 'name' : s['name'], 'duration' : s['duration'], 'time' : s['time']})
  return jsonify({'result' : output})
  
@app.route('/Music/xyz', methods=['GET'])
def get_all_music2():
  Music = mongo.db.Music
  xyz = ({"name" : "xyz"})
  output = []
  for s in Music.find(xyz):
    output.append({'id':s['id'], 'name' : s['name'], 'duration' : s['duration'], 'time' : s['time']})
  return jsonify({'result' : output})
  
@app.route("/Music/plm")
def plm():
    return render_template('page.html')

'''@app.route('/Music', methods=['POST'])
def add_music():
  Music = mongo.db.Music
  name = request.json['name']
  duration = request.json['duration']
  time = request.json['time']
  music_id = Music.insert({'name': name, 'distance': distance, 'time': time})
  new_star = Music.find_one({'_id': music_id })
  output = {'name' : new_Music['name'], 'distance' : new_Music['distance'], 'time' : new_Music['time']}
  return jsonify({'result' : output})
 ''' 


if __name__ == '__main__':
    app.run(debug=True)
