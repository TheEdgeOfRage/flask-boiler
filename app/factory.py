#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

from flask import Flask


def create_app(package_name, config, *argv):
	app = Flask(package_name)
	app.config.from_object(config)
	config.init_app(app)

	for extension in argv:
		extension.init_app(app)

	return app


