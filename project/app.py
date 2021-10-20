from flask import Flask, render_template, request

import launch

from db_requests_bp.db_requests_bp import service

app = Flask(__name__)
app.register_blueprint(service, url_prefix="/requests")


@app.route('/')
def main():
    end_work = request.args.get('end_work', None)
    print(end_work)
    return render_template('main.html', end_work=end_work)


if __name__ == "__main__":
    print(launch.DB_CONFIG)
    app.run(host=launch.HOST, port=launch.PORT)
