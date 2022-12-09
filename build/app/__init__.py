from flask import Flask
from flask_socketio import SocketIO

from app.Manager import Manager
from app.modules import SERVER_DATA, NAME


# Setup the Flask Application.
app = Flask(__name__)

# Import all the routes/endpoints.
from app import routes


# Setup the Web Socket.
socketio = SocketIO(app, async_mode=None)

# Import the Socket methods for communication.
from app import sockets


# Start the SYNC service.
if SERVER_DATA.get('is_leader'):
    manager = Manager(NAME)
    manager.start()


# Start our Application.
socketio.run(
    app, 
    host='0.0.0.0', 
    port=SERVER_DATA['http']
)