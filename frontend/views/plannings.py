from flask import Blueprint, redirect, render_template
from frontend.clients.plan_client import PlanningClient
from frontend.config import ENDPOINT

view = Blueprint('plan', __name__)

users_client = PlanningClient(ENDPOINT)


@view.route('/')
def plan():
    return redirect('/new_plan')


@view.route('/new_plan')
def new_plan():
    all_plans = users_client.get_all()
    return render_template('plannings.html', plans=all_plans)
