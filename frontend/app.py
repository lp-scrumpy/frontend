from flask import Blueprint, render_template
from jinja2 import Environment, PackageLoader

users = [
    {"uid": 1, "username": "Миша"},
    {"uid": 2, "username": "Маша"},
    {"uid": 3, "username": "Cаша"},
    {"uid": 4, "username": "Оля"},
]


env = Environment(loader=PackageLoader('frontend', 'templates'))

uapp = Blueprint('user', __name__)


@uapp.route('/')
def index():
    return render_template('index.html')


@uapp.route('/users')
def user_registration():
    template = env.get_template('name.html')
    return template.render(users=users)
