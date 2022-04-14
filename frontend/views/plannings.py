import logging

from flask import (Blueprint, redirect, render_template, request, session,
                   url_for)

from frontend.clients.plan_client import PlanningClient
from frontend.clients.task_client import TaskClient
from frontend.clients.user_client import UserClient
from frontend.config import ENDPOINT
from frontend.views.tasks import task_view

view = Blueprint('plannings', __name__)
view.register_blueprint(task_view, url_prefix='/<int:planning_id>/tasks')

logger = logging.getLogger(__name__)

plan_client = PlanningClient(ENDPOINT)
user_client = UserClient(ENDPOINT)
task_client = TaskClient(ENDPOINT)


@view.route('/<planning_id>')
def plan(planning_id):
    username, userid = session.get('username'), session.get('userid')
    tasks = task_client.get_all_tasks(planning_id)
    users = user_client.get_all_users(planning_id)
    return render_template(
        'plannings.html',
        username=username,
        userid=userid,
        users=users,
        tasks=tasks,
        planning_id=planning_id
    )


@view.post('/<planning_id>/tasks/')
def create_task(planning_id):
    logger.info('task created %s %s', planning_id, request.form['task'])
    task_client.add_task(name=request.form['task'], planning_id=planning_id)
    return redirect(url_for('plannings.plan', planning_id=planning_id))


@view.post('/<planning_id>/users/')
def create_user(planning_id):
    logger.info('user created %s', planning_id)
    user_client.add_user(name=request.form['user'], planning_id=planning_id)

    session['userid'] = 1
    session['username'] = request.form['user']
    return redirect(url_for('plannings.plan', planning_id=planning_id))
