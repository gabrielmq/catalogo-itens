#!/usr/bin/env python3

import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True

    SECRET_KEY = "secret_key"

    SQLALCHEMY_DATABASE_URI = os\
        .environ.get("DATABASE_URL") or "sqlite:///" + os.path\
        .join(base_dir, "catalogo_itens.db?check_same_thread=False")

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    OAUTH_CREDENTIALS = {
        "google": {
            "id": "app_id",
            "secret": "app_secret"
        },
        "facebook": {
            "id": "app_id",
            "secret": "app_secret"
        }
    }
