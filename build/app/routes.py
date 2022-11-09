import time
import json
import requests

from flask import request
from flask_restful import Resource, Api

from app import app
from app.modules import datastore, SERVER_DATA, CLUSTER

api = Api(app)

class HTTPHandler(Resource):
    def get(self):
        return json.dumps(datastore), 200

    def post(self):
        content = request.get_json()

        if SERVER_DATA['is_leader']:
            for adj_node in SERVER_DATA['adj']:
                _ = requests.post(
                    url=f'http://server-{adj_node}:{CLUSTER[adj_node]["http"]}/',
                    json=content
                )
                time.sleep(1)

        datastore.update(content)

        return json.dumps({'success': True}), 200

    def delete(self):
        key = request.args.get('key')

        del datastore[key]

        return json.dumps({'success': True}), 200


api.add_resource(HTTPHandler, '/')
