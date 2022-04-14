import logging

from flask import Blueprint, redirect, render_template, url_for

from frontend.clients.plan_client import PlanningClient
from frontend.clients.task_client import TaskClient
from frontend.clients.user_client import UserClient
from frontend.config import ENDPOINT

task_view = Blueprint('tasks', __name__)

logger = logging.getLogger(__name__)

plan_client = PlanningClient(ENDPOINT)
user_client = UserClient(ENDPOINT)
task_client = TaskClient(ENDPOINT)

estimates = ['1', '2', '3', '5', '8', '13', '21', '?']


@task_view.get('/<int:task_id>')
def get_task_by_id(planning_id: int, task_id: int):
    task = task_client.get_by_id(task_id, planning_id)
    logger.info(task)
    return render_template(
        'estimate.html',
        task_id=task.uid,
        planning_id=planning_id,
        estimates=estimates,
    )


@task_view.get('/<int:task_id>/score')
def final_score(planning_id: int, task_id: int):
    tasks = task_client.get_all_tasks(planning_id)
    # TODO: get user estimates and display
    # users = user_client.get_all_users(planning_id)
    # estimates = estimates_client.get_estimates(planning_id)
    return render_template('final_score.html', tasks=tasks, estimates=estimates)


@task_view.get('/<int:task_id>/<estimate>')
def set_estimate(planning_id: int, task_id: int, estimate: str):
    # TODO: tasks_client.set_estimate(planning_id, task_id, estimate)
    return redirect(url_for(
        'plannings.tasks.final_score',
        planning_id=planning_id,
        task_id=task_id,
    ))