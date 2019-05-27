from data.storage import Storage
import watering_period
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
storage = Storage("../data/data.json")


class GetAll(Resource):
    """ Class of getting all information about watering periods """
    @staticmethod
    def get():
        """ Method for HTTP-get request """
        list_ob = storage.read_all()
        response = [ob.__dict__() for ob in list_ob]
        return response


class GetById(Resource):
    """ Class of getting all information about current watering period """
    @staticmethod
    def get(period_id):
        """ Method for HTTP-get request """
        return storage.read(period_id).__dict__()


class Add(Resource):
    """ Class of adding information about new watering period """
    @staticmethod
    def post():
        """ Method for HTTP-post request """
        period = request.get_json()
        result = storage.create(
            watering_period.ob_from_dict(period)).__dict__()
        storage.save_session()
        return result, 201


class Update(Resource):
    """ Class of adding information about new watering period """
    @staticmethod
    def put():
        """ Method for HTTP-put request """
        period = request.get_json()
        if period.get("period_id") is None:
            return "", 404
        storage.update(
            period.get("period_id"),
            days=period.get("days"),
            time=period.get("time"))
        storage.save_session()
        return 200


class Delete(Resource):
    """ Class for deleting some watering period """
    @staticmethod
    def delete(period_id):
        """ Method for HTTP-delete request """
        storage.delete(period_id)
        storage.save_session()
        return 200


api.add_resource(GetAll, '/flowers')
api.add_resource(GetById, '/flowers/<int:id>')
api.add_resource(Add, '/flowers')
api.add_resource(Update, '/flowers')
api.add_resource(Delete, '/flowers/<int:id>')

app.run(debug=True)
