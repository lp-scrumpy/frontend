from flask import Blueprint, render_template
from frontend.clients.plan_client import PlanningClient
from frontend.config import ENDPOINT

view = Blueprint('plannings', __name__)

plan_client = PlanningClient(ENDPOINT)


# @view.route('/plannings')
# def plan():
#     all_plans = users_client.get_all()
#     return render_template('plannings.html', plans=all_plans)


@view.route('<plan_id>')
def plan(plan_id):
    tasks = plan_client.get_tasks(plan_id)
    return render_template('plannings.html', tasks=tasks)
