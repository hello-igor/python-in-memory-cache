from flask import Flask
from flask_restful import Api
from src.api import SetItemApi, GetItemApi, DelItemApi, KeysApi


app = Flask(__name__)
api = Api(app)
api.add_resource(SetItemApi, '/api/set')
api.add_resource(GetItemApi, '/api/get/<key>')
api.add_resource(DelItemApi, '/api/del/<key>')
api.add_resource(KeysApi, '/api/keys')

if __name__ == '__main__':
    app.run(debug=True)