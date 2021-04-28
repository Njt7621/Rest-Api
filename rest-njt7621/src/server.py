from flask import Flask
from flask_restful import Resource, Api
from api.movies import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Movies, '/')
api.add_resource(MoviesDetails, '/details')
api.add_resource(MoviesShown, '/shown/<id>')

if __name__ == '__main__':
    app.run(debug=True)