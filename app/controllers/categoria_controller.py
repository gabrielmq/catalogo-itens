#!/usr/bin/env python3

from flask import jsonify, render_template

from app import app, db
from app.models.model import Categoria


@app.route("/api/v1/categorias")
def categorias_json():
    categorias = db.session.query(Categoria).all()
    return jsonify(categoria=[categoria.serialize for categoria in categorias])


@app.route("/api/v1/categorias/<string:nome>")
def categoria_json(nome):
    categoria = db.session.query(Categoria).filter_by(nome=nome).one()
    return jsonify(categoria.serialize)


@app.route("/")
@app.route("/categorias")
def categorias():
    categorias = db.session.query(Categoria).all()
    return render_template("categoria/categorias.html", categorias=categorias)
