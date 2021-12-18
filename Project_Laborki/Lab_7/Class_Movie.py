from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Movie(Resource):
    def __init__(self, movie_id, title, genres):
        self.movie_id = movie_id
        self.title = title
        self.genres = genres

    def __str__(self):
        return f'Film {self.title}, nr id: {self.movie_id} w kategorii: {self.genres}).'

    def get(self):
        return {'hello': 'world'}


api.add_resource(Movie, '/')
