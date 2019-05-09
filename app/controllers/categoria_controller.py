#!/usr/bin/env python3

from flask import render_template, redirect, url_for, flash, session, request
from flask_login import current_user

from app import app, db
from app.models.model import Categoria, ItemCategoria


@app.route("/")
@app.route("/categorias")
def categorias():
    categorias = db.session.query(Categoria).all()
    ultimos_itens = db.session.query(ItemCategoria).order_by(db.desc(ItemCategoria.id)).limit(10)
    return render_template("categoria/categorias.html",
                           categorias=categorias,
                           itens=ultimos_itens)


@app.route("/categorias/<int:categoria_id>", methods=["GET", "POST"])
def itens_categoria(categoria_id):
    if current_user.is_anonymous:
        return redirect(url_for('login'))

    categoria = db.session.query(Categoria).filter_by(id=categoria_id).one()
    itens = db.session.query(ItemCategoria).filter_by(categoria_id=categoria.id).all()
    return render_template("", categoria=categoria, itens=itens)


@app.route('/categorias/<int:categoria_id>/item/<int:item_id>',
           methods=['GET', 'POST'])
def item_categoria(categoria_id, item_id):
    if current_user.is_anonymous:
        return redirect(url_for('login'))

    categoria = db.session.query(Categoria).filter_by(id=categoria_id).one()
    item_categ = db.session.query(ItemCategoria).filter_by(categoria_id=categoria.id).filter_by(id=item_id).one()

    return render_template("", categoria=categoria, item=item_categ)


@app.route('/categorias/item', methods=['GET', 'POST'])
def novo_item_categoria():
    if current_user.is_anonymous:
        return redirect(url_for('login'))

    categorias = db.session.query(Categoria).all()
    if request.method == "POST":
        novo_item = ItemCategoria(titulo=request.form["titulo"], descricao=request.form["descricao"],
                                  usuario_id=session["user_id"], categoria_id=request.form["categoria"])
        db.session.add(novo_item)
        db.session.commit()

        return redirect(url_for("categorias"))

    return render_template("item_categoria/novo-item.html", categorias=categorias)


@app.route('/categoria/<int:categoria_id>/item/<int:item_id>/editar',
           methods=['GET', 'POST'])
def editar_item_categoria(categoria_id, item_id):
    if current_user.is_anonymous:
        return redirect(url_for('login'))

    categoria = db.session.query(Categoria).filter_by(id=categoria_id).one()
    item_editado = db.session.query(ItemCategoria).filter_by(categoria_id=categoria.id).filter_by(id=item_id).one()

    if request.method == "POST":
        if request.form["titulo"]:
            item_editado.titulo = request.form["titulo"]
        if request.form["descricao"]:
            item_editado.descricao = request.form["descricao"]

        db.session.add(item_editado)
        db.session.commit()
        return redirect(url_for("", categoria_id=categoria_id))

    return render_template("", categoria_id=categoria_id, item_id=item_id, item=item_editado)


@app.route("/categorias/<int:categoria_id>/item/<int:item_id>/deletar",
           methods=['GET', 'POST'])
def delete_menu_item(categoria_id, item_id):
    item = db.session.query(ItemCategoria).filter_by(id=item_id).one()

    if request.method == "POST":
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for("", categoria_id=categoria_id, item_id=item_id))

    return render_template("", categoria_id=categoria_id, item_id=item_id, item=item)
