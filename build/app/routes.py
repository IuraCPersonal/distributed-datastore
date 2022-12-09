import json, random, requests, time

from flask_restful import Resource, Api
from flask import request, render_template, make_response, jsonify

from app import app
from app.modules import *
from app.utils.ManageCluster import ManageCluster


api = Api(app)


class HTTPHandler(Resource):
    # GET Method
    def get(self):
        r, excedeed_requests = None, 10
        target_host = NAME
        arg = request.args.get('key', None)

        # Here is the Load Balancer. A bit dummy 💤
        if SERVER_DATA.get('is_leader'):
            while r is None or r.status_code == 404 or excedeed_requests == 0:
                target_id = SERVERS_LIST.index(target_host) + 1 % len(SERVERS_LIST)
                target_host = SERVERS_LIST[target_id]
                target_port = CLUSTER.get(target_host).get('http')

                r = requests.get(
                    url=f'http://server-{target_host}:{target_port}',
                    params={'key': arg}
                )

                excedeed_requests -= 1

            return r.json()

        
        if arg is not None:
            try:
                r = datastore[arg]
            except KeyError:
                return make_response(
                    jsonify({'Error': 'Key Not Found'}),
                    404
                )
        else:
            r = datastore.copy()

        response = make_response(
            jsonify(r),
            200
        )

        return response

    
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


@app.route('/client')
def index():
    return render_template('index.html')


@app.route('/upload')
# UPLOAD Method
def upload():
    file = request.files['file'].read()

    if file.filename != '':
        file.save(file.filename)

    return json.dumps({'success': True}), 200


api.add_resource(HTTPHandler, '/')
