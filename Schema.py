from marshmallow import fields, Schema, validate


class produtoSchema(Schema):
    id = fields.String(dump_only=True)
    nome = fields.String(required=True, allow_none=False, validate=validate.Length(min=2, max=100))
    marca = fields.String(required=True, allow_none=False, validate=validate.Length(min=2, max=100))
    preco = fields.Float(required=True, allow_none=False)

    class Meta:
        fields = ('id', 'nome', 'marca', 'preco')
        ordered = True


class produtoCreateSchema(Schema):
    id = fields.String(dump_only=True)
    nome = fields.String(required=True, allow_none=False, validate=validate.Length(min=2, max=100))
    marca = fields.String(required=True, allow_none=False, validate=validate.Length(min=2, max=100))
    preco = fields.Float(required=True, allow_none=False)

    class Meta:
        fields = ('id', 'nome', 'marca', 'preco')
        ordered = True


class produtoEditSchema(Schema):
    id = fields.String(dump_only=True)
    nome = fields.String(required=False, allow_none=False, validate=validate.Length(min=2, max=20))
    marca = fields.String(required=False, allow_none=False, validate=validate.Length(min=2, max=100))
    preco = fields.Float(required=False, allow_none=False)

    class Meta:
        fields = ('id', 'nome', 'marca', 'preco')
        ordered = True
