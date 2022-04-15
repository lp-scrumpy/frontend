import logging
from typing import Optional

from flask import Blueprint, redirect, render_template, request, session, url_for

from frontend.clients.estimate_client import EstimateClient
from frontend.clients.plan_client import PlanningClient
from frontend.clients.task_client import TaskClient
from frontend.clients.user_client import UserClient
from frontend.config import ENDPOINT
from frontend import schemas

task_view = Blueprint('tasks', __name__)

logger = logging.getLogger(__name__)

plan_client = PlanningClient(ENDPOINT)
user_client = UserClient(ENDPOINT)
task_client = TaskClient(ENDPOINT)
estimate_client = EstimateClient(ENDPOINT)


ESTIMATES = ['1', '2', '3', '5', '8', '13', '21', '?']


@task_view.get('/<int:task_id>')
def get_task_by_id(planning_id: int, task_id: int):
    task = task_client.get_by_id(task_id, planning_id)
    estimates = get_estimates(planning_id=planning_id, task_id=task_id)

    if get_user_estimate(estimates):
        return final_score(
            planning_id=planning_id,
            task=task,
            estimates=estimates,
        )

    logger.info(task)
    return render_template(
        'estimates.html',
        task_id=task.uid,
        planning_id=planning_id,
        estimates=ESTIMATES,
        username=session['username'],
    )


@task_view.get('/<int:task_id>/<estimate>')
def set_estimate(planning_id: int, task_id: int, estimate: str):
    task_client.set_estimates(
        planning_id=planning_id,
        task_id=task_id,
        user_id=session['userid'],
        storypoint=int(estimate) if estimate != '?' else None,
    )

    return redirect(url_for(
        'plannings.tasks.get_task_by_id',
        planning_id=planning_id,
        task_id=task_id,
    ))


def get_estimates(planning_id: int, task_id: int) -> dict[int, schemas.Estimate]:
    estimates = estimate_client.get_estimates(planning_id=planning_id, task_id=task_id)
    return {estimate.user_id: estimate for estimate in estimates}


def get_user_estimate(estimates: dict[int, schemas.Estimate]) -> Optional[int]:
    userid = session['userid']
    estimate = estimates.get(userid)
    return estimate.storypoint if estimate else None


def final_score(planning_id: int, task: schemas.Task, estimates: dict[int, schemas.Estimate]):
    users = user_client.get_all_users(planning_id)
    users_map = {user.uid: user for user in users}

    user_estimates = [
        (users_map[estimate.user_id].name, estimate.storypoint or '?')
        for _, estimate in estimates.items()
    ]

    return render_template(
        'final_score.html',
        planning_id=planning_id,
        task=task,
        user_estimates=user_estimates,
        user_estimate=get_user_estimate(estimates) or '?',
        username=session['username'],
    )


@task_view.post('/<int:task_id>/new-score')
def set_score(planning_id: int, task_id: int):
    task_client.set_score(
        planning_id=planning_id,
        task_id=task_id,
        storypoint=int(request.form['score']),
    )
    return redirect(url_for('plannings.plan', planning_id=planning_id))
