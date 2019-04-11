#! /bin/sh
#
# entrypoint.sh
# Copyright (C) 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.
#

sleep 2
flask db upgrade
gunicorn -w 4 --bind 0.0.0.0:80 run:app

