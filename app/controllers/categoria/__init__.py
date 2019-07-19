#!/usr/bin/env python3

from flask import Blueprint

categ = Blueprint("categoria", __name__,
                  template_folder="templates",
                  static_folder="static")


from app.controllers.categoria import categoria_controller