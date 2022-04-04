import logging
from flask import Blueprint, redirect, render_template
from frontend.clients.plan_client import PlanningClient

from datetime import datetime
from frontend.clients.user_client import UserClient
from frontend.config import ENDPOINT

uapp = Blueprint('user', __name__)

logger = logging.getLogger(__name__)

users_client = UserClient(ENDPOINT)
plan_client = PlanningClient(ENDPOINT)


@uapp.route('/')
def index():
    plan = plan_client.add(name='', date=datetime.now())
    logger.info(plan)
    return redirect('<plan_id>')


@uapp.route('/users')
def user_registration():
    all_users = users_client.get_all()
    return render_template('name.html', users=all_users)
