#!/usr/bin/env python3

from flask import jsonify

from app import app, db
from app.models.model import Categoria, ItemCategoria


@app.route("/api/v1/categorias")
def categorias_json():
    categorias = db.session.query(Categoria).all()
    return jsonify(categoria=[categoria.serialize for categoria in categorias])


@app.route("/api/v1/categorias/<int:categoria_id>")
def categoria_por_id_json(categoria_id):
    categoria = db.session.query(Categoria).filter_by(id=categoria_id).one()
    return jsonify(categoria.serialize)


@app.route("/api/v1/categorias/<string:nome>")
def categoria_por_nome_json(nome):
    categoria = db.session.query(Categoria).filter_by(nome=nome).one()
    return jsonify(categoria.serialize)


@app.route("/api/v1/categorias/<int:categoria_id>/item")
def itens_categoria_json(categoria_id):
    categoria = db.session.query(Categoria).filter_by(id=categoria_id).one()
    itens = db.session.query(ItemCategoria).filter_by(categoria_id=categoria.id).all()
    return jsonify(itens_categoria=[item.serialize for item in itens])


@app.route("/api/v1/categorias/item/<int:item_id>")
def restaurant_menu_item(item_id):
    item = db.session.query(ItemCategoria).filter_by(id=item_id).one()
    return jsonify(item_categoria=item.serialize)
