from app import socketio
from app.modules import datastore

from flask import session
from flask_socketio import emit



@socketio.event
def my_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1

    emit(
        'my_response',
        {
            'data': message['data'], 
            'count': session['receive_count']
        }
    )


# Receive the test request from client and send back a test response
@socketio.on('test_message')
def handle_message(key_value):
    emit(
        'test_response', 
        {
            'data': datastore.get(key_value['data'])
        }
    )


@socketio.event
def connect():
    emit(
        'my_response', 
        {
            'data': 'Connect', 
            'count': 0
        }
    )