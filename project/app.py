from flask import Flask, render_template, request

import launch

from db_requests_bp.db_requests_bp import service
from auth.auth import auth_app

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my super secret key'

app.register_blueprint(service, url_prefix="/requests")
app.register_blueprint(auth_app, url_prefix="/login")


@app.route('/')
def main():
    end_work = request.args.get('end_work', None)
    return render_template('main.html', end_work=end_work)


if __name__ == "__main__":
    app.run(host=launch.HOST, port=launch.PORT)
