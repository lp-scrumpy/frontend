from flask import Blueprint, render_template
from jinja2 import Environment, PackageLoader
from frontend.clients.user_client import UserClient
from frontend.config import ENDPOINT


env = Environment(loader=PackageLoader('frontend', 'templates'))

uapp = Blueprint('user', __name__)


@uapp.route('/')
def index():
    return render_template('index.html')


@uapp.route('/users')
def user_registration():
    users_client = UserClient(ENDPOINT)
    all_users = users_client.get_all()
    template = env.get_template('name.html')
    return template.render(users=all_users)
