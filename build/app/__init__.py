from app.modules import SERVER_DATA
from flask import Flask

app = Flask(__name__)

from app import routes


app.run(
    host='0.0.0.0', 
    port=SERVER_DATA['http'], 
    debug=False, 
    use_reloader=False
)
