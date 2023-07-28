from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socket = SocketIO(app, cors_allowed_origins='*')

# default route
@app.route('/')
def home():
    return render_template('index.html')

# send message socket system
@socket.on('message')
def msg_manager(message):
    send(message, broadcast=True)
    
# runs app using cors config and socketio 
socket.run(app, host='192.168.1.4', debug=True)