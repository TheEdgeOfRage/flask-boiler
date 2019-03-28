#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

from flask_sqlalchemy import SQLAlchemy
from passlib.hash import argon2

db = SQLAlchemy()


class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.Unicode(256), unique=True, index=True, nullable=False)
	password = db.Column(db.String(128), nullable=False)

	def __init__(self, email, password):
		self.email = email
		self.password = argon2.hash(password)

	def verify_password(self, password):
		return argon2.verify(password, self.password)

	def __repr__(self):
		return f'<User {self.email}>'

