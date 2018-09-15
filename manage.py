# -*- coding: utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from zhiliao import app
from zhiliao.exts import db
from zhiliao.main.models import *
from zhiliao.auth.models import *

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
