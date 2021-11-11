from flask import Blueprint, render_template, request, session

from db_processing.db_access import db_get_data
from launch import sql_provider
from access import group_permission_decorator

auth_app = Blueprint('auth', __name__, template_folder='templates')


@auth_app.route('/', methods=['POST', 'GET'])
@group_permission_decorator
def login_page():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')

        sql_req = db_get_data(sql_provider.get('auth_user.sql', login=login))
        if len(sql_req) != 0:
            if sql_req[0][0] == password:
                session['group'] = sql_req[0][1]
                status = 'Вы успешно вошли'
            else:
                status = 'Неверный пароль'
        else:
            status = 'Пользователь не найден'
    else:
        status = None
    return render_template('login_page.html', status=status)


@auth_app.route('/exit')
@group_permission_decorator
def exit_page():
    if 'group' in session:
        session.pop('group')
        status = True
    else:
        status = False
    return render_template('exit.html', status=status)
