# Catalogo de itens

Este projeto é uma aplicação web de cadastro de itens para determinadas categorias que a aplicação disponibiliza. Para poder cadastrar itens o usuário deverá se logar na aplicação com sua conta do Google ou Facebook, após efetuar o login o usuário poderá cadastrar itens para as categorias.

## Pré-requisitos

- Python 3.7
- Flask
- flask-sqlalchemy
- flask-migrate
- flask-script
- sqlite3

## Executando a aplicação

- Clone o projeto https://github.com/gabrielmq/catalogo-itens.git
- Acesse o diretorio do projeto pelo prompt de comando.
- Execute o comando `pip install -r requirements.txt` para instalar todas as dependências do projeto.
- Execute o comando `python3 run.py runserver` para inicializar a aplicação.
- Com a aplicação inicializada acesse a url http://localhost:5000

## Endpoints disponibilizados pela aplicação

- /api/v1/categorias

```
{
  "categoria": [
    {
      "id": 1,
      "nome": "Soccer"
    },
    {
      "id": 2,
      "nome": "Basketball"
    },
    {
      "id": 3,
      "nome": "Baseball"
    },
    {
      "id": 4,
      "nome": "Frisbee"
    },
    ...
  ]
}
```

- /api/v1/categorias/int:categoria_id/item

```
{
  "itens_categoria": [
    {
      "categoria_id": 1,
      "descricao": "Teste",
      "id": 1,
      "titulo": "Teste 123",
      "usuario_id": 2
    },
    ...
  ]
}
```

## Licensa

Este projeto foi desenvolvido durante o Nanodegree Desenvolvedor Web Full-Stack oferecido pela Udacity.
