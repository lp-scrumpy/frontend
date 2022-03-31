from flask import Blueprint, render_template

from frontend.clients.user_client import UserClient
from frontend.config import ENDPOINT


uapp = Blueprint('user', __name__)

users_client = UserClient(ENDPOINT)


@uapp.route('/')
def index():
    return render_template('index.html')


@uapp.route('/users')
def user_registration():
    all_users = users_client.get_all()
    return render_template('name.html', users=all_users)
