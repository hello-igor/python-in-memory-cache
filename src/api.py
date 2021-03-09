from flask import request, Response
from flask_restful import Resource, reqparse
from src.cache import MyCache


c = MyCache()

parser = reqparse.RequestParser()
parser.add_argument('key')
parser.add_argument('value')
parser.add_argument('ttl')
parser.add_argument('pattern')


class SetItemApi(Resource):

    def post(self):
        args = parser.parse_args()
        if args['key'] == None:
            return 'Invalid key'
        if args['value'] == None:
            return 'Invalid value'
        if args['ttl'] != None:
            c.set_item(args['key'], args['value'], int(args['ttl']))
        else:
            c.set_item(args['key'], args['value'])
        return 201


class GetItemApi(Resource):

    def get(self, key):
        return c.get_item(key)


class DelItemApi(Resource):

    def get(self, key):
        return c.del_item(key) 


class KeysApi(Resource):

    def post(self):
        args = parser.parse_args()
        return c.keys(args['pattern'])