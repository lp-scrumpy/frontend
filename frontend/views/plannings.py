import logging

from flask import (Blueprint, abort, redirect, render_template, request,
                   session, url_for)

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


@view.route('/<int:planning_id>')
def plan(planning_id: int):
    username, userid = session.get('username'), session.get('userid')
    planning = plan_client.get_by_id(planning_id)
    if not planning:
        abort(404, "Planning not found")

    tasks = task_client.get_all_tasks(planning_id)
    users = user_client.get_all_users(planning_id)
    users_set = {user.uid for user in users}

    if userid and username and userid not in users_set:
        username, userid = None, None

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

    user = user_client.add_user(name=request.form['user'], planning_id=planning_id)

    session['userid'] = user.uid
    session['username'] = user.name

    return redirect(url_for('plannings.plan', planning_id=planning_id))
