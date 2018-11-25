from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
from flask import Flask, request

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        return {'item': (filter(lambda x: x['name'] == name, items), None)}

    def post(self, name):
        if next(iter(filter(lambda x: x['name'] == name, items)), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000)
