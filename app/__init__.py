#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from os import environ

from .api import api
from .config import configs
from .models import db


def create_app(package_name):
	app = Flask(package_name)
	config = environ.get('FLASK_ENV', 'default')
	config = configs.get(config)
	app.config.from_object(config)

	config.init_app(app)
	db.init_app(app)
	api.init_app(app)
	JWTManager(app)
	Migrate(app, db)

	return app

