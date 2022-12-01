import time
import json
import requests

from flask import request
from flask_restful import Resource, Api

from app import app
from app.utils.ManageCluster import ManageCluster
from app.modules import datastore, SERVER_DATA, CLUSTER, SERVERS_LIST, NAME

api = Api(app)

class HTTPHandler(Resource):
    # GET Method
    def get(self):
        return json.dumps(datastore), 200

    
    # POST Method
    def post(self):
        content = request.get_json()

        datastore.update(content)

        # Function to Distribute Data across the cluster.
        ManageCluster.dist_data(datastore)

        return json.dumps({'success': True}), 200

    
    # UPDATE Method
    def update(self):
        content = request.get_json()

        datastore.update(content)

        return json.dumps({'success': True}), 200


    # DELETE Method
    def delete(self):
        key = request.args.get('key')

        del datastore[key]

        return json.dumps({'success': True}), 200


api.add_resource(HTTPHandler, '/')
