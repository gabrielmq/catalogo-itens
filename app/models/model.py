#!/usr/bin/env python3


from flask_login import UserMixin

from app import db


class Usuario(UserMixin, db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    foto = db.Column(db.String(250))

    def __init__(self, nome, email, foto):
        self.nome = nome
        self.email = email
        self.foto = foto

    def __repr__(self):
        return "<Usuario {0}>".format(self)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "foto": self.foto
        }


class Categoria(db.Model):
    __tablename__ = "categorias"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(250), nullable=False)

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return "<Categoria {0}>".format(self)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "nome": self.nome
        }


class ItemCategoria(db.Model):
    __tablename__ = "item_categoria"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(80), nullable=False, unique=True)
    descricao = db.Column(db.String(250))

    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.id"))

    usuario = db.relationship(Usuario, foreign_keys=usuario_id)
    categoria = db.relationship(Categoria, foreign_keys=categoria_id)

    def __init__(self, titulo, descricao, usuario_id, categoria_id):
        self.titulo = titulo
        self.descricao = descricao
        self.usuario_id = usuario_id
        self.categoria_id = categoria_id

    def __repr__(self):
        return "<ItemCategoria {0}>".format(self)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "usuario_id": self.usuario_id,
            "categoria_id": self.categoria_id
        }
