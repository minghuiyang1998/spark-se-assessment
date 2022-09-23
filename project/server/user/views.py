from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

users_blueprint = Blueprint('users', __name__)

class RegisterAPI(MethodView):
    """
    list all users
    """

    def get(self):
        list = db.session.query(User).all()
        result = []
        for n in list:
            result.append(n.email)
        print(result)
        responseObject = {
            'status': 'success',
            'message': 'Request successful but please send an HTTP POST request to list users.',
            'all': result
        }
        return make_response(responseObject), 201

# define the API resources
users_view = RegisterAPI.as_view('users_api')

# add Rules for API Endpoints
users_blueprint.add_url_rule(
    '/users/index',
    view_func=users_view,
    methods=['GET']
)