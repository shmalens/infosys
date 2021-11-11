from functools import wraps

from flask import session, request, render_template

from launch import ACCESS_CONFIG


def group_permission_validation():
    access_config = ACCESS_CONFIG
    group_name = session.get('group', 'unauthorized')

    target_app = "" if len(request.endpoint.split('.')) == 1 else request.endpoint.split('.')[1]

    if (group_name in access_config) and (target_app in access_config[group_name]):
        return True
    return False


def group_permission_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if group_permission_validation():
            return func(*args, **kwargs)
        return render_template('main.html')

    return wrapper
