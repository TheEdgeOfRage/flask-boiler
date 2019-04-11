#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

from flask_restful import Api
from .user import UserResource, UserListResource, LoginResource, RefreshResource

api = Api()
api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<user_id>')
api.add_resource(LoginResource, '/login')
api.add_resource(RefreshResource, '/refresh')

