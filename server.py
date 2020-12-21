from flask import Flask, jsonify, request, url_for, abort
from flask_cors import CORS
from movieDAO import movieDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')
CORS(app)
 

@app.route('/')
def index():
    return "hello there"

 
@app.route('/movies', methods=["GET"])
def get_all():
    return jsonify(movieDao.get_all())

@app.route('/movies/<int:id>')
def find_by_id(id):
    return jsonify(movieDao.find_by_id(id))

@app.route('/movies', methods=["POST"])
def create():
    if not request.json:
        abort(400)

    movie = {
        #"ISBN": request.json["ISBN"],
        "title": request.json["title"],
        "director": request.json["director"],
        "year": request.json["year"]
    }
    return jsonify(movieDao.create(movie))

@app.route('/movies/<int:id>', methods=["PUT"])
def update(id):
    found_movie = movieDao.find_by_id(id) # goes to the database for book by ISBN. Returns data primed for update, entered by user
    #print (found_movie)
    if found_movie == {}:
        return jsonify({}), 404
    current_movie = found_movie
    if "title" in request.json: # what exactly is request.json. data type?? WHat does it do?
        current_movie["title"] = request.json["title"]
    if "director" in request.json:
        current_movie["director"] = request.json["director"]
    if "year" in request.json:
        current_movie["year"] = request.json["year"]
    movieDao.update(current_movie) # book still not actually updated in database until this point here.
    
    return jsonify(current_movie)

@app.route('/movies/<int:id>', methods=["DELETE"])
def delete(id):
    if id == None:
        print("ISBN not found")
    else:
        movieDao.delete(id)
        return jsonify({"done":True})

if __name__ == "__main__":
    print("hello world")
    app.run(debug=True)
     