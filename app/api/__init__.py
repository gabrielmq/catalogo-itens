#!/usr/bin/env python3

from flask import Blueprint

blue_print = Blueprint("api", __name__)

from app.api import api_v1