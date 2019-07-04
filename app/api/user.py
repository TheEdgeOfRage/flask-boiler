#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
	create_access_token,
	create_refresh_token,
	jwt_required,
	jwt_refresh_token_required,
	get_jwt_identity,
)

from common import db
from app.models.user import User
from app.schemas.user import UserSchema


class UserResource(Resource):
	user_schema = UserSchema()

	@jwt_required
	def get(self, user_id):
		user = User.query.filter_by(id=user_id).first()
		if user is None:
			return {'error': 'No user found'}, 404

		return self.user_schema.dump(user)


class UserListResource(Resource):
	user_schema = UserSchema()

	@jwt_required
	def get(self):
		return [self.user_schema.dump(user) for user in User.query.all()]

	def post(self):
		email = request.json['email']
		password = request.json['password']
		user = User(email=email, password=password)
		db.session.add(user)
		db.session.commit()

		return self.user_schema.dump(user)


class LoginResource(Resource):
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

		ret = {
			'access_token': create_access_token(identity=email),
			'refresh_token': create_refresh_token(identity=email)
		}

		return ret, 200


class RefreshResource(Resource):
	@jwt_refresh_token_required
	def post(self):
		current_email = get_jwt_identity()
		ret = {
			'access_token': create_access_token(identity=current_email)
		}

		return ret, 200

