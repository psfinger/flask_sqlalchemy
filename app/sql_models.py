from datetime import datetime
from app import db


class Logging(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    task_type = db.Column(db.String(20))
    sys_name = db.Column(db.String(20))
    table_name = db.Column(db.String(20))
    vdate = db.Column(db.String(8))
    logger = db.Column(db.String(20))
    level = db.Column(db.String(20))
    message = db.Column(db.Text)
    create_time = db.Column(db.DATETIME, default=datetime.now())

    def __init__(self,
                 task_type,
                 sys_name,
                 table_name,
                 vdate,
                 logger,
                 level,
                 message,
                 create_time=datetime.now()
                 ):
        self.task_type = task_type
        self.sys_name = sys_name
        self.table_name = table_name
        self.vdate = vdate
        self.logger = logger
        self.level = level
        self.message = message
        self.create_time = create_time

    def __repr__(self):
        return f'[{self.create_time}]<{self.task_type} message:{self.message}>'


if __name__ == '__main__':
    # 1. 创建数据库表
    # db.drop_all()
    db.create_all()
    # 2. 创建数据库表数据
    index = 10
    while index > 0:
        log_1 = Logging(task_type='emergency',
                        sys_name='hvps',
                        table_name='HVPSZDT0101',
                        vdate='20191024',
                        logger='root',
                        level='info',
                        message='create a file susccess!')
        print(log_1)
        db.session.add(log_1)
        db.session.commit()

        log_2 = Logging(task_type='emergency',
                        sys_name='hvps',
                        table_name='HVPSZDT0102',
                        vdate='20191024',
                        logger='root',
                        level='ERROR',
                        message='hdfs process!')
        print(log_2)
        db.session.add(log_2)
        db.session.commit()

        log_3 = Logging(task_type='check',
                        sys_name='hvps',
                        table_name='HVPSZDT0102',
                        vdate='20191024',
                        logger='root',
                        level='ERROR',
                        message='hdfs process!')
        print(log_3)
        db.session.add(log_3)
        db.session.commit()

        log_4 = Logging(task_type='check',
                        sys_name='hvps',
                        table_name='HVPSZDT0102',
                        vdate='20191024',
                        logger='root',
                        level='WARNING',
                        message='hdfs process!')
        print(log_4)
        db.session.add(log_4)
        db.session.commit()
        index=index-1
