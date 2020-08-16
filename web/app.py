from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from http import HTTPStatus

app = Flask(__name__)
api = Api(app)


def check_posted_data(posted_data, function_name):
    if function_name == "add" or function_name == "subtract" or function_name == "multiply":
        if "x" not in posted_data or "y" not in posted_data:
            return 301,
        else:
            return 200
    else:
        if posted_data['y'] == 0:
            return 302,
        else:
            return 200


class Add(Resource):

    def post(self):
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, function_name="add")

        if status_code != 200:
            return {"message": "An error has occurred"}, HTTPStatus.NOT_ACCEPTABLE
        else:
            z = posted_data['x'] + posted_data['y']
            return {"x + y = ": z}, HTTPStatus.OK


class Subtract(Resource):

    def post(self):
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, function_name="subtract")

        if status_code != 200:
            return {"message": "An error has occurred"}, HTTPStatus.NOT_ACCEPTABLE
        else:
            z = posted_data['x'] - posted_data['y']
            return {"x - y = ": z}, HTTPStatus.OK


class Multiply(Resource):

    def post(self):
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, function_name="multiply")

        if status_code != 200:
            return {"message": "An error has occurred"}, HTTPStatus.NOT_ACCEPTABLE
        else:
            z = posted_data['x'] * posted_data['y']
            return {"x * y = ": z}, HTTPStatus.OK


class Divide(Resource):

    def post(self):
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, function_name="divide")

        if status_code != 200:
            return {"message": "An error has occurred"}, HTTPStatus.NOT_ACCEPTABLE
        else:
            z = posted_data['x'] / posted_data['y']
            return {"x / y = ": z}, HTTPStatus.OK


api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
