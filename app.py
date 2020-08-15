from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from http import HTTPStatus

app = Flask(__name__)
api = Api(app)


class Add(Resource):
    pass


class Subtract(Resource):
    pass


class Multiply(Resource):
    pass


class Divide(Resource):
    pass


api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')