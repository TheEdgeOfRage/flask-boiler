#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from app.models import User, db
from app.schemas import UserSchema


class UserResource(Resource):
	schema = UserSchema()

	def get(self, user_id):
		user = User.query.filter_by(id=user_id).first()
		if user is None:
			return {'error': 'No user found'}, 404

		return self.schema.dump(user)


class UserListResource(Resource):
	schema = UserSchema()

	def get(self):
		users = User.query.all()
		result = []
		for user in users:
			result.append(self.schema.dump(user))

		return result

	def post(self):
		email = request.json['email']
		password = request.json['password']
		user = User(email=email, password=password)
		db.session.add(user)
		db.session.commit()

		return self.schema.dump(user)


class UserLogin(Resource):
	def post(self):
		if not request.is_json:
			return {'msg': 'Missing JSON in request'}, 400

		email = request.json.get('email', None)
		password = request.json.get('password', None)
		if not email:
			return {'msg': 'Missing username parameter'}, 400
		if not password:
			return {'msg': 'Missing password parameter'}, 400

		user = User.query.filter_by(email=email).first()
		if user is None or not user.verify_password(password):
			return {'msg': 'Wrong username or password'}, 401

		access_token = create_access_token(identity=email)
		return {'token': access_token}, 200

