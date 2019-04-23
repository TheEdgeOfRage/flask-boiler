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
from flask_sqlalchemy import SQLAlchemy
from os import environ

from .config import configs

db = SQLAlchemy()


def create_app(package_name=__name__):
	app = Flask(package_name)
	config = configs.get(environ.get('FLASK_ENV', 'production'))
	app.config.from_object(config)

	JWTManager(app)
	db.init_app(app)
	Migrate(app, db)

	return app

