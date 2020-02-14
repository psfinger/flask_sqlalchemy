from flask import render_template, request, session, jsonify, url_for, g
from werkzeug.utils import redirect

from loglist import bp
from loglist.forms import SearchForm
from sql_models import Logging


@bp.before_app_request
def before_request():
    g.search_form = SearchForm()


@bp.route('/index')
@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/showAll', methods=('GET', 'POST'))
def show_all():
    # form = SearchForm()
    page = request.values.get('page', 1, type=int)
    paginate = Logging.query.order_by(Logging.id.desc()).paginate(page, 20)
    logs = paginate.items
    if logs:
        return render_template('showAll.html', paginate=paginate, logs=logs, form=g.search_form)
    return 'Not Found'


@bp.route('/search', methods=('GET', 'POST'))
def search():
    # form = SearchForm()
    # if not form.validate_on_submit():
    #   print("redirect")
    #   return redirect(url_for('loglist.show_all'))
    page = request.values.get('page', 1, type=int)
    log_filter = []
    search_level = g.search_form.level.data
    # search_level = request.values.get('search_level')
    print(g.search_form.level.data)
    print(search_level)
    if search_level:
        log_filter.append(Logging.level == search_level)
    paginate = Logging.query.filter(*log_filter).order_by(Logging.id.desc()).paginate(page, 20)
    logs = paginate.items
    if logs:
        return render_template('loglist.html', paginate=paginate, logs=logs, form=g.search_form,
                               search_level=search_level)
    return 'Not Found'
