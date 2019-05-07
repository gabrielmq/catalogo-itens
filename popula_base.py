#!/usr/bin/env python3

from app import db
from app.models.model import Categoria


categorias = [
    "Soccer", "Basketball", "Baseball",
    "Frisbee", "SnowBoarding", "Rock Climbing",
    "Foosball", "Skating", "Hockey"
]

categorias_existentes = db.session.query(Categoria).all()
if not categorias_existentes:
    print("adicionando categorias...")
    for categoria in categorias:
        print(categoria)
        db.session.add(Categoria(nome=categoria))
        db.session.commit()
    print("categorias adicionadas...")
else:
    print("Já existem categorias cadastradas no banco...")
