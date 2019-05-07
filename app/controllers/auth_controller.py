#!/usr/bin/env python3

from flask import render_template, redirect, url_for, flash, session
from flask_login import login_user, logout_user, current_user

from app import app, db, login_manager
from app.auth.oauth import OAuthSignIn
from app.models.model import Usuario


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    logout_user()
    return redirect(url_for("categorias"))


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(Usuario).get(int(user_id))


@app.route("/authorize/<string:provider>")
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('categorias'))

    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route("/callback/<string:provider>")
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for("categorias"))

    oauth = OAuthSignIn.get_provider(provider)
    username, email, picture = oauth.callback()

    if email is None:
        flash("Falha na autenticação.")
        return redirect(url_for("categorias"))

    user = db.session.query(Usuario).filter_by(email=email).first()
    if not user:
        user = Usuario(nome=username, email=email, foto=picture)
        db.session.add(user)
        db.session.commit()

    login_user(user, True)
    return redirect(url_for("categorias"))
