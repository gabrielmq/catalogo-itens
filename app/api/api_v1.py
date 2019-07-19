#!/usr/bin/env python3

from flask import jsonify

from app import db
from app.api import blue_print
from app.models.model import Categoria, ItemCategoria


categorias = [
    "Soccer", "Basketball", "Baseball",
    "Frisbee", "SnowBoarding", "Rock Climbing",
    "Foosball", "Skating", "Hockey"
]


@blue_print.route("/api/categorias/all")
def insere_categorias():
    categorias_existentes = db.session.query(Categoria).count()
    if categorias_existentes == 0:
        for categoria in categorias:
            print(categoria)
            db.session.add(Categoria(nome=categoria))
            db.session.commit()

    return categorias_json()


@blue_print.route("/api/v1/categorias")
def categorias_json():
    """Busca e retorna as categorias no formato JSON"""
    categorias = db.session.query(Categoria).all()
    return jsonify(categoria=[categoria.serialize for categoria in categorias])


@blue_print.route("/api/v1/categorias/<int:categoria_id>")
def categoria_por_id_json(categoria_id):
    """Busca e retorna uma categorias no formato JSON pelo ID"""
    categoria = db.session.query(Categoria).filter_by(id=categoria_id).one()
    return jsonify(categoria.serialize)


@blue_print.route("/api/v1/categorias/<string:nome>")
def categoria_por_nome_json(nome):
    """Busca e retorna uma categorias pelo nome no formato JSON"""
    categoria = db.session.query(Categoria).filter_by(nome=nome).one()
    return jsonify(categoria.serialize)


@blue_print.route("/api/v1/categorias/<int:categoria_id>/item")
def itens_categoria_json(categoria_id):
    """Busca e retorna os itens de uma categoria no formato JSON"""
    categoria = db.session.query(Categoria).filter_by(id=categoria_id).one()
    itens = db.session.query(ItemCategoria) \
        .filter_by(categoria_id=categoria.id).all()
    return jsonify(itens_categoria=[item.serialize for item in itens])


@blue_print.route("/api/v1/categorias/item/<int:item_id>")
def item_categoria_json(item_id):
    """Busca e retorna um item de uma categorias no formato JSON pelo ID"""
    item = db.session.query(ItemCategoria).filter_by(id=item_id).one()
    return jsonify(item_categoria=item.serialize)
