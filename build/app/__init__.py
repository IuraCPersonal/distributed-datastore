import time
import requests

from flask import Flask
from app.modules import SERVER_DATA, CLUSTER, SERVERS_LIST, datastore, NAME
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)

from app import routes


app.run(
    host='0.0.0.0', 
    port=SERVER_DATA['http'], 
    debug=False, 
    use_reloader=False
)
