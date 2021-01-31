# project/server/users/views.py

# Resources used:
# https://flask.palletsprojects.com/en/1.1.x/tutorial/views/
# https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm

from flask import Blueprint, make_response, jsonify

from project.server import db
from project.server.models import User

# Create a blueprint to collect views related to users
users_blueprint = Blueprint('users', __name__, url_prefix='/users')

@users_blueprint.route('/index', methods=["GET"])
def get_users():
    # Query the database
    response = db.session.query(User).all()

    # Create and send a response with the users' emails
    responseObject = {
        'users': [row.email for row in response],
    }
    return make_response(jsonify(responseObject)), 200