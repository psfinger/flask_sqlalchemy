from flask_wtf import Form
from wtforms import StringField, DateTimeField, SubmitField


class SearchForm(Form):
    task_type = StringField('task_type')
    sys_name = StringField('sys_name')
    table_name = StringField('table_name')
    vdate = StringField('vdate')
    logger = StringField('logger')
    level = StringField('level')
    message = StringField('message')
    create_time = DateTimeField('create_time')
    submit = SubmitField('submit')
