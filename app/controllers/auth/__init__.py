#!/usr/bin/env python3

from flask import Blueprint

auth = Blueprint("auth", __name__,
                 template_folder="templates",
                 static_folder="static")


from app.controllers.auth import auth_controller
