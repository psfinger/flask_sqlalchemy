# 主程序

from flask import Flask, render_template
from sql_models import app, Logging


# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/log_list/<int:num>/<int:per>/')
def log_list(num, per):
    logs = Logging.query.offset((num-1)*per).limit(per)
    return render_template('list.html', logs=logs)


@app.route('/loglist/<int:page>')
def loglist(page):
    paginate = Logging.query.paginate(page, 20)
    logs = paginate.items
    if logs:
        return render_template('loglist.html', paginate=paginate, logs=logs)
    return 'Not Found'


if __name__ == '__main__':
    app.run()