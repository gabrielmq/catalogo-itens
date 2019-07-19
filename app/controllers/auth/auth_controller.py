#!/usr/bin/env python3

from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from app import db, login_manager
from app.controllers.auth import auth
from app.auth.oauth import OAuthSignIn
from app.models.model import Usuario


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("categoria.categorias"))


@login_manager.user_loader
def load_user(user_id):
    """Carrega o usuário que acabou de logar na sessão"""
    return db.session.query(Usuario).get(int(user_id))


@auth.route("/authorize/<provider>")
def oauth_authorize(provider):
    """Realiza a autorização oauth com o provedor de acesso informado"""

    if not current_user.is_anonymous:
        return redirect(url_for('categoria.categorias'))

    # obtem o provedor de autenticação e autoriza o acesso
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@auth.route("/callback/<provider>")
def oauth_callback(provider):
    """Callback para obter as informações do perfil do
    usuário no provedor informado"""

    if not current_user.is_anonymous:
        return redirect(url_for("categoria.categorias"))

    oauth = OAuthSignIn.get_provider(provider)
    username, email, picture = oauth.callback()

    if email is None:
        flash("Falha na autenticação.")
        return redirect(url_for("categoria.categorias"))

    # busca o usuáiro no banco, se não existir insere um novo
    user = db.session.query(Usuario).filter_by(email=email).first()
    if not user:
        user = Usuario(nome=username, email=email, foto=picture)
        db.session.add(user)
        db.session.commit()

    # loga o usuário na aplicação e retorna para a página principal
    login_user(user, True)
    return redirect(url_for("categoria.categorias"))
