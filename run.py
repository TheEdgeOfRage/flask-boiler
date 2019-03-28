#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

from flask_migrate import Migrate
from os import environ

from app import create_app
from app.api import api
from app.config import configs
from app.models import db

config = environ.get('FLASK_ENV', 'default')
config = configs.get(config)

app = create_app(package_name=__name__, config=config, extensions=[api, db])
migrate = Migrate(app, db)

