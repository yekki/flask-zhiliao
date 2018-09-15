# -*- coding: utf-8 -*-
import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost:3306/zhiliao'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(24)
