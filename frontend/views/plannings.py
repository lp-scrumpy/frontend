from flask import Blueprint, redirect, render_template
from jinja2 import Environment, PackageLoader

from frontend.clients.user_client import UserClient
from frontend.config import ENDPOINT

view = Blueprint('plan', __name__)

env = Environment(loader=PackageLoader('frontend', 'templates'))

users_client = UserClient(ENDPOINT)


@view.route('/')
def plan():
    return redirect('/new_plan')


@view.route('/new_plan')
def new_plan():
    all_plans = users_client.get_all()
    return render_template('plannings.html', plans=all_plans)
