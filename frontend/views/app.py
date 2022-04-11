import logging
from flask import Blueprint, redirect, render_template, url_for
from frontend.clients.plan_client import PlanningClient

from datetime import datetime
from frontend.clients.user_client import UserClient
from frontend.config import ENDPOINT

view = Blueprint('app', __name__)

logger = logging.getLogger(__name__)

users_client = UserClient(ENDPOINT)
plan_client = PlanningClient(ENDPOINT)


@view.route('/')
def index():
    plan = plan_client.add(name='', date=datetime.now())
    logger.info(plan)
    return redirect(url_for('plannings.plan', planning_id=plan.uid))


@view.route('/users')
def user_registration():
    all_users = users_client.get_all()
    return render_template('name.html', users=all_users)
