#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

from os import environ

DB_URI = environ.get('DB_URI', None)
if DB_URI is None:
	DB_ENGINE = environ.get('DB_ENGINE', 'postgresql')
	DB_USER = environ.get('DB_USER', 'root')
	DB_PASSWORD = environ.get('DB_PASSWORD', None)
	DB_HOST = environ.get('DB_HOST', 'localhost')
	DB_PORT = environ.get('DB_PORT', '5432')
	DB_NAME = environ.get('DB_NAME', None)


class BaseConfig:
	DEBUG = False
	TESTING = False
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_RECORD_QUERIES = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = DB_URI or f'{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
	JWT_SECRET_KEY = None


class DevConfig(BaseConfig):
	DEBUG = True
	TESTING = True
	JWT_SECRET_KEY = 'default-secret'


class TestConfig(BaseConfig):
	DEBUG = True
	TESTING = True
	JWT_SECRET_KEY = environ.get('SECRET_KEY', 'default-secret')


class ProdConfig(BaseConfig):
	DEBUG = False
	TESTING = False
	JWT_SECRET_KEY = environ.get('SECRET_KEY', None)


configs = {
	'development': DevConfig,
	'testing': TestConfig,
	'production': ProdConfig,
}

