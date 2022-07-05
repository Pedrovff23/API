from flask import Flask, request, jsonify
from Schema import produtoCreateSchema, produtoSchema, produtoEditSchema
from models import Produto
from marshmallow.exceptions import ValidationError

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

produtosCadastrados = {}


@app.route("/produtos", methods=["GET"])
def produtoGet():
    data = dict(produtoSchema().dump(produtosCadastrados))
    return jsonify({"data": data}), 200


@app.route("/cadastro/usuario", methods=["POST"])
def produtoPost():
    try:
        data = produtoCreateSchema().load(request.json)

        models = Produto(**data)

        data = dict(produtoCreateSchema().dump(models))
        produtosCadastrados.update(data)

        return jsonify({"data": data}), 200

    except ValidationError as e:
        errors = {'message': 'Unprocessable Entity', 'errors': e.messages}
        return jsonify(errors), 422

    except Exception:

        return 'Register Produto Not Found', 404


@app.route("/alterar/usuario", methods=["PATCH"])
def produtoPatch():
    try:
        data = produtoEditSchema().load(request.json)
        produtosCadastrados.update(**data)

        return jsonify({"data": data}), 200

    except ValidationError as e:
        errors = {'message': 'Unprocessable Entity', 'errors': e.messages}
        return jsonify(errors), 422

    except Exception:

        return 'Register Produto Not Found', 404


@app.route("/deletar/usuario", methods=["DELETE"])
def produtoDelete():
    try:

        produtosCadastrados.clear()

        return '', 204

    except Exception:

        return 'Register Produto Not Found', 404
