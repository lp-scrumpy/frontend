import logging

from flask import Blueprint, redirect, render_template, request, url_for

from frontend.clients.plan_client import PlanningClient
from frontend.clients.task_client import TaskClient
from frontend.clients.user_client import UserClient
from frontend.config import ENDPOINT

view = Blueprint('plannings', __name__)

logger = logging.getLogger(__name__)

plan_client = PlanningClient(ENDPOINT)
user_client = UserClient(ENDPOINT)
task_client = TaskClient(ENDPOINT)


@view.route('/<planning_id>')
def plan(planning_id):
    tasks = task_client.get_all_tasks(planning_id)
    return render_template('plannings.html', tasks=tasks, users=[], planning_id=planning_id)


@view.post('/<planning_id>/tasks/')
def create_task(planning_id):
    logger.info('task created %s %s', planning_id, request.form['task'])
    task_client.add_task(name=request.form['task'], planning_id=planning_id)
    return redirect(url_for('plannings.plan', planning_id=planning_id))


@view.post('/<planning_id>/users/')
def create_user(planning_id):
    logger.info('user created %s', planning_id)
    return redirect(url_for('plannings.plan', planning_id=planning_id))
