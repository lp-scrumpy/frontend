import logging
from flask import Blueprint, render_template
from frontend.clients.plan_client import PlanningClient
from frontend.clients.task_client import TaskClient
from frontend.clients.user_client import UserClient
from frontend.config import ENDPOINT

view = Blueprint('plannings', __name__)

logger = logging.getLogger(__name__)

plan_client = PlanningClient(ENDPOINT)
user_client = UserClient(ENDPOINT)
task_client = TaskClient(ENDPOINT)


@view.route('<planning_id>')
def plan(planning_id):
    tasks = task_client.get_all_tasks(planning_id)
    return render_template('plannings.html', tasks=tasks)


